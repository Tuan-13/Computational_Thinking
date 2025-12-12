# search_engine.py
from unidecode import unidecode
from utils.search_data import DISH_DATABASE, CATEGORY_MAPPINGS

def normalize_text(text):
    if not text: return ""
    return unidecode(text).strip().lower()

# Kiểm tra xem từ khóa có phải là thuật ngữ ẩm thực đã biết không
def is_known_food_term(user_query):
    raw_query = user_query.lower().strip()
    norm_query = normalize_text(raw_query)
    
    for cat_key, cat_values in CATEGORY_MAPPINGS.items():
        if cat_key in raw_query or normalize_text(cat_key) in norm_query: return True
        for val in cat_values:
            if val in raw_query: return True
            
    for standard_name, aliases in DISH_DATABASE.items():
        if normalize_text(standard_name) in norm_query: return True
        
        for alias in aliases:
            norm_alias = normalize_text(alias)
            if norm_alias in norm_query or (len(norm_query) > 3 and norm_query in norm_alias):
                return True
                
    basic_foods = [
        "com", "bun", "pho", "mi", "banh", "lau", "nuong", 
        "ga", "bo", "heo", "vit", "ca", "tom", "muc", "trung", "oc",
        "chicken", "beef", "pork", "fish", "rice", "noodle", "shrimp", "squid", "soup",
        "coffee", "cafe", "tra", "tea", "bread", "steak", "pizza", "pasta"
    ]
    query_words = norm_query.split()
    for food in basic_foods:
        if food == norm_query or food in query_words:
            return True
            
    return False

def expand_search_query_smart(user_query):
    """
    [CẬP NHẬT MẠNH] Mở rộng từ khóa tìm kiếm để bắt được nhiều quán hơn trên OSM.
    Xử lý thông minh: Chữ hoa/thường, không dấu, từ đồng nghĩa tiếng Anh.
    """
    raw_query = user_query.lower().strip()
    norm_query = normalize_text(raw_query)
    
    final_keywords = set()
    
    dish_found = False
    for standard_name, aliases in DISH_DATABASE.items():
        check_list = [standard_name] + aliases
        for term in check_list:
            term_norm = normalize_text(term)
            
            is_match = False
            
            if term_norm == norm_query:
                is_match = True
            
            elif term_norm in norm_query:
                is_match = True
                
            elif len(norm_query) > 2 and norm_query in term_norm:
                is_match = True
                
            if is_match:
                final_keywords.add(standard_name) 
                final_keywords.add(term)          
                for a in aliases[:3]: 
                    final_keywords.add(a)
                dish_found = True
                break
        if dish_found: break 

# 2. Mở rộng theo category nếu chưa tìm thấy dish cụ thể
    if not dish_found:
        for cat_key, cat_values in CATEGORY_MAPPINGS.items():
            
            if cat_key in raw_query or normalize_text(cat_key) in norm_query:
                final_keywords.update(cat_values)
            else:
                for val in cat_values:
                    
                    if val == raw_query or normalize_text(val) == norm_query: 
                        final_keywords.add(val)
                        final_keywords.add(cat_key)

    ingredient_mappings = {
        "gà": ["chicken", "cơm gà", "phở gà", "gà rán", "lẩu gà", "cháo gà", "kfc", "lotteria"],
        "ga": ["chicken", "cơm gà", "phở gà", "gà rán"],
        "chicken": ["gà", "fried chicken", "com ga"],
        
        "bò": ["beef", "phở bò", "bún bò", "bò kho", "bít tết", "steak"],
        "bo": ["beef", "pho bo", "bun bo"],
        "beef": ["bò", "steak"],
        
        "cá": ["fish", "bún cá", "chả cá", "cá kho"],
        "ca": ["fish", "bun ca"],
        
        "ốc": ["snail", "hải sản", "seafood", "oc"],
        "oc": ["snail", "hai san"],
        
        "vịt": ["duck", "vịt quay", "cháo vịt"],
        "vit": ["duck", "vit quay"],
        
        "cơm": ["rice", "cơm tấm", "cơm gà", "cơm rang", "cơm niêu"],
        "com": ["rice", "com tam", "com ga"],
        
        "bún": ["vermicelli", "bún bò", "bún chả", "bún riêu"],
        "bun": ["vermicelli", "bun bo", "bun cha"]
    }

    if norm_query in ingredient_mappings:
        final_keywords.update(ingredient_mappings[norm_query])
    else:
        for key, values in ingredient_mappings.items():
            if f" {key} " in f" {norm_query} " or key == norm_query:
                final_keywords.update(values)

    
    final_keywords.add(raw_query)
    final_keywords.add(norm_query)

    result = [k for k in final_keywords if len(k) >= 2]
    
    return list(result)