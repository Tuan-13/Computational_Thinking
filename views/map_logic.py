# views/map_logic.py
import random
import math
from geopy.distance import geodesic
from utils.translate import get_text

# --- 1. LOGIC TÍNH TOÁN VẬN TỐC & THỜI GIAN ---
def get_velocity(mode):
    """Trả về vận tốc (m/s) theo chế độ di chuyển"""
    if mode == "walking": return 1.2      # ~4.3 km/h
    elif mode == "bicycling" or mode == "cycling": return 3.5  # ~12.6 km/h
    else: return 7.0                      # ~25 km/h (Vận tốc trung bình trong phố)

def calculate_time_minutes(distance_meters, mode):
    """Công thức: Thời gian (phút) = Quãng đường (m) / Vận tốc (m/s)"""
    velocity = get_velocity(mode)
    seconds = distance_meters / velocity
    minutes = int(seconds / 60)
    return max(1, minutes) # Tối thiểu 1 phút

# --- 2. LOGIC XỬ LÝ DỮ LIỆU ---
def process_results(raw_results, center_lat, center_lon, budget, lang):
    """Xử lý dữ liệu thô: tính khoảng cách sơ bộ để sort, tạo dữ liệu giả lập (rating, price)"""
    processed = []
    for place in raw_results:
        tags = place.get('tags', {})
        name = tags.get('name', "Quán không tên")
        place_id = place['id']
        
        # Khoảng cách Geodesic dùng để sắp xếp danh sách ban đầu
        d = geodesic((center_lat, center_lon), (place['lat'], place['lon'])).meters
        
        random.seed(place_id) 
        simulated_rating = round(random.uniform(3.5, 5.0), 1)
        simulated_reviews = random.randint(15, 700)
        price_opts = ["$", "$", "$$", "$$", "$$$"] 
        simulated_price = random.choice(price_opts)

        is_match_budget = True
        if budget == get_text("budget_cheap", lang) and simulated_price != "$": is_match_budget = False
        elif budget == get_text("budget_medium", lang) and simulated_price != "$$": is_match_budget = False
        elif budget == get_text("budget_expensive", lang) and simulated_price != "$$$": is_match_budget = False
        
        if not is_match_budget: continue

        score = simulated_rating * math.log(1 + simulated_reviews)
        cuisine = tags.get('cuisine', tags.get('amenity', 'shop'))
        address = place.get('address', 'Đang cập nhật địa chỉ')

        processed.append({
            "id": place_id, "name": name, "lat": place['lat'], "lon": place['lon'],
            "cuisine": cuisine, "price": simulated_price, "rating": simulated_rating,
            "reviews": simulated_reviews, "score": score,
            "distance_sort": d, # Khoảng cách này dùng để sort
            "address": address
        })
    
    processed.sort(key=lambda x: x['score'], reverse=True)
    return processed[:15]