# views/map_view.py
import streamlit as st
from utils.translate import get_text
from services.osm_service import geocode, get_restaurants_from_osm
from services.search_engine import is_known_food_term
from views.map_components import render_settings, render_results_list, render_map, render_home_page
from views.map_logic import process_results

def render_map_tab(lang):
    # --- GIAO DIỆN TÌM KIẾM ---
    st.markdown(f"""
    <div style="
        text-align: center;
        margin-bottom: 1rem;
    ">
        <div style="
            font-size: 1rem;
            color: #64748b;
            font-weight: 500;
        ">{get_text("header_question", lang)}</div>
    </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):
        c1, c2 = st.columns([3, 1])
        with c1:
            dish_input = st.text_input(
                get_text("what_to_eat", lang),
                value="",
                placeholder="🔍 Bánh mì, Phở, Cơm tấm, Pizza...",
                label_visibility="collapsed",
                key="search_input_field"
            )
            if dish_input: st.session_state.dish_input = dish_input

        with c2:
            search_btn = st.button(
                f"{get_text('search_button', lang)}",
                type="primary",
                use_container_width=True
            )

    settings = render_settings(lang)

    # --- XỬ LÝ TÌM KIẾM ---
    if search_btn:
        st.session_state.selected_place_id = None
        center_lat, center_lon = None, None
        
        if settings['use_location'] and settings['user_lat']:
            center_lat, center_lon = settings['user_lat'], settings['user_lon']
        elif not settings['use_location']:
            geo = geocode(settings['city_input'])
            if geo:
                center_lat, center_lon = geo['lat'], geo['lon']
        
        st.session_state.center_coords = (center_lat, center_lon)

        if center_lat and dish_input:
            with st.spinner(get_text("searching", lang).format(dish_input)):
                raw_results = get_restaurants_from_osm(center_lat, center_lon, settings['radius'], dish_input)
                
                # Gọi hàm process_results từ map_logic.py
                st.session_state.search_results = process_results(
                    raw_results, center_lat, center_lon, settings['budget'], lang
                )
            
            if not st.session_state.search_results:
                # Kiểm tra xem từ khóa có phải là món ăn đã biết không
                if is_known_food_term(dish_input):
                    msg = get_text("error_no_food_nearby", lang).format(dish_input)
                    st.error(f"❌ {msg}")
                    st.info(get_text("try_increasing_radius", lang))
                else:
                    msg = get_text("error_invalid_query", lang).format(dish_input)
                    st.warning(f"🤔 {msg}")

        elif not dish_input:
            st.warning("Vui lòng nhập món ăn bạn muốn tìm!")

    # --- HIỂN THỊ KẾT QUẢ ---
    if st.session_state.get("center_coords") and st.session_state.get("search_results"):
        results = st.session_state.search_results
        slat, slon = st.session_state.center_coords

        col_map, col_list = st.columns([2, 1])

        with col_list:
            render_results_list(results, settings['mode'])

        with col_map:
            render_map(slat, slon, results, settings['mode'])
    else:
        # --- TRANG CHỦ KHI CHƯA TÌM KIẾM ---
        render_home_page()