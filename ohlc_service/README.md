# OHLC Data Service

## Tổng quan

OHLC Data Service là một dịch vụ API được xây dựng bằng FastAPI, cung cấp dữ liệu OHLC (Open, High, Low, Close) cho các tài sản tài chính như cổ phiếu, tiền điện tử, v.v. Dịch vụ này hỗ trợ lưu trữ, truy xuất và cập nhật dữ liệu OHLC, đồng thời có thể tự động lấy dữ liệu định kỳ thông qua scheduler.

## Tính năng

- **Cung cấp API RESTful** để truy xuất dữ liệu OHLC.
- **Tự động tạo và quản lý cơ sở dữ liệu** khi khởi động dịch vụ.
- **Scheduler tự động**: Lấy và cập nhật dữ liệu OHLC định kỳ.
- **Dễ dàng mở rộng** với các route và tính năng mới.
- **Quản lý cấu hình bảo mật** qua file `.env` (không commit lên git).

## Hướng dẫn cài đặt & setup

### 1. Clone repository

```bash
git clone <link-repo-cua-ban>
cd <ten-thu-muc-du-an>
```

### 2. Tạo và cấu hình file `.env`

Tạo file `.env` ở thư mục gốc dự án và thêm các biến môi trường cần thiết, ví dụ:

DATABASE_URL=sqlite

### 3. Cài đặt các thư viện phụ thuộc

Khuyến nghị sử dụng Python 3.8+ và pip:

```bash
pip install -r requirements.txt
```

### 4. Chạy dịch vụ

```bash
uvicorn app.api.main:app --reload
```

- Truy cập API docs tại: [http://localhost:8000/docs](http://localhost:8000/docs)

## Cấu trúc thư mục

```
ohlc_service/
├── app/
│   ├── api/
│   │   ├── main.py
│   │   └── routes/
│   ├── core/
│   ├── db/
│   └── services/
├── requirements.txt
└── README.md
```

## Đóng góp

Mọi đóng góp, báo lỗi hoặc đề xuất tính năng mới đều được hoan nghênh! Vui lòng tạo issue hoặc pull request.

---

**Lưu ý:**  
- Đảm bảo file `.env` đã được thêm vào `.gitignore` để tránh lộ thông tin nhạy cảm.
- Dịch vụ có thể cần cấu hình thêm tùy theo môi trường triển khai thực tế.