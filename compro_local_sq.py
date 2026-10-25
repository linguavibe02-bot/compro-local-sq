import streamlit as st
import base64

# 1. Configuración de página (Mobile First)
st.set_page_config(page_title="Compro Local SQ", page_icon="🛍️", layout="centered")

# 2. CSS de App Nativa (Modo Oscuro + Naranja Vibrante)
st.markdown("""
<style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stApp { background-color: #121212; }
    .block-container { padding-top: 2rem; padding-bottom: 5rem; max-width: 600px; }
    
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }

    /* Tarjetas de Negocios/Productos */
    .card {
        background-color: #1E1E1E; border-radius: 20px; padding: 15px;
        border: 1px solid #333; margin-bottom: 15px; transition: transform 0.2s;
    }
    .card:hover { transform: scale(1.02); border-color: #FF6B35; }
    .card img { border-radius: 15px; width: 100%; height: 150px; object-fit: cover; }
    .promo-badge { background-color: #FF6B35; color: white; padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; }
    .price { color: #4ADE80; font-size: 18px; font-weight: 800; }
    .title { text-align: center; color: white; font-size: 28px; font-weight: 800; margin-bottom: 5px; }
    .subtitle { text-align: center; color: #888; font-size: 14px; margin-bottom: 25px; }

    /* Botones de Navegación Inferior */
    div.stButton > button {
        background-color: #1E1E1E; color: #888; border: none; border-radius: 15px;
        padding: 10px; width: 100%; font-weight: 600; transition: all 0.3s;
    }
    div.stButton > button:hover { color: white; }
    div.stButton > button[kind="primary"] { background-color: #FF6B35; color: white; box-shadow: 0 0 15px rgba(255, 107, 53, 0.4); }
</style>
""", unsafe_allow_html=True)

# 3. Estado de navegación
if "page" not in st.session_state:
    st.session_state.page = "inicio"

# 4. Contenido Dinámico
if st.session_state.page == "inicio":
    st.markdown("<p class='title'>Compro Local SQ</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Apoya lo nuestro. Compra en Quilichao.</p>", unsafe_allow_html=True)
    
    # Ejemplo de tarjeta
    st.markdown("""
    <div class="card">
        <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=600&h=300&fit=crop">
        <div style="margin-top: 15px;">
            <span class="promo-badge">Recomendado</span>
            <h3 style="color: white; margin: 5px 0;">Panadería La Espiga</h3>
            <p style="color: #aaa; font-size: 13px;">Pan fresco horneado a leña.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "negocios":
    st.markdown("<p class='title'>Negocios</p>", unsafe_allow_html=True)
    st.info("Aquí va la lista de negocios...")

elif st.session_state.page == "promos":
    st.markdown("<p class='title'>Promociones</p>", unsafe_allow_html=True)
    st.info("Aquí van las ofertas...")

# 5. Barra de Navegación Inferior (Simulada)
st.markdown("<br><br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Inicio", use_container_width=True, type="primary" if st.session_state.page=="inicio" else "secondary"):
        st.session_state.page = "inicio"; st.rerun()
with col2:
    if st.button("🏪 Locales", use_container_width=True, type="primary" if st.session_state.page=="negocios" else "secondary"):
        st.session_state.page = "negocios"; st.rerun()
with col3:
    if st.button("🎉 Promos", use_container_width=True, type="primary" if st.session_state.page=="promos" else "secondary"):
        st.session_state.page = "promos"; st.rerun()
