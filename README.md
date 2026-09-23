# Bài tập: An toàn và bảo mật thông tin

## 1. Thông tin sinh viên
- **Họ và tên:** Nguyễn Đăng Thịnh
- **MSSV:** k235480106069
- **Email:** k235480106069@tnut.edu.vn
- **Deadline:** 23h59 ngày 28/9/2026

## 2. Tìm hiểu thuật toán mã hoá hiện đại DES và AES
- **Thuật toán DES (Data Encryption Standard):** Là thuật toán mã hóa khối với cấu trúc mạng Feistel. Quá trình mã hóa và giải mã thực hiện qua 16 vòng. Hiện nay DES không còn an toàn do kích thước khóa ngắn.
- **Thuật toán AES (Advanced Encryption Standard):** Thuật toán mã hóa hiện đại, an toàn hơn thay thế cho DES. Quá trình mã hóa thực hiện qua nhiều vòng lặp, mỗi vòng thực hiện các phép biến đổi thay thế và hoán vị trên các khối dữ liệu. 
- Mọi quy trình mã hoá/giải mã của AES đã được em cài đặt bằng ngôn ngữ Python trong file `aes_ma_hoa.py`.

## 3. Thuật toán mã hoá bất đối xứng RSA
- RSA sử dụng nguyên lý sinh cặp khóa bí mật và công khai dựa trên độ khó của việc phân tích một số nguyên lớn thành các thừa số nguyên tố.
- **Cách sinh cặp khóa:** Cặp khóa được sinh ra thông qua việc chọn 2 số nguyên tố lớn, tính tích của chúng (modulus) và tính toán hàm số Euler để tìm ra khóa công khai (Public Key) và khóa bí mật (Private Key).

## 4. Các mô hình áp dụng thuật toán RSA
Theo các lý thuyết về RSA, có các mô hình áp dụng chính sau đây:
- **Xác thực người gửi (Chữ ký số):** Người gửi dùng khóa bí mật của mình để mã hóa (ký) dữ liệu. Người nhận dùng khóa công khai của người gửi để giải mã, qua đó xác nhận đúng là người đó đã gửi.
- **Xác thực người nhận:** Người gửi dùng khóa công khai của người nhận để mã hóa dữ liệu. Chỉ người nhận sở hữu khóa bí mật tương ứng mới có thể giải mã và đọc được nội dung.
- **Xác thực cả hai:** Kết hợp cả hai phương pháp trên: Người gửi ký bằng khóa bí mật của mình, sau đó tiếp tục mã hóa toàn bộ bằng khóa công khai của người nhận. Điều này đảm bảo cả tính bảo mật và tính xác thực.

## 5. So sánh thời gian và cách dùng kết hợp sức mạnh RSA và AES
- **So sánh thời gian:** Thuật toán AES có thời gian mã hoá/giải mã nhanh hơn rất nhiều so với thuật toán RSA. RSA xử lý các phép toán phức tạp trên số lớn nên rất chậm và tốn tài nguyên.
- **Cách dùng kết hợp:** Trong thực tế, hệ thống kết hợp sức mạnh của cả hai bằng cách sử dụng phương pháp mã hóa lai (Hybrid Encryption). Hệ thống sẽ dùng thuật toán RSA để mã hóa và phân phối "khóa bí mật của AES" một cách an toàn giữa 2 bên. Sau khi hai bên đã trao đổi khóa an toàn, họ sẽ dùng thuật toán AES với khóa đó để mã hóa khối dữ liệu lớn nhằm đảm bảo tốc độ cao.
