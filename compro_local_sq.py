import streamlit as st
import base64

# ==============================================================================
# CONFIGURACIÓN DE PÁGINA (Debe ser lo primero en Streamlit)
# ==============================================================================
st.set_page_config(
    page_title="Compro Local - SQ",
    page_icon="🏪",
    layout="wide",
    initial_sidebar_state="collapsed"  # Ocultar barra lateral en móvil por defecto
)

# ==============================================================================
# ESTILOS CSS PERSONALIZADOS (Para un look llamativo y móvil)
# ==============================================================================
def local_css():
    st.markdown(f"""
    <style>
        /* Paleta de colores: Vibrante, cálida, local */
        :root {{
            --primary-color: #FF6B35; /* Naranja vibrante */
            --secondary-color: #F7C59F; /* Melocotón suave */
            --background-color: #FFF8F0; /* Fondo crema */
            --text-color: #2D3142; /* Azul oscuro profundo */
            --accent-color: #EF476F; /* Rosa fuerte para acentos */
            --success-color: #06D6A0; /* Verde menta para acciones */
        }}

        /* Fondo general de la app */
        .stApp {{
            background-color: var(--background-color);
            color: var(--text-color);
        }}

        /* Ocultar el header y footer de Streamlit para parecer una app nativa */
        header {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        #MainMenu {{visibility: hidden;}}

        /* Título principal */
        h1 {{
            color: var(--primary-color);
            text-align: center;
            font-family: 'Arial Black', sans-serif;
            font-size: 2.5rem !important;
            margin-bottom: 0rem;
        }}
        h2, h3 {{
            color: var(--text-color);
            font-family: 'Arial', sans-serif;
        }}

        /* Tarjetas de negocios/productos */
        .card {{
            background-color: white;
            border-radius: 20px;
            padding: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            margin-bottom: 15px;
            border: 2px solid var(--secondary-color);
            transition: transform 0.2s;
        }}
        .card:hover {{
            transform: scale(1.02);
            border-color: var(--primary-color);
        }}

        /* Imágenes de las tarjetas */
        .card img {{
            border-radius: 15px;
            width: 100%;
            height: 150px;
            object-fit: cover;
        }}

        /* Botones */
        .stButton > button {{
            background-color: var(--primary-color);
            color: white;
            border-radius: 25px;
            padding: 10px 25px;
            font-weight: bold;
            border: none;
            width: 100%;
            transition: background-color 0.3s;
        }}
        .stButton > button:hover {{
            background-color: var(--accent-color);
            color: white;
        }}

        /* Etiquetas de promoción */
        .promo-badge {{
            background-color: var(--accent-color);
            color: white;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 0.8rem;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 5px;
        }}

        /* Precios */
        .price {{
            color: var(--success-color);
            font-size: 1.2rem;
            font-weight: bold;
        }}

        /* Navegación inferior (simulada con radio buttons) */
        .stRadio > div {{
            display: flex;
            justify-content: space-around;
            background-color: white;
            padding: 10px;
            border-radius: 30px;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
        }}
        .stRadio > div > label {{
            background-color: transparent !important;
            padding: 10px !important;
            border-radius: 20px !important;
        }}
        .stRadio > div > label[data-checked="true"] {{
            background-color: var(--secondary-color) !important;
        }}
    </style>
    """, unsafe_allow_html=True)

local_css()

# ==============================================================================
# DATOS SIMULADOS (Para la Fase 1)
# ==============================================================================
# En la Fase 2, estos datos vendrán de Supabase.
NEGOCIOS = [
    {"id": 1, "nombre": "Panadería La Espiga", "categoria": "Comida", "descripcion": "Pan fresco y tradicional horneado a leña.", "imagen": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400&h=300&fit=crop", "destacado": True},
    {"id": 2, "nombre": "Café Quilichao", "categoria": "Café", "descripcion": "Café de origen local, cultivado en las montañas.", "imagen": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=400&h=300&fit=crop", "destacado": True},
    {"id": 3, "nombre": "Artesanías del Valle", "categoria": "Artesanías", "descripcion": "Tejidos y cerámicas hechas por artesanos locales.", "imagen": "https://images.unsplash.com/photo-1590736969955-71cc94901144?w=400&h=300&fit=crop", "destacado": False},
    {"id": 4, "nombre": "Frutas y Verduras Don Pedro", "categoria": "Mercado", "descripcion": "Productos frescos del campo directamente a tu mesa.", "imagen": "https://images.unsplash.com/photo-1542838132-92c53300491e?w=400&h=300&fit=crop", "destacado": False},
]

PRODUCTOS = [
    {"id": 101, "negocio_id": 1, "nombre": "Pan de Bono (x6)", "precio": 6000, "imagen": "https://images.unsplash.com/photo-1598373182133-52452f7691ef?w=400&h=300&fit=crop", "promocion": "2x1 los martes"},
    {"id": 102, "negocio_id": 1, "nombre": "Torta de Chocolate", "precio": 25000, "imagen": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=300&fit=crop", "promocion": None},
    {"id": 103, "negocio_id": 2, "nombre": "Café Molido 500g", "precio": 18000, "imagen": "https://images.unsplash.com/photo-1559525839-b184a4d698c7?w=400&h=300&fit=crop", "promocion": "Envío gratis"},
    {"id": 104, "negocio_id": 4, "nombre": "Canasta de Frutas", "precio": 30000, "imagen": "https://images.unsplash.com/photo-1610832958506-aa56368176cf?w=400&h=300&fit=crop", "promocion": "10% de descuento"},
]

PROMOCIONES = [
    {"id": 1, "titulo": "Martes de Pan de Bono", "negocio": "Panadería La Espiga", "descripcion": "Lleva 6 panes y paga 3.", "imagen": "https://images.unsplash.com/photo-1598373182133-52452f7691ef?w=400&h=300&fit=crop"},
    {"id": 2, "titulo": "Café con Envío Gratis", "negocio": "Café Quilichao", "descripcion": "En pedidos superiores a $20.000.", "imagen": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=400&h=300&fit=crop"},
]

# ==============================================================================
# BARRA DE NAVEGACIÓN (Simula la parte inferior de una app móvil)
# ==============================================================================
# Usamos un radio horizontal para simular los tabs de una app.
# En la Fase 4, esto se puede personalizar aún más.
seccion = st.radio(
    "Navegación",
    ["🏠 Inicio", "🏪 Negocios", "🛒 Productos", "🎉 Promos"],
    horizontal=True,
    label_visibility="collapsed"
)

# ==============================================================================
# CONTENIDO DE CADA SECCIÓN
# ==============================================================================

if seccion == "🏠 Inicio":
    st.markdown("<h1>Compro Local - SQ</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Apoya lo nuestro. Compra en Santander de Quilichao.</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&h=300&fit=crop", use_container_width=True, caption="Lo mejor de nuestra tierra, a un clic.")
    
    st.subheader("⭐ Destacados de la Semana")
    cols = st.columns(2)
    for i, negocio in enumerate([n for n in NEGOCIOS if n["destacado"]]):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="card">
                <img src="{negocio['imagen']}" alt="{negocio['nombre']}">
                <h4 style="margin-top: 10px; margin-bottom: 5px;">{negocio['nombre']}</h4>
                <p style="font-size: 0.9rem; color: #555;">{negocio['descripcion']}</p>
                <span class="promo-badge">Recomendado</span>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Ver {negocio['nombre']}", key=f"btn_dest_{negocio['id']}"):
                st.session_state.seccion = "🏪 Negocios" # Simula navegación
                st.rerun()

elif seccion == "🏪 Negocios":
    st.markdown("<h2>🏪 Negocios Locales</h2>", unsafe_allow_html=True)
    st.write("Descubre los emprendimientos que hacen grande a Quilichao.")
    
    for negocio in NEGOCIOS:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(negocio["imagen"], use_container_width=True)
        with col2:
            st.subheader(negocio["nombre"])
            st.caption(f"Categoría: {negocio['categoria']}")
            st.write(negocio["descripcion"])
            if negocio["destacado"]:
                st.markdown('<span class="promo-badge">⭐ Destacado</span>', unsafe_allow_html=True)
        st.divider()

elif seccion == "🛒 Productos":
    st.markdown("<h2>🛒 Productos</h2>", unsafe_allow_html=True)
    st.write("Pide directamente y apoya al productor local.")
    
    # Filtro simple por negocio (simulado)
    negocios_nombres = ["Todos"] + [n["nombre"] for n in NEGOCIOS]
    filtro_negocio = st.selectbox("Filtrar por negocio:", negocios_nombres)
    
    productos_filtrados = PRODUCTOS
    if filtro_negocio != "Todos":
        negocio_id = next(n["id"] for n in NEGOCIOS if n["nombre"] == filtro_negocio)
        productos_filtrados = [p for p in PRODUCTOS if p["negocio_id"] == negocio_id]

    cols = st.columns(2)
    for i, prod in enumerate(productos_filtrados):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="card">
                <img src="{prod['imagen']}" alt="{prod['nombre']}">
                <h4 style="margin-top: 10px; margin-bottom: 5px;">{prod['nombre']}</h4>
                <p class="price">${prod['precio']:,.0f} COP</p>
            </div>
            """, unsafe_allow_html=True)
            if prod["promocion"]:
                st.markdown(f'<span class="promo-badge">{prod["promocion"]}</span>', unsafe_allow_html=True)
            if st.button(f"Agregar al carrito", key=f"add_{prod['id']}"):
                st.success(f"¡{prod['nombre']} agregado! (Simulado)")

elif seccion == "🎉 Promos":
    st.markdown("<h2>🎉 Promociones</h2>", unsafe_allow_html=True)
    st.write("Aprovecha las ofertas de nuestros negocios locales.")
    
    for promo in PROMOCIONES:
        st.markdown(f"""
        <div class="card">
            <img src="{promo['imagen']}" alt="{promo['titulo']}">
            <h4 style="margin-top: 10px; margin-bottom: 5px;">{promo['titulo']}</h4>
            <p style="font-size: 0.9rem; color: #555;">{promo['negocio']}</p>
            <p>{promo['descripcion']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.divider()

# ==============================================================================
# PIE DE PÁGINA (Opcional)
# ==============================================================================
st.markdown("""
<hr>
<p style="text-align: center; font-size: 0.8rem; color: #888;">
    Hecho con ❤️ para Santander de Quilichao. <br>
    Compro Local - SQ © 2025
</p>
""", unsafe_allow_html=True)

# Nota: La navegación con st.session_state.seccion en los botones es una simulación.
# Para una navegación real entre páginas, en la Fase 2 migraremos a st.navigation o multipage.
