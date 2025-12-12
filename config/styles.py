# styles.py
import streamlit as st
import os
import base64

def get_base64_image(image_path):
    """Đọc ảnh và convert sang base64"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def load_css(file_name="style.css"):
    """
    Hàm đọc file CSS và inject vào Streamlit.
    Đồng thời inject background image dưới dạng base64.
    Hỗ trợ dark mode thông qua session state.
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up to project root
    assets_dir = os.path.join(base_dir, "assets")
    css_path = os.path.join(assets_dir, file_name)
    bg_path = os.path.join(assets_dir, "background.jpg")

    # Lấy theme từ session state
    is_dark = st.session_state.get("dark_mode", False)
    theme_attr = 'data-theme="dark"' if is_dark else ''

    try:
        # Đọc CSS
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()

        # Đọc và encode background image
        if os.path.exists(bg_path):
            bg_base64 = get_base64_image(bg_path)

            # Inject CSS
            st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

            # Inject background và theme attribute
            if is_dark:
                # Dark mode - darker overlay
                st.markdown(f'''
                <style>
                .stApp {{
                    background-image: linear-gradient(
                        rgba(15, 23, 42, 0.92),
                        rgba(30, 41, 59, 0.95)
                    ), url("data:image/jpeg;base64,{bg_base64}") !important;
                    background-size: cover !important;
                    background-position: center !important;
                    background-repeat: no-repeat !important;
                    background-attachment: fixed !important;
                }}

                /* Dark mode - Sidebar selectbox text */
                section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] span {{
                    color: #1e293b !important;
                }}

                section[data-testid="stSidebar"] .stSelectbox svg {{
                    fill: #1e293b !important;
                }}

                /* Dark mode - Expander header text (Cài đặt) */
                div[data-testid="stExpander"] summary span {{
                    color: #1e293b !important;
                }}

                div[data-testid="stExpander"] summary svg {{
                    fill: #1e293b !important;
                    color: #1e293b !important;
                }}

                /* Dark mode - Chat input - ALL selectors */
                textarea {{
                    color: #ffffff !important;
                    background-color: #1e293b !important;
                }}

                textarea::placeholder {{
                    color: #94a3b8 !important;
                    opacity: 1 !important;
                    -webkit-text-fill-color: #94a3b8 !important;
                }}

                /* Dark mode - Text input */
                input[type="text"] {{
                    color: #ffffff !important;
                    background-color: #1e293b !important;
                }}

                input[type="text"]::placeholder {{
                    color: #94a3b8 !important;
                    opacity: 1 !important;
                    -webkit-text-fill-color: #94a3b8 !important;
                }}
                </style>
                ''', unsafe_allow_html=True)
            else:
                # Light mode
                st.markdown(f'''
                <style>
                .stApp {{
                    background-image: linear-gradient(
                        rgba(255, 255, 255, 0.82),
                        rgba(248, 250, 252, 0.85)
                    ), url("data:image/jpeg;base64,{bg_base64}") !important;
                    background-size: cover !important;
                    background-position: center !important;
                    background-repeat: no-repeat !important;
                    background-attachment: fixed !important;
                }}
                </style>
                ''', unsafe_allow_html=True)
        else:
            st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

        # Inject theme attribute vào html element
        st.markdown(f'''
        <script>
            document.documentElement.setAttribute('data-theme', '{"dark" if is_dark else "light"}');
        </script>
        ''', unsafe_allow_html=True)

    except FileNotFoundError:
        st.error(f"Lỗi: Không tìm thấy file {file_name}. Hãy kiểm tra lại thư mục.")