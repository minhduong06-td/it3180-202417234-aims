# Lab 01 – Xâu hỏi thảo luận

## Câu 1. Vì sao sử dụng `git mv`?

Lệnh `git mv` được sử dụng để di chuyển hoặc đổi tên các tệp đang được Git quản lý. Lệnh này đồng thời cập nhật vùng staging, giúp thao tác đổi tên hoặc di chuyển được ghi nhận trong commit tiếp. Git có thể nhận diện việc đổi tên tệp dựa trên mức độ tương đồng nội dung, ngay cả khi sử dụng lệnh di chuyển thông thường. Tuy nhiên, `git mv` giúp thao tác thuận tiện và nhất quán hơn. Có thể sử dụng `git log --follow -- aims/cart.py` để truy vết lịch sử của tệp `cart.py` trước và sau khi di chuyển vào thư mục `aims/`.

## Câu 2. Nhánh `release/lab01` có phải là baseline không?

Có. Branch `release/lab01` được sử dụng để lưu trạng thái mã nguồn đã thống nhất. Vai trò của branch là baseline để xác định phiên bản được nộp, kiểm tra tính toàn vẹn và so sánh với các phiên bản tiếp trong những lab sau. Baseline cần được kiểm soát thay đổi, không nên chỉnh sửa trực tiếp.

## Câu 3. Vì sao không commit trực tiếp vào `master` dù làm việc một mình?

Việc phát triển trên branch riêng và merge qua Pull Request giúp kiểm soát thay đổi.

Cụ thể:

- Theo dõi mục đích, nội dung và lịch sử của từng thay đổi.
- Kiểm tra mã nguồn và kết quả chạy thử trước khi merge.
- Duy trì tính ổn định của branch `master`.
- Thuận tiện khi cần đánh giá, truy vết hoặc hoàn tác thay đổi.
- Hình thành quy trình làm việc nhất quán, có thể áp dụng khi phát triển theo nhóm.

Ngay cả khi làm việc cá nhân, việc sử dụng Pull Request vẫn giúp bảo đảm tính minh bạch và khả năng kiểm soát lịch sử phát triển.
