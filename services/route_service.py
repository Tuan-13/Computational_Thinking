# route_service.py
import requests
import time
from geopy.distance import geodesic
from utils.translate import get_text # [MỚI] Import hàm dịch

def get_icon_and_instruction(maneuver, road_name, lang="vi"):
    m_type = maneuver.get('type')
    modifier = maneuver.get('modifier')
    road = road_name if road_name else get_text("unnamed", lang) # Hoặc để trống tùy ý
    
    # Mapping hướng sang Key trong config
    mapping = {
        "left": ("⬅️", "nav_left"),
        "right": ("➡️", "nav_right"),
        "slight left": ("↖️", "nav_slight_left"),
        "slight right": ("↗️", "nav_slight_right"),
        "sharp left": ("↙️", "nav_sharp_left"),
        "sharp right": ("↘️", "nav_sharp_right"),
        "straight": ("⬆️", "nav_straight"),
        "uturn": ("↩️", "nav_uturn"),
    }
    
    icon = "⬆️"
    instruction = get_text("nav_default", lang).format(m_type)

    if m_type == "depart":
        icon, instruction = "🏁", get_text("nav_depart", lang).format(road)
    elif m_type == "arrive":
        icon, instruction = "🎉", get_text("nav_arrive", lang)
    elif m_type == "roundabout" or m_type == "rotary":
        exit_num = maneuver.get('exit', 1)
        icon, instruction = "🔄", get_text("nav_roundabout", lang).format(exit_num, road)
    elif m_type == "fork":
        if modifier in mapping:
            icon = mapping[modifier][0]
            dir_text = mapping[modifier][0] # Icon mũi tên làm hướng
            instruction = get_text("nav_fork", lang).format(dir_text, road)
    elif m_type == "end of road":
        if modifier in mapping:
            icon = mapping[modifier][0]
            dir_text = mapping[modifier][0]
            instruction = get_text("nav_end_of_road", lang).format(dir_text, road)
    elif modifier in mapping:
        icon = mapping[modifier][0]
        # Gọi get_text với key tương ứng và format đường vào
        instruction = get_text(mapping[modifier][1], lang).format(road)
    
    return icon, instruction

def get_route(start_lat, start_lon, end_lat, end_lon, mode="driving", lang="vi"):
    base_url = "http://router.project-osrm.org/route/v1"

    # Prepare fallback mode order
    modes_to_try = [mode]
    for m in ("driving", "walking", "cycling"):
        if m not in modes_to_try:
            modes_to_try.append(m)

    last_error = None
    # Try each mode with up to 3 attempts
    for try_mode in modes_to_try:
        url = f"{base_url}/{try_mode}/{start_lon},{start_lat};{end_lon},{end_lat}?overview=full&geometries=geojson&steps=true"
        for attempt in range(3):
            try:
                r = requests.get(url, timeout=6)
                r.raise_for_status()
                data = r.json()
                if 'routes' not in data or not data['routes']:
                    last_error = f"No routes returned for mode {try_mode}"
                    break
                route = data['routes'][0]

                geometry = route['geometry']['coordinates']
                path = [[point[1], point[0]] for point in geometry]

                steps_raw = route.get('legs', [{}])[0].get('steps', [])
                steps_data = []

                for step in steps_raw:
                    maneuver = step.get('maneuver', {})
                    road_name = step.get('name', '')
                    icon, instruction = get_icon_and_instruction(maneuver, road_name, lang)
                    steps_data.append({
                        "icon": icon,
                        "instruction": instruction,
                        "distance": step.get('distance', 0),
                        "duration": step.get('duration', 0)
                    })

                return path, route.get('distance', 0), route.get('duration', 0), steps_data
            except Exception as e:
                last_error = f"mode {try_mode} attempt {attempt}: {e}"
                time.sleep(0.3)
                continue
    if last_error:
        print(f"OSRM Error: {last_error}")
        # fallback: straight line with estimated duration
        dist_m = int(geodesic((start_lat, start_lon), (end_lat, end_lon)).meters)
        v = 1.2 if mode == 'walking' else 3.5 if mode == 'cycling' or mode == 'bicycling' else 7.0
        dur_s = int(dist_m / v) if v > 0 else 0
        path = [[start_lat, start_lon], [end_lat, end_lon]]
        steps = [{
            "icon": "⬆️",
            "instruction": get_text("nav_default", lang).format(get_text("unnamed", lang)),
            "distance": dist_m,
            "duration": dur_s,
            "approximate": True
        }]
        return path, dist_m, dur_s, steps