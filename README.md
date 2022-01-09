# Bài tập lớn môn nhập môn học máy và khai phá dữ liệu

Source chính là file PhanLoaiTieuDeBaiBao.py

Data là file data.csv (Chưa qua bước tiền xử lý)

Project sử dụng 2 model là Multinomial Naive Bayes và Support vector machine - xử lý bài toán Multi - class classification

Model SVM (SVC) hiệu quả hơn với độ chính xác, precision and recall, f1 score đều cao hơn MultinomialNB

### Các bước xử lý bài toán Phân loại tiêu đề bài báo:

- Biểu diễn, mô tả dữ liệu

- Tiền xử lý dữ liệu: tách chữ, từ (sử dụng package underthesea); lower case; chuyển số -> numbers, ngày tháng -> days, phần trăm -> percents làm giảm feature; bỏ các kí tự không cần thiết; loại bỏ stop word.

- Vector hóa dữ liệu

- Sử dụng TF-IDF

- Chia đều dữ liệu từ các label thành các tập train và test với Stratified

- Model training

- Model evaluation

- Final

Model SVC được lưu trong file moel_SVC.sav

### Thư viện được sử dụng:

- Scikit-learn

- Underthesea

- Pandas

- Tqdm

- Matplotlib

### Những bước còn phải làm:

- Thêm unique data doisong, kinhdoanh, suckhoe, thoisu (done)

- Lựa chọn tham số tối ưu: kernel, C... (dùng tqdm) => Vẽ biểu đồ với từng tham số (done)

- Viết file jupyter (trực quan hóa data, chi tiết các bước, chi tiết các thuật toán) (done)

### Những điều cần note vào báo cáo:

- So sánh tốc độ chạy giữa 2 thuật toán

- Tốc độ và độ "chính xác" của model khi không dùng tf-idf và khi dùng, khi dùng random split và khi dùng stratified

- Độ "chính xác" khi chênh lệch data, khi cân bằng, khi unique thấp...

- Lý giải???
