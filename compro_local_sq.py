import streamlit as st

# ==============================================================================
# CONFIGURACIÓN DE PÁGINA
# ==============================================================================
st.set_page_config(
    page_title="Compro Local - SQ",
    page_icon="🏪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# ESTILOS CSS - LOOK APP NATIVA (CON CORRECCIÓN DE COLORES)
# ==============================================================================
def local_css():
    st.markdown("""
    <style>
        /* 1. Fuente Moderna */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        html, body, [class*="css"] { font-family: 'Outfit', sans-serif !important; }
        
        /* 2. Fondo general y FORZAR COLOR DE TEXTO OSCURO */
        .stApp { background-color: #F2F4F7; color: #2D3142 !important; }
        .block-container {
            max-width: 650px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        /* Forzar color de texto oscuro en párrafos, listas y markdown */
        div[data-testid="stMarkdownContainer"] p, 
        div[data-testid="stMarkdownContainer"] span, 
        div[data-testid="stMarkdownContainer"] h1, 
        div[data-testid="stMarkdownContainer"] h2, 
        div[data-testid="stMarkdownContainer"] h3,
        div[data-testid="stMarkdownContainer"] h4,
        p, span {
            color: #2D3142 !important;
        }

        /* 3. Ocultar menús de Streamlit */
        header {visibility: hidden;} footer {visibility: hidden;} #MainMenu {visibility: hidden;}

        /* 4. Títulos */
        h1 { color: #FF6B35 !important; text-align: center; font-weight: 800; font-size: 2.5rem !important; letter-spacing: -1px; margin-bottom: 0; }
        h2, h3 { color: #2D3142 !important; font-weight: 700; }

        /* 5. MENÚ DE NAVEGACIÓN (Píldoras) */
        div[data-testid="stRadio"] div[role="radiogroup"] label > div:first-child { display: none !important; }
        
        div[data-testid="stRadio"] div[role="radiogroup"] label {
            background-color: #FFFFFF; border-radius: 30px; padding: 10px 20px;
            margin-right: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.06);
            transition: all 0.3s ease; border: 2px solid transparent; cursor: pointer;
        }
        
        /* Texto de las píldoras inactivas */
        div[data-testid="stRadio"] div[role="radiogroup"] label div[data-testid="stMarkdownContainer"] p {
            color: #555555 !important; font-weight: 600 !important; font-size: 15px !important;
        }

        /* Píldora Seleccionada (Activa) - Forzar texto blanco */
        div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
            background-color: #FF6B35; border-color: #FF6B35;
            box-shadow: 0 6px 15px rgba(255, 107, 53, 0.35);
        }
        div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] div[data-testid="stMarkdownContainer"] p {
            color: #FFFFFF !important; font-weight: 800 !important;
        }

        /* 6. Tarjetas */
        .card {
            background-color: #FFFFFF; border-radius: 24px; padding: 0; overflow: hidden;
            box-shadow: 0 8px 20px rgba(0,0,0,0.04); margin-bottom: 20px;
            border: 1px solid #F0F0F0; transition: transform 0.2s ease;
        }
        .card:hover { transform: scale(1.01); }
        .card img { width: 100%; height: 180px; object-fit: cover; }
        .card-body { padding: 18px; }
        
        /* 7. Botones con Degradado - Forzar texto blanco */
        .stButton > button {
            background: linear-gradient(135deg, #FF6B35 0%, #EF476F 100%) !important;
            color: white !important; border-radius: 14px !important; border: none !important;
            padding: 12px 20px !important; font-weight: 700 !important; width: 100%;
            transition: all 0.3s !important; box-shadow: 0 4px 12px rgba(239, 71, 111, 0.25) !important;
        }
        .stButton > button:hover {
            transform: translateY(-2px) !important; box-shadow: 0 8px 20px rgba(239, 71, 111, 0.4) !important;
        }
        /* Asegurar que el texto de los botones sea blanco */
        .stButton > button p { color: #FFFFFF !important; font-weight: 700 !important; }

        /* 8. Etiquetas */
        .promo-badge { background-color: #EF476F; color: white !important; padding: 5px 12px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
        .price { color: #06D6A0 !important; font-size: 1.4rem; font-weight: 800; margin: 4px 0; }

        /* 9. Cajas de selección (Selectbox) */
        div[data-baseweb="select"] > div {
            background-color: #FFFFFF !important; border-radius: 12px !important; color: #2D3142 !important;
        }
        div[data-baseweb="select"] * { color: #2D3142 !important; }
    </style>
    """, unsafe_allow_html=True)

local_css()

# ==============================================================================
# DATOS SIMULADOS (Lógica 100% intacta)
# ==============================================================================
NEGOCIOS = [
    {"id": 1, "nombre": "Panadería La Espiga", "categoria": "Comida", "descripcion": "Pan fresco y tradicional horneado a leña.", "imagen": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400&h=300&fit=crop", "destacado": True},
    {"id": 2, "nombre": "Café Quilichao", "categoria": "Café", "descripcion": "Café de origen local, cultivado en las montañas.", "imagen": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=400&h=300&fit=crop", "destacado": True},
    {"id": 3, "nombre": "Artesanías del Valle", "categoria": "Artesanías", "descripcion": "Tejidos y cerámicas hechas por artesanos locales.", "imagen": "https://images.unsplash.com/photo-1610701596007-11502861dcfa?w=400&h=300&fit=crop", "destacado": False},
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
# BARRA DE NAVEGACIÓN
# ==============================================================================
seccion = st.radio(
    "Navegación",
    ["🏠 Inicio", "🏪 Negocios", "🛒 Productos", "🎉 Promos"],
    horizontal=True,
    label_visibility="collapsed"
)

st.write("") # Espacio

# ==============================================================================
# CONTENIDO
# ==============================================================================
if seccion == "🏠 Inicio":
    st.markdown("<h1>Compro Local - SQ</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.1rem; margin-bottom: 25px;'>Apoya lo nuestro. Compra en Santander de Quilichao.</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&h=300&fit=crop", use_container_width=True, caption="Lo mejor de nuestra tierra, a un clic.")
    
    st.subheader("⭐ Destacados de la Semana")
    cols = st.columns(2)
    for i, negocio in enumerate([n for n in NEGOCIOS if n["destacado"]]):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="card">
                <img src="{negocio['imagen']}" alt="{negocio['nombre']}">
                <div class="card-body">
                    <span class="promo-badge">Recomendado</span>
                    <h4 style="margin-top: 10px; margin-bottom: 5px; color: #2D3142;">{negocio['nombre']}</h4>
                    <p style="font-size: 0.9rem; margin-bottom: 0;">{negocio['descripcion']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Ver {negocio['nombre']}", key=f"btn_dest_{negocio['id']}"):
                st.session_state.seccion = "🏪 Negocios"
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
                <div class="card-body">
                    <h4 style="margin-top: 0; margin-bottom: 4px; color: #2D3142;">{prod['nombre']}</h4>
                    <p class="price">${prod['precio']:,.0f} COP</p>
                </div>
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
            <div class="card-body">
                <h4 style="margin-top: 0; margin-bottom: 5px; color: #2D3142;">{promo['titulo']}</h4>
                <p style="font-size: 0.9rem; color: #FF6B35 !important; font-weight: 600;">{promo['negocio']}</p>
                <p style="color: #555555;">{promo['descripcion']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.divider()

st.markdown("<hr><p style='text-align: center; font-size: 0.8rem; color: #888;'>Hecho con ❤️ para Santander de Quilichao. <br> Compro Local - SQ © 2025</p>", unsafe_allow_html=True)
