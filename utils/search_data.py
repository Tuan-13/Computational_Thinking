# search_data.py

# Danh sách món ăn và từ khóa liên quan (Đa ngôn ngữ + Không dấu)
# Cấu trúc: "TỪ_KHÓA_CHUẨN_OSM": ["alias 1", "alias 2", "ngôn ngữ khác"...]

DISH_DATABASE = {
    # =========================================================================
    # NHÓM 1: BÚN / PHỞ / MÌ (VIETNAMESE NOODLE SOUPS)
    # =========================================================================
    "phở bò": [
        "pho bo", "beef noodle soup", "beef noodle", "牛肉粉", 
        "sopa de fideos con ternera", "soupe tonkinoise au boeuf", "sopa de macarrão com carne", 
        "เฝอเนื้อ", "حساء المعكرونة بقر", "소고기 쌀국수", "牛肉フォー"
    ],
    "phở gà": [
        "pho ga", "chicken noodle soup", "chicken noodle", "鸡肉粉", 
        "sopa de fideos con pollo", "soupe de nouilles au poulet", "canja de galinha vietnamita", 
        "เฝอไก่", "حساء الدجاج بالشعيرية", "닭고기 쌀국수", "鶏肉フォー"
    ],
    "bún chả": [
        "bun cha", "grilled pork noodle", "烤肉米粉", 
        "cerdo a la parrilla con fideos", "porc grillé aux vermicelles", 
        "บุ๋นชา", "شعيرية لحم الخنزير المشوي", "분짜", "ブンチャ"
    ],
    "bún bò huế": [
        "bun bo hue", "hue beef noodle", "spicy beef noodle", "順化牛肉粉",
        "fideos de ternera picantes", "soupe de nouilles de hue", 
        "บุ๋นบ่อเหว", "نودلز اللحم الحار", "분보후에", "ブンボーフエ"
    ],
    "bún riêu": [
        "bun rieu", "crab noodle", "crab paste vermicelli", 
        "sopa de fideos de cangrejo", "soupe de nouilles au crabe", 
        "บุ๋นเรียว", "شعيرية السلطعون", "분리우", "ブンリュウ"
    ],
    "mì quảng": [
        "mi quang", "quang noodle", "廣南麵", "nouilles de quang", 
        "หมี่กว๋าง", "مي كوانغ", "미꽝", "ミークアン"
    ],
    "hủ tiếu": [
        "hu tieu", "kuy teav", "pork seafood noodle",
        "sopa de fideos de cerdo", "soupe de nouilles au porc", 
        "ก๋วยเตี๋ยว", "هو تيو", "후티우", "フーティウ"
    ],
    "cao lầu": ["cao lau", "hoi an noodle", "nouilles de hoi an", "เกาเหลา", "카오라우", "カオラウ"],
    "bún cá": ["bun ca", "fish noodle", "sopa de pescado", "soupe de poisson", "ขนมจีนน้ำยาปลา", "생선 국수", "ブンカー"],
    "bánh canh": ["banh canh", "thick noodle soup", "udon vietnam", "udon vietnamita", "반깐", "バンカン"],
    "bún thịt nướng": [
        "bun thit nuong", "grilled pork with vermicelli", 
        "vermicelles au porc grillé", "fideos con cerdo asado", 
        "ขนมจีนหมูย่าง", "분팃느엉", "ブンティットヌオン"
    ],
    "mì xào giòn": [
        "mi xao gion", "crispy egg noodles", 
        "fideos fritos crujientes", "nouilles frites croustillantes", 
        "หมี่กรอบราดหน้า", "바삭한 볶음면", "揚げ麺"
    ],
    "bánh canh cua": [
        "banh canh cua", "crab udon soup", 
        "sopa de udon de cangrejo", "soupe udon au crabe", 
        "ก๋วยจั๊บญวนปู", "게살 국수", "バンカンクア"
    ],

    # =========================================================================
    # NHÓM 2: MÓN CƠM & BÁNH VIỆT (VIETNAMESE RICE & CAKES)
    # =========================================================================
    "cơm tấm": [
        "com tam", "broken rice", "碎米飯", 
        "arroz roto", "riz cassé", "arroz quebrado", 
        "ข้าวต้ม", "أرز مكسور", "껌땀", "コムタム"
    ],
    "cơm gà": [
        "com ga", "chicken rice", "鸡饭", 
        "arroz con pollo", "riz au poulet", "arroz de frango", 
        "ข้าวมันไก่", "أرز الدجاج", "치킨 라이스", "コムガー"
    ],
    "cơm chiên": ["com chien", "fried rice", "arroz frito", "riz cantonais", "ข้าวผัด", "أرز مقلي", "볶음밥", "チャーハン"],
    "bánh mì": [
        "banh mi", "vietnamese sandwich", "baguette", "bread", "越式法包",
        "bocadillo vietnamita", "sandwich vietnamien", "sanduíche vietnamita", 
        "บั๋นหมี่", "بان مي", "반미", "バインミー"
    ],
    "bánh xèo": [
        "banh xeo", "vietnamese pancake", "pancake", "越式煎餅",
        "crepe vietnamita", "crêpe vietnamienne", "panqueca vietnamita", 
        "ขนมเบื้องญวน", "فطيرة فيتنامية", "반쎄오", "バインセオ"
    ],
    "bánh cuốn": ["banh cuon", "steamed rice roll", "rollo de arroz", "rouleau de riz", "ปากหม้อญวน", "반꾸온", "バインクオン"],
    "bánh bột lọc": ["banh bot loc", "tapioca dumpling", "empanadillas de tapioca", "raviolis de tapioca", "반봇록", "タピオカ餅"],
    "cơm niêu": [
        "com nieu", "claypot rice", 
        "arroz en olla de barro", "riz en pot d'argile", 
        "ข้าวอบหม้อดิน", "솥밥", "土鍋ご飯"
    ],
    "bánh bèo": ["banh beo", "water fern cake", "pastel de helecho", "gâteau de fougère", "บั๋นแบ่ว", "반베오", "バインベオ"],
    "bột chiên": [
        "bot chien", "fried rice flour cake", 
        "pastel de harina frito", "gâteau de farine frit", "massa frita", 
        "ขนมผักกาด", "봇찌엔", "揚げ餅"
    ],

    # =========================================================================
    # NHÓM 3: MÓN VIỆT CHÍNH (MAIN COURSES)
    # =========================================================================
    "bò kho": [
        "bo kho", "beef stew", 
        "estofado de ternera", "ragoût de bœuf", "ensopado de carne", 
        "สตูว์เนื้อ", "يخنة لحم البقر", "보코", "ビーフシチュー"
    ],
    "cá kho tộ": [
        "ca kho to", "caramelized fish", 
        "pescado caramelizado", "poisson au caramel", "peixe caramelizado", 
        "ปลาต้มเค็ม", "생선 조림", "魚の煮付け"
    ],
    "canh chua": [
        "canh chua", "sour soup", "sopa agria", "soupe aigre", "sopa azeda", 
        "แกงส้ม", "깐주아", "酸っぱいスープ"
    ],
    "rau muống xào": [
        "rau muong xao toi", "stir-fried morning glory", "water spinach",
        "espinaca de agua salteada", "liseron d'eau sauté", 
        "ผัดผักบุ้ง", "공심채 볶음", "空心菜炒め"
    ],
    "chả cá lã vọng": [
        "cha ca la vong", "turmeric fish with dill", 
        "pescado con eneldo", "poisson à l'aneth", "짜까라봉", "チャーカーラヴォン"
    ],
    "bò né": ["bo ne", "sizzling beef steak", "filete de ternera", "steak de bœuf", "สเต็กเนื้อ", "보네", "ボーネ"],

    # =========================================================================
    # NHÓM 4: ẨM THỰC QUỐC TẾ (INTERNATIONAL CUISINE) - [CẬP NHẬT TIẾNG HÀN/NHẬT]
    # =========================================================================
    "pizza": [
        "pizza", "italian pizza", "pizzeria", "pizza ý", 
        "พิซซ่า", "بيتزا", "pizze", "피자", "ピザ"
    ],
    "mì ý": [
        "mi y", "spaghetti", "pasta", "carbonara", "bolognese", 
        "espaguetis", "pâtes", "สปาเก็ตตี้", "معكرونة", "스파게티", "파스타", "スパゲッティ"
    ],
    "bít tết": [
        "bit tet", "steak", "beefsteak", "western steak", 
        "bistec", "steak frites", "bife", "สเต็ก", "شريحة لحم", "스테이크", "ステーキ"
    ],
    "gà rán": [
        "ga ran", "fried chicken", "kfc", "lotteria", "jollibee", 
        "pollo frito", "poulet frit", "frango frito", 
        "ไก่ทอด", "دجاج مقلي", "치킨", "프라이드치킨", "フライドチキン", "唐揚げ"
    ],
    "sushi": [
        "sushi", "sashimi", "japanese food", "cơm cuộn nhật", 
        "comida japonesa", "japonais", "ซูชิ", "سوشي", "스시", "초밥", "寿司", "すし"
    ],
    "ramen": [
        "ramen", "japanese noodle", "mì nhật", 
        "fideos japoneses", "nouilles japonaises", "ราเมน", "رامين", "라멘", "일본라면", "ラーメン"
    ],
    "dim sum": [
        "dim sum", "dimsum", "dumpling", "ha cao", "xiu mai", "há cảo", 
        "comida china", "chinois", "ติ่มซำ", "ديم سوم", "딤섬", "点心"
    ],
    "vịt quay": [
        "vit quay", "roast duck", "peking duck", "heo quay", 
        "pato asado", "canard rôti", "pato assado", 
        "เป็ดย่าง", "بط مشوي", "오리고기", "베이징덕", "ローストダック", "北京ダック"
    ],
    "lẩu thái": [
        "lau thai", "tom yum", "thai hotpot", 
        "olla caliente tailandesa", "fondue thaïlandaise", 
        "ต้มยำ", "توم يوم", "똠얌꿍", "태국식 샤브샤브", "トムヤムクン", "タイ風鍋"
    ],
    "pad thái": [
        "pad thai", "thai fried noodle", "phở thái", 
        "fideos tailandeses", "nouilles thaïlandaises", 
        "ผัดไทย", "باد تاي", "팟타이", "パッタイ"
    ],
    "thịt nướng hàn quốc": [
        "thit nuong han quoc", "korean bbq", "samgyeopsal", "galbi", 
        "barbacoa coreana", "barbecue coréen", 
        "หมูย่างเกาหลี", "شواء كوري", "삼겹살", "갈비", "한국식 바베큐", "サムギョプサル", "焼肉"
    ],
    "tokbokki": [
        "tokbokki", "tteokbokki", "spicy rice cake", "bánh gạo cay", 
        "pastel de arroz picante", "gâteau de riz épicé", 
        "ต๊อกบกกี", "كعك الأرز الحار", "떡볶이", "トッポギ"
    ],
    "kimbap": [
        "kimbap", "gimbap", "korean roll", "cơm cuộn hàn quốc", 
        "rollo coreano", "rouleau coréen", 
        "คิมบับ", "كيمباب", "김밥", "キンパ"
    ],
    "taco": [
        "taco", "burrito", "mexican food", "món mexico", 
        "comida mexicana", "mexicain", "ทาโก้", "تاكو", "타코", "タコス"
    ],
    "bánh crepe": [
        "banh crepe", "crepe", "pancake", 
        "crêpe", "crepa", "เครป", "كريب", "크레페", "クレープ"
    ],

    # =========================================================================
    # NHÓM 5: ĂN VẶT & ĐƯỜNG PHỐ (STREET FOOD)
    # =========================================================================
    "gỏi cuốn": [
        "goi cuon", "fresh spring roll", "summer roll", "春捲",
        "rollito de primavera fresco", "rouleau de printemps", 
        "เปาะเปี๊ยะสด", "لفائف الربيع", "고이꾸온", "월남쌈", "生春巻き"
    ],
    "nem rán": [
        "nem ran", "cha gio", "fried spring roll", "egg roll", "炸春捲",
        "rollito de primavera frito", "nems", 
        "เปาะเปี๊ยะทอด", "لفائف البيض", "짜조", "揚げ春巻き"
    ],
    "bún đậu": ["bun dau", "bun dau mam tom", "fermented shrimp paste noodle", "ขนมจีนกะปิ", "분더우", "ブンダウ"],
    "ốc": ["oc", "snail", "shellfish", "escargot", "caracoles", "caramujos", "หอย", "حلزون", "고동", "貝料理"],
    "xiên nướng": ["xien nuong", "skewer", "bbq", "kebab", "brocheta", "brochette", "espetinho", "مشاوي", "꼬치구이", "串焼き"],
    "bò lá lốt": ["bo la lot", "beef in betel leaf", "ternera en hoja de betel", "bœuf aux feuilles de bétel", "보라롯", "ボーラーロット"],
    "cháo gà": ["chao ga", "chicken porridge", "gachas de pollo", "bouillie de poulet", "โจ๊กไก่", "عصيدة الدجاج", "닭죽", "鶏粥"],
    "súp cua": ["sup cua", "crab soup", "sopa de cangrejo", "soupe de crabe", "กระเพาะปลา", "게살 스프", "蟹スープ"],
    "gỏi đu đủ": ["goi du du", "papaya salad", "ensalada de papaya", "salade de papaye", "ส้มตำ", "سلطة البابايا", "파파야 샐러드", "パパイヤサラダ"],
    "nem nướng": ["nem nuong", "grilled sausage", "salchicha asada", "saucisse grillée", "แหนมเนือง", "넴느엉", "ネムヌオン"],

    # =========================================================================
    # NHÓM 6: ĐỒ UỐNG & TRÁNG MIỆNG (DRINKS & DESSERTS)
    # =========================================================================
    "cà phê": [
        "ca phe", "coffee", "cafe", "咖啡", "café", "กาแฟ", "قهوة", "커피", "コーヒー"
    ],
    "cà phê trứng": ["ca phe trung", "egg coffee", "café con huevo", "café aux œufs", "กาแฟไข่", "에그 커피", "エッグコーヒー"],
    "trà sữa": ["tra sua", "milk tea", "bubble tea", "té con leche", "thé au lait", "ชานมไข่มุก", "شاي حليب", "밀크티", "버블티", "タピオカミルクティー"],
    "nước mía": ["nuoc mia", "sugarcane juice", "jugo de caña", "jus de canne", "น้ำอ้อย", "عصير قصب", "사탕수수 주스", "サトウキビジュース"],
    "sinh tố": ["sinh to", "smoothie", "batido", "shake", "น้ำปั่น", "عصير", "스무디", "スムージー"],
    "chè": ["che", "sweet soup", "sopa dulce", "soupe sucrée", "ของหวาน", "حساء حلو", "쩨", "チェー"],
    "bánh pía": ["banh pia", "durian cake", "pastel de durian", "gâteau au durian", "ขนมเปี๊ยะ", "반피아", "バインピア"],
    "chè trôi nước": ["che troi nuoc", "glutinous rice balls", "bolas de arroz", "boules de riz", "บัวลอย", "체트로이느억", "白玉団子"],
    "chè khúc bạch": ["che khuc bach", "almond panna cotta", "panna cotta de almendras", "체쿡박", "アーモンドパンナコッタ"],
    "bia hơi": ["bia hoi", "fresh beer", "draft beer", "cerveza fresca", "bière pression", "เบียร์สด", "بيرة", "생맥주", "ビアホイ"],
    "bánh flan": ["banh flan", "caramel pudding", "flan", "pudim", "คาราเมลคัสตาร์ด", "플랜", "プリン"],
    "rau câu": ["rau cau", "jelly", "gelatina", "gelée", "วุ้น", "젤리", "ゼリー"]
}

# Mapping cho các nhóm lớn (Categories)
CATEGORY_MAPPINGS = {
    # Ẩm thực quốc tế
    "món âu": ["pizza", "pasta", "steak", "spaghetti", "burger", "western food", "european", "양식", "西洋料理"],
    "món nhật": ["sushi", "ramen", "sashimi", "udon", "japanese food", "tempura", "일식", "日本料理"],
    "món hàn": ["korean bbq", "kimchi", "tokbokki", "kimbap", "korean food", "한식", "韓国料理"],
    "món thái": ["pad thai", "tom yum", "thai food", "som tum", "태국 요리", "タイ料理"],
    "fast food": ["kfc", "mcdonald", "lotteria", "burger", "fried chicken", "pizza", "패스트푸드", "ファーストフード"],

    # Đồ chay
    "chay": [
        "vegetarian", "vegan", "chay", "plant based", "素食",
        "vegetariano", "vegano", "végétarien", "végétalien", 
        "มังสวิรัติ", "เจ", "نباتي", "채식", "비건", "ベジタリアン"
    ],
    
    # Hải sản
    "hải sản": [
        "seafood", "hai san", "fish", "crab", "海鮮",
        "mariscos", "pescado", "fruits de mer", "poisson", 
        "อาหารทะเล", "مأكولات بحرية", "سمك", "해산물", "シーフード"
    ],
    
    # Đồ nướng
    "đồ nướng": [
        "bbq", "grill", "nuong", "yakiniku", "烤肉",
        "parrilla", "asado", "grillade", "barbecue", 
        "ปิ้งย่าง", "หมูกระทะ", "مشاوي", "شواء", "바베큐", "구이", "バーベキュー", "焼き肉"
    ],
    
    # Lẩu
    "lẩu": [
        "hotpot", "lau", "shabu", "火鍋",
        "olla caliente", "fondue chinoise", 
        "สุกี้", "ชาบู", "وعاء ساخن", "핫팟", "샤브샤브", "火鍋"
    ],
    
    # Món nước
    "món nước": [
        "noodle", "soup", "pho", "bun", "ramen",
        "fideos", "sopa", "nouilles", "soupe", 
        "ก๋วยเตี๋ยว", "معكرونة", "حساء", "국수", "면 요리", "麺料理"
    ],
    
    # Cafe / Tráng miệng
    "cafe": [
        "coffee", "cafe", "tea", "bakery",
        "cafetería", "café", "คาเฟ่", "مقهى", "카페", "カフェ"
    ],
    
    # Đồ uống có cồn
    "quán nhậu": [
        "beer", "pub", "bar", "bia", "alcohol",
        "cerveza", "bière", "cerveja", 
        "เบียร์", "เหล้า", "بيرة", "مشروبات", "맥주", "술집", "居酒屋"
    ]
}