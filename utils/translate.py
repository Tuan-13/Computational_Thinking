# utils.py
import streamlit as st
from deep_translator import GoogleTranslator
from config.config import BASE_TEXTS

# --- DỊCH THUẬT CƠ BẢN ---
@st.cache_resource
def get_translator():
    return GoogleTranslator(source='vi', target='en')

def translate_text(text, target_lang, source_lang='vi'):
    if target_lang == source_lang or not text: return text
    # Map code ngôn ngữ cho đúng chuẩn Google Translate
    target_lang_api = 'zh-CN' if target_lang == 'zh' else target_lang
    try:
        return GoogleTranslator(source=source_lang, target=target_lang_api).translate(text)
    except Exception:
        return text

def get_text(key, lang="vi"):
    # Cache đơn giản để không dịch đi dịch lại các nhãn tĩnh
    if "translations_cache" not in st.session_state: 
        st.session_state.translations_cache = {}
        
    cache_key = f"{key}_{lang}"
    if cache_key in st.session_state.translations_cache: 
        return st.session_state.translations_cache[cache_key]
    
    base_text = BASE_TEXTS.get(key, key)
    
    # Chỉ dịch nếu ngôn ngữ khác Tiếng Việt
    translated = base_text if lang == "vi" else translate_text(base_text, lang, 'vi')
    
    st.session_state.translations_cache[cache_key] = translated
    return translated