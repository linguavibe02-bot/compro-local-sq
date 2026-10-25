import streamlit as st

# ==============================================================================
# CONFIGURACIÓN DE PÁGINA
# ==============================================================================
st.set_page_config(
    page_title="Compro Local - SQ",
    page_icon="🏪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# ESTILOS CSS MEJORADOS (Solo cambiamos esto)
# ==============================================================================
def local_css():
    st.markdown("""
    <style>
        /* Fuente moderna de Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        
        html, body, [class*="css"] { font-family: 'Outfit', sans-serif !important; }
        
        :root {
            --primary: #FF6B35;
            --accent: #EF476F;
            --bg: #FFF8F0;
            --text: #2D3142;
            --success: #06D6A0;
        }
        
        .stApp { background-color: var(--bg); color: var(--text); }
        header {visibility: hidden;} footer {visibility: hidden;} #MainMenu {visibility: hidden;}
        
        /* Títulos */
        h1 { color: var(--primary); text-align: center; font-weight: 800; font-size: 2.8rem !important; margin-bottom: 0rem; letter-spacing: -1px; }
        h2, h3 { color: var(--text); font-weight: 700; }

        /* Navegación estilo Píldora (Para el st.radio) */
        div[role="radiogroup"] {
            display: flex; justify-content: center; gap: 10px; margin-bottom: 25px; flex-wrap: wrap;
        }
        div[role="radiogroup"] > label {
            background-color: white; padding: 10px 25px; border-radius: 30px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #EAEAEA;
            transition: all 0.3s; cursor: pointer;
        }
        div[role="radiogroup"] > label:hover { transform: translateY(-2px); border-color: var(--primary); }
        
        /* Tarjetas (Cards) */
        .card {
            background-color: white; border-radius: 20px; padding: 0; overflow: hidden;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05); margin-bottom: 20px;
            border: 1px solid #FFF; transition: transform 0.3s, box-shadow 0.3s;
        }
        .card:hover { transform: translateY(-5px); box-shadow: 0 15px 35px rgba(255, 107, 53, 0.15); }
        .card img { width: 100%; height: 180px; object-fit: cover; border-radius: 20px 20px 0 0; }
        .card-body { padding: 20px; }
        
        /* Botones */
        .stButton > button {
            background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
            color: white; border-radius: 15px; padding: 12px 25px; font-weight: 700;
            border: none; width: 100%; transition: all 0.3s; box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
        }
        .stButton > button:hover { transform: scale(1.02); box-shadow: 0 6px 20px rgba(255, 107, 53, 0.5); color: white; }
        
        /* Etiquetas y Precios */
        .promo-badge { background-color: var(--accent); color: white; padding: 6px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; display: inline-block; margin-bottom: 8px; }
        .price { color: var(--success); font-size: 1.4rem; font-weight: 800; margin: 5px 0; }
    </style>
    """, unsafe_allow_html=True)

local_css()

# ==============================================================================
# DATOS SIMULADOS (Lógica Original Intacta)
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

# ==============================================================================
# CONTENIDO DE CADA SECCIÓN
# ==============================================================================
if seccion == "🏠 Inicio":
    st.markdown("<h1>Compro Local - SQ</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666; font-size: 1.2rem; margin-bottom: 30px;'>Apoya lo nuestro. Compra en Santander de Quilichao.</p>", unsafe_allow_html=True)
    
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
                    <h4 style="margin-top: 5px; margin-bottom: 5px;">{negocio['nombre']}</h4>
                    <p style="font-size: 0.95rem; color: #555;">{negocio['descripcion']}</p>
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
                    <h4 style="margin-top: 0; margin-bottom: 5px;">{prod['nombre']}</h4>
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
                <h4 style="margin-top: 0; margin-bottom: 5px;">{promo['titulo']}</h4>
                <p style="font-size: 0.9rem; color: var(--primary); font-weight: 600;">{promo['negocio']}</p>
                <p>{promo['descripcion']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.divider()

st.markdown("<hr><p style='text-align: center; font-size: 0.8rem; color: #888;'>Hecho con ❤️ para Santander de Quilichao. <br> Compro Local - SQ © 2025</p>", unsafe_allow_html=True)
