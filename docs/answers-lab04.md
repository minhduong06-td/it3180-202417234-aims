# Lab 04 – Câu hỏi thảo luận

## Vì sao không merge release/* ngược về master?
Vì release giữ một bản đã phát hành. Merge ngược cả nhánh có thể đưa thay đổi chỉ dành cho bản cũ vào master. Nếu cần, chỉ chuyển bản sửa tương ứng.

## Khác GitFlow thế nào?
GitFlow có `develop` và `main`, cùng các nhánh feature, release, hotfix. Bài thực hành dùng `master` làm nhánh phát triển và giữ từng bản ở `release/labXX`.

## Vì sao dùng 1.0.0 thay vì 0.4.0?
Vì Lab 04 là mốc phát hành 1.0.0 được quy định trong bài; các mốc Lab 01–03 là 0.x.
