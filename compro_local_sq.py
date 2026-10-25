import streamlit as st

st.set_page_config(page_title="Compro Local - SQ", page_icon="🏪", layout="wide", initial_sidebar_state="collapsed")

# Solo CSS (Nada de lógica tocada)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
    .stApp { background-color: #FFF8F0; }
    header {visibility: hidden;} footer {visibility: hidden;} #MainMenu {visibility: hidden;}
    h1 { color: #FF6B35; font-weight: 800; text-align: center; }
    h2, h3 { color: #2D3142; font-weight: 700; }
    .card { background-color: white; border-radius: 16px; padding: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 15px; border: 1px solid #EAEAEA; }
    .card img { border-radius: 12px; width: 100%; height: 160px; object-fit: cover; }
    .stButton > button { background-color: #FF6B35; color: white; border-radius: 12px; font-weight: 600; border: none; width: 100%; }
    .stButton > button:hover { background-color: #EF476F; color: white; }
    .promo-badge { background-color: #EF476F; color: white; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; display: inline-block; }
    .price { color: #06D6A0; font-size: 1.3rem; font-weight: 800; }
</style>
""", unsafe_allow_html=True)

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
]
PROMOCIONES = [
    {"id": 1, "titulo": "Martes de Pan de Bono", "negocio": "Panadería La Espiga", "descripcion": "Lleva 6 panes y paga 3.", "imagen": "https://images.unsplash.com/photo-1598373182133-52452f7691ef?w=400&h=300&fit=crop"},
]

seccion = st.radio("Navegación", ["🏠 Inicio", "🏪 Negocios", "🛒 Productos", "🎉 Promos"], horizontal=True, label_visibility="collapsed")

if seccion == "🏠 Inicio":
    st.markdown("<h1>Compro Local - SQ</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666; font-size: 1.1rem;'>Apoya lo nuestro. Compra en Santander de Quilichao.</p>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&h=300&fit=crop", use_container_width=True)
    st.subheader("⭐ Destacados de la Semana")
    cols = st.columns(2)
    for i, negocio in enumerate([n for n in NEGOCIOS if n["destacado"]]):
        with cols[i % 2]:
            st.markdown(f'<div class="card"><img src="{negocio["imagen"]}"><h4>{negocio["nombre"]}</h4><p>{negocio["descripcion"]}</p><span class="promo-badge">Recomendado</span></div>', unsafe_allow_html=True)

elif seccion == "🏪 Negocios":
    st.markdown("<h2>🏪 Negocios Locales</h2>", unsafe_allow_html=True)
    for negocio in NEGOCIOS:
        st.markdown(f'<div class="card"><img src="{negocio["imagen"]}"><h4>{negocio["nombre"]}</h4><p>{negocio["descripcion"]}</p></div>', unsafe_allow_html=True)

elif seccion == "🛒 Productos":
    st.markdown("<h2>🛒 Productos</h2>", unsafe_allow_html=True)
    cols = st.columns(2)
    for i, prod in enumerate(PRODUCTOS):
        with cols[i % 2]:
            st.markdown(f'<div class="card"><img src="{prod["imagen"]}"><h4>{prod["nombre"]}</h4><p class="price">${prod["precio"]:,.0f} COP</p></div>', unsafe_allow_html=True)
            if st.button(f"Agregar {prod['nombre']}", key=f"add_{prod['id']}"): st.success("Agregado (Simulado)")

elif seccion == "🎉 Promos":
    st.markdown("<h2>🎉 Promociones</h2>", unsafe_allow_html=True)
    for promo in PROMOCIONES:
        st.markdown(f'<div class="card"><img src="{promo["imagen"]}"><h4>{promo["titulo"]}</h4><p>{promo["descripcion"]}</p></div>', unsafe_allow_html=True)
