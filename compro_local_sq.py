import streamlit as st

# 1. Configuración de página (Mobile First)
st.set_page_config(
    page_title="Compro Local - SQ",
    page_icon="🛍️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Estilos CSS (Manteniendo tu paleta cálida, pero con look de App)
st.markdown("""
<style>
    /* Ocultar menús de Streamlit */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    
    /* Fondo cálido y contenedor centrado para celular */
    .stApp { background-color: #FFF8F0; }
    .block-container { padding-top: 2rem; padding-bottom: 6rem; max-width: 600px; }
    
    /* Fuentes */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
    
    /* Título principal */
    .title { text-align: center; color: #FF6B35; font-size: 32px; font-weight: 800; margin-bottom: 0px; }
    .subtitle { text-align: center; color: #666; font-size: 15px; margin-bottom: 25px; }
    
    /* Tarjetas Premium */
    .card {
        background-color: #FFFFFF; border-radius: 20px; padding: 15px;
        box-shadow: 0 8px 16px rgba(255, 107, 53, 0.08);
        margin-bottom: 15px; border: 2px solid #FFF;
        transition: transform 0.2s, border-color 0.2s;
    }
    .card:hover { transform: translateY(-3px); border-color: #FF6B35; }
    .card img { border-radius: 15px; width: 100%; height: 160px; object-fit: cover; }
    
    .promo-badge { 
        background-color: #EF476F; color: white; padding: 4px 12px; 
        border-radius: 20px; font-size: 11px; font-weight: 600; display: inline-block;
    }
    .price { color: #06D6A0; font-size: 20px; font-weight: 800; }
    
    /* Botones normales */
    div.stButton > button {
        background-color: #FFFFFF; color: #FF6B35; border: 2px solid #FF6B35;
        border-radius: 15px; padding: 10px; width: 100%; font-weight: 800;
        transition: all 0.2s;
    }
    div.stButton > button:hover { background-color: #FF6B35; color: white; }
    
    /* Botón activo de la barra inferior */
    div.stButton > button[kind="primary"] { 
        background-color: #FF6B35; color: white; border: none; 
        box-shadow: 0 4px 10px rgba(255, 107, 53, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# 3. Datos Simulados (Recuperados de la versión original)
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

# 4. Control de Navegación
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

# 5. Renderizado de Páginas
if st.session_state.pagina == "inicio":
    st.markdown("<p class='title'>Compro Local - SQ</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Apoya lo nuestro. Compra en Quilichao.</p>", unsafe_allow_html=True)
    
    st.markdown("### ⭐ Destacados de la Semana")
    for negocio in [n for n in NEGOCIOS if n["destacado"]]:
        st.markdown(f"""
        <div class="card">
            <img src="{negocio['imagen']}">
            <div style="padding-top: 10px;">
                <span class="promo-badge">Recomendado</span>
                <h3 style="margin: 8px 0 4px 0;">{negocio['nombre']}</h3>
                <p style="color: #666; font-size: 14px; margin-bottom: 0;">{negocio['descripcion']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.pagina == "negocios":
    st.markdown("<p class='title'>Negocios Locales</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Descubre los emprendimientos de la región.</p>", unsafe_allow_html=True)
    
    for negocio in NEGOCIOS:
        st.markdown(f"""
        <div class="card">
            <img src="{negocio['imagen']}">
            <div style="padding-top: 10px;">
                <span class="promo-badge" style="background-color: #F7C59F; color: #333;">{negocio['categoria']}</span>
                <h3 style="margin: 8px 0 4px 0;">{negocio['nombre']}</h3>
                <p style="color: #666; font-size: 14px;">{negocio['descripcion']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.pagina == "productos":
    st.markdown("<p class='title'>Productos</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Pide directamente y apoya al productor local.</p>", unsafe_allow_html=True)
    
    for prod in PRODUCTOS:
        st.markdown(f"""
        <div class="card">
            <img src="{prod['imagen']}">
            <div style="padding-top: 10px;">
                <h3 style="margin: 0 0 4px 0;">{prod['nombre']}</h3>
                <p class="price">${prod['precio']:,.0f} COP</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"🛒 Agregar {prod['nombre']}", key=f"add_{prod['id']}"):
            st.success("¡Agregado al carrito! (Simulado)")

elif st.session_state.pagina == "promos":
    st.markdown("<p class='title'>Promociones</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Aprovecha las ofertas de nuestros negocios.</p>", unsafe_allow_html=True)
    
    for promo in PROMOCIONES:
        st.markdown(f"""
        <div class="card">
            <img src="{promo['imagen']}">
            <div style="padding-top: 10px;">
                <h3 style="margin: 0 0 4px 0;">{promo['titulo']}</h3>
                <p style="color: #FF6B35; font-weight: bold; font-size: 14px;">{promo['negocio']}</p>
                <p style="color: #666; font-size: 14px;">{promo['descripcion']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 6. Barra de Navegación Inferior (Fija)
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Inicio", use_container_width=True, type="primary" if st.session_state.pagina=="inicio" else "secondary"):
        st.session_state.pagina = "inicio"; st.rerun()
with col2:
    if st.button("🏪 Locales", use_container_width=True, type="primary" if st.session_state.pagina=="negocios" else "secondary"):
        st.session_state.pagina = "negocios"; st.rerun()
with col3:
    if st.button("🛒 Tienda", use_container_width=True, type="primary" if st.session_state.pagina=="productos" else "secondary"):
        st.session_state.pagina = "productos"; st.rerun()
with col4:
    if st.button("🎉 Promos", use_container_width=True, type="primary" if st.session_state.pagina=="promos" else "secondary"):
        st.session_state.pagina = "promos"; st.rerun()
