# 🍽️ Tìm Quán Ăn Thông Minh (Smart Restaurant Finder)

Dự án là một ứng dụng web tìm kiếm và gợi ý quán ăn thông minh được xây dựng bằng Streamlit, tích hợp bản đồ tương tác (Folium) và một trợ lý ảo AI Foodie Guide sử dụng mô hình Gemini để đưa ra các gợi ý và phân tích chuyên sâu về ẩm thực. Ứng dụng tập trung vào trải nghiệm người dùng thân thiện, tốc độ tìm kiếm nhanh và khả năng tương tác đa ngôn ngữ.

# ✨ Tính Năng Chính

## Tìm kiếm Địa điểm Linh hoạt:

  - Cho phép người dùng tìm kiếm quán ăn theo tên món hoặc loại hình ẩm thực (ví dụ: "Bánh Mì", "Lẩu Thái").

  - Hỗ trợ tìm kiếm theo vị trí hiện tại của người dùng (GPS) hoặc nhập thủ công một địa điểm cụ thể.

  - Lọc kết quả theo Bán kính (Radius) và Ngân sách (Bình dân $, Trung bình $$, Sang trọng $$$).

## Bản đồ Tương tác & Dẫn đường:

  - Sử dụng thư viện Folium để hiển thị trực quan các quán ăn tìm được trên bản đồ.

  - Tính toán và hiển thị tuyến đường đi (dẫn đường) chi tiết từ vị trí người dùng đến quán ăn được chọn (sử dụng OSRM).

## Trợ lý Ẩm thực AI (Gemini Chatbot):

  - Tích hợp một Foodie Guide AI (sử dụng Gemini 2.5 Flash) có khả năng nhìn thấy (RAG Context) danh sách các quán ăn đang hiển thị trên bản đồ.

  - Tư vấn, so sánh, và đưa ra gợi ý chuyên sâu dựa trên các quán đã tìm thấy.

## Hỗ trợ Đa Ngôn ngữ:
  - Dịch thuật tự động giao diện sang nhiều ngôn ngữ phổ biến (Anh, Trung, Hàn, Nhật, Pháp, v.v.) bằng thư viện googletrans.

# 🛠️ Công Nghệ Sử Dụng

| Loại | Công nghệ/Thư viện | Mục đích |
|------|--------------------|----------|
| Giao diện | Streamlit | Xây dựng giao diện ứng dụng web bằng Python. |
| AI/NLP | Google GenAI (Gemini 2.5 Flash) | Cung cấp tính năng Chatbot và xử lý ngôn ngữ. |
| Bản đồ | Folium, streamlit-folium | Hiển thị và tương tác với bản đồ. |
| Dữ liệu | Overpass API (OSM) | Truy vấn dữ liệu địa lý về các quán ăn. |
| Vị trí/Dẫn đường | Geopy (Nominatim), OSRM | Geocoding và tính toán tuyến đường đi. |
| Ngôn ngữ | googletrans, unidecode | Dịch thuật giao diện và chuẩn hóa truy vấn tìm kiếm. |

# ⚙️ Yêu Cầu Hệ Thống

- Để chạy ứng dụng, bạn cần cài đặt Python 3.8+ và các thư viện được liệt kê trong file requirements.txt.

## 1. Cài đặt Thư viện

- Sử dụng pip để cài đặt tất cả các dependencies:

- pip install -r requirements.txt


## 2. Cấu hình API Key

- Tính năng Trợ lý Ảo AI yêu cầu GEMINI_API_KEY.

  1.Lấy API Key từ Google AI Studio.

  2.Tạo file .streamlit/secrets.toml trong thư mục dự án (nếu chạy local).

  3.Thêm key vào file với định dạng sau:

```# .streamlit/secrets.toml
GEMINI_API_KEY = "YOUR_API_KEY_HERE"
```

> Lưu ý: Nếu không có key, ứng dụng vẫn chạy nhưng tính năng Chatbot sẽ bị vô hiệu hóa.

# 🚀 Cách Cài Đặt và Chạy Dự Án

1. Tải các file: Đảm bảo bạn có đủ các file Python chính (main.py, config.py, utils.py, services.py) và thư mục views (chứa map_view.py và chatbot_view.py).

2. Cài đặt thư viện (theo hướng dẫn ở trên).

3. Chạy ứng dụng bằng Streamlit trong thư mục chứa file main.py:

```
streamlit run main.py
```

4. Ứng dụng sẽ mở tự động trong trình duyệt web của bạn, thường là tại địa chỉ http://localhost:8501.

# 🤝 Người Đóng Góp

[Tên của bạn] - Vai trò chính: [Ví dụ: Phát triển Giao diện và Tích hợp AI]

[Tên người đóng góp khác (Nếu có)]
