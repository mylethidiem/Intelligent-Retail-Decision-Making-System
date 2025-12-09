#!/bin/bash

# --- CẤU HÌNH API BACKEND (UVICORN) ---

echo "Starting Uvicorn API Backend on port 5050..."

# Sử dụng toán tử '&' để chạy lệnh Uvicorn ở chế độ nền (background)
# Điều này cho phép script tiếp tục chạy lệnh tiếp theo ngay lập tức.
uvicorn app.main:app --host 0.0.0.0 --port 5050 &

# CẢNH BÁO: Rất quan trọng! Thêm độ trễ để API có thời gian khởi động
# trước khi frontend cố gắng kết nối. Điều này ngăn lỗi "Connection refused".
echo "Waiting 10 seconds for API to initialize..."
sleep 10

# --- CẤU HÌNH FRONTEND (GRADIO) ---

echo "Starting Gradio Frontend..."

# Lệnh này sẽ chạy ở chế độ foreground (tiền cảnh)
# và giữ cho container/Space không bị thoát.
python -m app.frontend.gradio_ui

# Nếu Gradio của bạn được khởi chạy bằng launch(server_port=7860),
# thì lệnh này sẽ chiếm Terminal và giữ cho ứng dụng chạy.