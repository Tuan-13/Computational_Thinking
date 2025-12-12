# main.py
import streamlit as st
from utils.translate import get_text
from views.map_view import render_map_tab
from views.chatbot_view import render_chatbot_tab
from config.styles import load_css

st.set_page_config(page_title="Smart Restaurant Finder", layout="wide")

# --- SESSION STATE INIT ---
if "search_results" not in st.session_state: st.session_state.search_results = []
if "center_coords" not in st.session_state: st.session_state.center_coords = None
if "selected_place_id" not in st.session_state: st.session_state.selected_place_id = None
if "language" not in st.session_state: st.session_state.language = "vi"
if "dark_mode" not in st.session_state: st.session_state.dark_mode = False


load_css()

# --- SIDEBAR ---
with st.sidebar:
    # Logo và branding
    is_dark_sidebar = st.session_state.get("dark_mode", False)
    subtitle_color = "#64748b" if not is_dark_sidebar else "#94a3b8"

    st.markdown(f"""
    <div style="text-align: center; padding: 1rem 0 1.5rem 0;">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">🍜</div>
        <div style="
            font-family: 'Poppins', sans-serif;
            font-size: 1.1rem;
            font-weight: 600;
            background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        ">Smart Restaurant</div>
        <div style="font-size: 0.75rem; color: {subtitle_color}; margin-top: 0.25rem;">Find your perfect meal</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Dark mode toggle
    is_dark = st.session_state.dark_mode
    theme_icon = "🌙" if not is_dark else "☀️"
    theme_label = "Dark Mode" if not is_dark else "Light Mode"

    col_theme1, col_theme2 = st.columns([3, 1])
    with col_theme1:
        st.markdown(f"""
        <div style="
            font-size: 0.75rem;
            font-weight: 600;
            color: {'#1e293b' if is_dark else '#64748b'};
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.25rem;
        ">{theme_icon} Theme</div>
        """, unsafe_allow_html=True)
    with col_theme2:
        if st.button("🔄", key="theme_toggle", help=f"Switch to {theme_label}"):
            st.session_state.dark_mode = not st.session_state.dark_mode
            st.rerun()

    st.divider()

    # Language selector 
    st.markdown(f"""
    <div style="
        font-size: 0.75rem;
        font-weight: 600;
        color: {'#1e293b' if is_dark else '#64748b'};
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    ">🌐 Language / Ngôn ngữ</div>
    """, unsafe_allow_html=True)

    language_options = {
        "vi": "🇻🇳 Tiếng Việt",
        "en": "🇬🇧 English",
        "zh": "🇨🇳 中文",
        "ko": "🇰🇷 한국어",
        "ja": "🇯🇵 日本語",
        "fr": "🇫🇷 Français",
        "es": "🇪🇸 Español",
        "th": "🇹🇭 ไทย",
        "ar": "🇸🇦 العربية",
        "pt": "🇧🇷 Português (BR)"
    }

    selected_lang = st.selectbox(
        get_text("language", st.session_state.language),
        options=list(language_options.keys()),
        format_func=lambda x: language_options[x],
        index=list(language_options.keys()).index(st.session_state.language),
        label_visibility="collapsed"
    )

    st.divider()

    # Footer info
    footer_color = "#64748b" if not is_dark else "#1e293b"
    st.markdown(f"""
    <div style="
        position: fixed;
        bottom: 1rem;
        font-size: 0.7rem;
        color: {footer_color};
        text-align: center;
        width: calc(100% - 2rem);
    ">
        <div style="margin-bottom: 0.25rem;">Made with ❤️</div>
        <div>Powered by OpenStreetMap & AI</div>
    </div>
    """, unsafe_allow_html=True)
    
    if selected_lang != st.session_state.language:
        st.session_state.language = selected_lang
        st.rerun()

lang = st.session_state.language

if selected_lang != st.session_state.language:
    st.session_state.language = selected_lang
    
    if "translations_cache" in st.session_state:
        del st.session_state.translations_cache
        
    st.rerun()

# --- MAIN INTERFACE ---
is_dark_main = st.session_state.get("dark_mode", False)
title_bg = "rgba(30, 41, 59, 0.85)" if is_dark_main else "rgba(255, 255, 255, 0.8)"
title_border = "rgba(51, 65, 85, 0.5)" if is_dark_main else "rgba(255, 255, 255, 0.5)"

st.markdown(f'''
<div style="
    background: {title_bg};
    backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 1rem 2rem;
    margin-bottom: 1rem;
    text-align: center;
    border: 1px solid {title_border};
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
">
    <h1 style="
        background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Poppins', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        padding: 0;
    ">{get_text("app_title", lang)}</h1>
</div>
''', unsafe_allow_html=True)

tab_map, tab_chat = st.tabs([
    "🗺️ " + get_text("map_tab", lang),
    "🤖 " + get_text("chatbot_tab", lang)
])

with tab_map:
    render_map_tab(lang)

with tab_chat:
    render_chatbot_tab(lang)