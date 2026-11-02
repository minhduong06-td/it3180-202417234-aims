# Lab 05 – Câu hỏi thảo luận

## Upstream first và release first
Upstream first sửa trên `master` trước, rồi đưa sang release. Release first sửa ngay trên bản đang bị lỗi, sau đó chuyển bản vá về các nhánh khác. Cách thứ hai sửa bản cũ nhanh hơn nhưng dễ sót nhánh nếu không kiểm tra.

## Nếu quên sửa release/lab05 thì phát hiện thế nào?
Dùng `git cherry -v origin/release/lab05 origin/release/lab04` để so sánh bản vá, sau đó kiểm tra trực tiếp việc tìm `lion` trên từng phiên bản.
