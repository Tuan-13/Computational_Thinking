# views/map_components.py
import streamlit as st
import folium
from folium import plugins
from streamlit_folium import st_folium
from streamlit_js_eval import get_geolocation
import math

# Import các module nội bộ
from utils.translate import get_text
from services.route_service import get_route
# Import logic từ file mới tách
from views.map_logic import calculate_time_minutes

def render_settings(lang):
    """Hiển thị panel cài đặt"""
    user_lat, user_lon = None, None
    city_input = "Ho Chi Minh City"
    selected_mode_api = "driving"
    selected_budget = None
    radius = 3000
    use_location = True

    with st.expander("⚙️ " + get_text("settings", lang), expanded=False):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            use_location = st.checkbox(get_text("use_current_location", lang), value=True)
            if use_location:
                loc = get_geolocation()
                if loc:
                    user_lat = loc['coords']['latitude']
                    user_lon = loc['coords']['longitude']
                    st.success("GPS OK!")
            else:
                city_input = st.text_input(get_text("enter_location", lang), value="Đại học Khoa học Tự Nhiên")
        
        with col2:
            label_transport = get_text("transport_mode", lang)
            travel_modes = {
                get_text("mode_driving", lang): "driving",
                get_text("mode_walking", lang): "walking",
                get_text("mode_bicycling", lang): "cycling"
            }
            selected_mode_label = st.selectbox(label_transport, list(travel_modes.keys()))
            selected_mode_api = travel_modes[selected_mode_label]

        with col3:
            budget_options = [
                get_text("budget_all", lang),
                get_text("budget_cheap", lang),
                get_text("budget_medium", lang),
                get_text("budget_expensive", lang)
            ]
            selected_budget = st.selectbox(get_text("budget", lang), budget_options)

        with col4:
            radius = st.slider(get_text("radius", lang), 500, 5000, 3000, step=500)
            
    return {
        "user_lat": user_lat, "user_lon": user_lon,
        "use_location": use_location, "city_input": city_input,
        "mode": selected_mode_api, "budget": selected_budget, "radius": radius
    }

def render_results_list(results, mode):
    """Hiển thị danh sách quán ăn bên trái"""
    # Lấy ngôn ngữ và theme hiện tại từ session state
    lang = st.session_state.get("language", "vi")
    is_dark = st.session_state.get("dark_mode", False)

    # Header kết quả với thiết kế mới
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%);
        padding: 1rem 1.25rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(78, 205, 196, 0.3);
    ">
        <div style="
            font-family: 'Poppins', sans-serif;
            font-size: 1.1rem;
            font-weight: 600;
            color: white;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        ">
            <span>📍</span> {get_text('top_results', lang).format(len(results))}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<style>div[data-testid="stVerticalBlock"] > div > div[data-testid="stVerticalBlock"] {gap: 0.5rem;}</style>""", unsafe_allow_html=True)

    center_coords = st.session_state.get("center_coords")

    for idx, r in enumerate(results):
        is_selected = (str(st.session_state.get('selected_place_id')) == str(r['id']))

        # --- LOGIC TÍNH KHOẢNG CÁCH & THỜI GIAN TRONG LIST ---
        if is_selected and center_coords:
            path, real_dist, _, _ = get_route(
                center_coords[0], center_coords[1], r['lat'], r['lon'], mode, lang=lang
            )
            final_dist = real_dist if path else r['distance_sort']
            dist_label = f"{int(final_dist)}m"
        else:
            final_dist = r['distance_sort']
            dist_label = f"~{int(final_dist)}m"

        est_time_min = calculate_time_minutes(final_dist, mode)
        time_display_str = f"{est_time_min} phút"

        # Card styling dựa trên trạng thái và theme
        if is_selected:
            if is_dark:
                card_bg = "linear-gradient(135deg, #064e3b 0%, #065f46 100%)"
                card_border = "2px solid #34d399"
                name_color = "#f1f5f9"
                info_color = "#94a3b8"
            else:
                card_bg = "linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%)"
                card_border = "2px solid #10b981"
                name_color = "#1e293b"
                info_color = "#64748b"
            card_shadow = "0 4px 15px rgba(16, 185, 129, 0.25)"
            number_bg = "#10b981"
        else:
            if is_dark:
                card_bg = "#1e293b"
                card_border = "1px solid #334155"
                name_color = "#f1f5f9"
                info_color = "#94a3b8"
            else:
                card_bg = "white"
                card_border = "1px solid #e2e8f0"
                name_color = "#1e293b"
                info_color = "#64748b"
            card_shadow = "0 2px 8px rgba(0,0,0,0.06)"
            number_bg = "linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%)"

        # Badge colors for dark mode
        if is_dark:
            dist_badge_bg = "linear-gradient(135deg, #1e3a5f 0%, #1e40af 100%)"
            dist_badge_color = "#93c5fd"
            time_badge_bg = "linear-gradient(135deg, #78350f 0%, #92400e 100%)"
            time_badge_color = "#fde68a"
        else:
            dist_badge_bg = "linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%)"
            dist_badge_color = "#1e40af"
            time_badge_bg = "linear-gradient(135deg, #fef3c7 0%, #fde68a 100%)"
            time_badge_color = "#92400e"

        st.markdown(
            f"""
            <div style="
                background: {card_bg};
                padding: 1rem;
                border-radius: 14px;
                border: {card_border};
                margin-bottom: 0.75rem;
                box-shadow: {card_shadow};
                transition: all 0.3s ease;
            ">
                <div style="display: flex; align-items: flex-start; gap: 0.75rem;">
                    <div style="
                        background: {number_bg};
                        color: white;
                        width: 28px;
                        height: 28px;
                        border-radius: 8px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-weight: 700;
                        font-size: 0.85rem;
                        flex-shrink: 0;
                    ">{idx+1}</div>
                    <div style="flex: 1; min-width: 0;">
                        <div style="
                            font-weight: 600;
                            font-size: 1rem;
                            color: {name_color};
                            margin-bottom: 0.35rem;
                            line-height: 1.3;
                        ">{r['name']}</div>
                        <div style="
                            display: flex;
                            align-items: center;
                            gap: 0.75rem;
                            font-size: 0.85rem;
                            color: {info_color};
                            margin-bottom: 0.5rem;
                        ">
                            <span style="display: flex; align-items: center; gap: 0.2rem;">
                                <span style="color: #fbbf24;">★</span> {r['rating']}
                                <span style="color: #94a3b8; font-size: 0.75rem;">({r['reviews']})</span>
                            </span>
                            <span>•</span>
                            <span style="color: {'#34d399' if is_dark else '#10b981'}; font-weight: 500;">{r['price']}</span>
                        </div>
                        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                            <span style="
                                background: {dist_badge_bg};
                                color: {dist_badge_color};
                                padding: 0.25rem 0.6rem;
                                border-radius: 20px;
                                font-size: 0.75rem;
                                font-weight: 600;
                            ">📍 {dist_label}</span>
                            <span style="
                                background: {time_badge_bg};
                                color: {time_badge_color};
                                padding: 0.25rem 0.6rem;
                                border-radius: 20px;
                                font-size: 0.75rem;
                                font-weight: 600;
                            ">⏱️ {time_display_str}</span>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True
        )

        def select_place(pid=r['id']):
            st.session_state.selected_place_id = str(pid)

        btn_label = get_text("go_to_place_btn", lang).format(idx+1)
        st.button(btn_label, key=f"btn_{r['id']}", on_click=select_place, use_container_width=True)

def render_map(center_lat, center_lon, results, mode):
    """Hiển thị bản đồ Folium và đường đi thực tế"""
    # Lấy ngôn ngữ
    lang = st.session_state.get("language", "vi")

    m = folium.Map(location=[center_lat, center_lon], zoom_start=15)
    folium.Marker([center_lat, center_lon], icon=folium.Icon(color='red', icon='user', prefix='fa'), popup=get_text("you", lang)).add_to(m)
    
    selected_place = next((x for x in results if str(x['id']) == str(st.session_state.get('selected_place_id'))), None)
    
    for r in results:
        is_selected = (selected_place and str(r['id']) == str(selected_place['id']))
        color = 'green' if is_selected else 'blue'
        
        popup_html = f"""
        <div style="font-family: sans-serif; width: 200px;">
            <h4 style="margin: 0 0 5px 0;">{r['name']}</h4>
            <p style="margin: 0; font-size: 0.9em;">⭐ {r['rating']} | 💬 {r['reviews']}</p>
            <p style="margin: 0; font-size: 0.9em; color: #666;">{r['address']}</p>
        </div>
        """
        marker = folium.Marker(
            [r['lat'], r['lon']],
            tooltip=f"{r['name']}",
            popup=folium.Popup(popup_html, max_width=250),
            icon=folium.Icon(color=color, icon='cutlery', prefix='fa')
        )
        marker.add_to(m)
    
    steps_to_display = []
    display_dist_m = 0
    display_time_min = 0
        
    if selected_place:
        # Gọi API lấy đường đi thực tế
        path, real_dist, real_dur_api, steps = get_route(
            center_lat, center_lon, selected_place['lat'], selected_place['lon'], 
            mode=mode, lang=lang
        )
        
        if path:
            if mode == "driving": route_color = "#3388ff" 
            elif mode == "walking": route_color = "#4CAF50" 
            else: route_color = "#eb1509" 

            plugins.AntPath(
                locations=path, dash_array=[10, 20], delay=1000, color=route_color,
                pulse_color='#FFFFFF', weight=6, opacity=0.8
            ).add_to(m)
            
            steps_to_display = steps
            display_dist_m = real_dist 
            display_time_min = calculate_time_minutes(display_dist_m, mode)
            
        else:
            display_dist_m = selected_place['distance_sort']
            display_time_min = calculate_time_minutes(display_dist_m, mode)

        # If we have a route but it's approximate (fallback), show a notice
        if steps_to_display and isinstance(steps_to_display, list) and steps_to_display[0].get('approximate'):
            st.info(get_text('real_route_unavailable', lang))
    
    st_folium(m, width="100%", height=600)
    
    # === HIỂN THỊ CHI TIẾT LỘ TRÌNH ===
    if steps_to_display:
        st.markdown(f"### {get_text('real_route_title', lang)}")
        
        c1, c2 = st.columns(2)
        dist_str = f"{display_dist_m/1000:.1f} km" if display_dist_m > 1000 else f"{int(display_dist_m)} m"
        
        c1.metric(get_text("actual_dist", lang), dist_str)
        c2.metric(get_text("est_time", lang), f"{display_time_min} min")
        
        st.divider()
        
        with st.container(height=400):
            for i, step in enumerate(steps_to_display):
                dist_m = int(step['distance'])
                icon = step.get('icon', '⏺️')
                instruction = step['instruction'] 
                
                if dist_m == 0 and i < len(steps_to_display) - 1:
                    continue

                col_icon, col_text, col_dist = st.columns([1, 8, 2])
                with col_icon:
                    st.markdown(f"<div style='font-size: 1.5em; text-align: center;'>{icon}</div>", unsafe_allow_html=True)
                with col_text:
                    st.markdown(f"**{instruction}**")
                    if dist_m > 0: 
                        caption_text = get_text("step_continue_dist", lang).format(dist_m)
                        st.caption(caption_text)
                with col_dist:
                    step_min = math.ceil(step['duration'] / 60)
                    if step_min > 0:
                        st.markdown(f"<div style='text-align: right; color: gray; font-size: 0.8em;'>{step_min} min</div>", unsafe_allow_html=True)
                
                st.markdown("<hr style='margin: 5px 0; border-top: 1px dashed #eee;'>", unsafe_allow_html=True)


def render_home_page():
    """Hiển thị trang chủ khi chưa tìm kiếm - compact version"""
    # Lấy trạng thái dark mode
    is_dark = st.session_state.get("dark_mode", False)
    lang = st.session_state.get("language", "vi")

    # Card style chung - glassmorphism với dark mode support
    if is_dark:
        card_style = """
            text-align: center;
            padding: 1rem 0.75rem;
            background: rgba(30, 41, 59, 0.85);
            backdrop-filter: blur(10px);
            border-radius: 14px;
            border: 1px solid rgba(51, 65, 85, 0.5);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        """
        title_color = "#f1f5f9"
        subtitle_color = "#94a3b8"
        suggestion_bg = "rgba(30, 41, 59, 0.85)"
        suggestion_border = "rgba(51, 65, 85, 0.5)"
        suggestion_text_color = "#cbd5e1"
    else:
        card_style = """
            text-align: center;
            padding: 1rem 0.75rem;
            background: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(10px);
            border-radius: 14px;
            border: 1px solid rgba(255, 255, 255, 0.5);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        """
        title_color = "#1e293b"
        subtitle_color = "#64748b"
        suggestion_bg = "rgba(255, 255, 255, 0.7)"
        suggestion_border = "rgba(255, 255, 255, 0.5)"
        suggestion_text_color = "#475569"

    # Feature cards - 4 cột
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f'''<div style="{card_style}">
                <div style="font-size: 1.75rem; margin-bottom: 0.4rem;">📍</div>
                <div style="font-weight: 600; color: {title_color}; font-size: 0.9rem;">{get_text("home_feature_nearby", lang)}</div>
                <div style="font-size: 0.75rem; color: {subtitle_color};">{get_text("home_feature_nearby_desc", lang)}</div>
            </div>''',
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f'''<div style="{card_style}">
                <div style="font-size: 1.75rem; margin-bottom: 0.4rem;">🗺️</div>
                <div style="font-weight: 600; color: {title_color}; font-size: 0.9rem;">{get_text("home_feature_route", lang)}</div>
                <div style="font-size: 0.75rem; color: {subtitle_color};">{get_text("home_feature_route_desc", lang)}</div>
            </div>''',
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f'''<div style="{card_style}">
                <div style="font-size: 1.75rem; margin-bottom: 0.4rem;">💰</div>
                <div style="font-weight: 600; color: {title_color}; font-size: 0.9rem;">{get_text("home_feature_budget", lang)}</div>
                <div style="font-size: 0.75rem; color: {subtitle_color};">{get_text("home_feature_budget_desc", lang)}</div>
            </div>''',
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            f'''<div style="{card_style}">
                <div style="font-size: 1.75rem; margin-bottom: 0.4rem;">🤖</div>
                <div style="font-weight: 600; color: {title_color}; font-size: 0.9rem;">{get_text("home_feature_ai", lang)}</div>
                <div style="font-size: 0.75rem; color: {subtitle_color};">{get_text("home_feature_ai_desc", lang)}</div>
            </div>''',
            unsafe_allow_html=True
        )

    # Popular searches - compact
    st.markdown(
        f'''<div style="
            background: {suggestion_bg};
            backdrop-filter: blur(10px);
            border-radius: 12px;
            padding: 0.75rem 1.25rem;
            margin-top: 1rem;
            border: 1px solid {suggestion_border};
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
            text-align: center;
        ">
            <span style="color: #ea580c; font-weight: 600;">{get_text("home_suggestion_label", lang)}</span>
            <span style="color: {suggestion_text_color};"> {get_text("home_suggestion_list", lang)}</span>
        </div>''',
        unsafe_allow_html=True
    )