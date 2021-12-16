# Bài tập lớn môn nhập môn học máy và khai phá dữ liệu

Source chính là file PhanLoaiTieuDeBaiBao.py

Data là file data.csv (Chưa được preprocess)

Project sử dụng 2 model là Multinomial Naive Bayes và Support vector machine - xử lý bài toán Multi - class classification

Model SVM (SVC) hiệu quả hơn với độ chính xác, precision and recall, f1 score đều cao hơn MultinomialNB

### Các bước xử lý bài toán Phân loại tiêu đề bài báo:

- Biểu diễn, mô tả dữ liệu (chưa xong)

- Tiền xử lý dữ liệu: tách chữ, từ (sử dụng package underthesea); lower case; chuyển số -> numbers, ngày tháng -> days, phần trăm -> percents làm giảm feature; bỏ các kí tự không cần thiết; loại bỏ stop word.

- Vector hóa dữ liệu

- Sử dụng TF-IDF

- Chia đều dữ liệu từ các label thành các tập train và test với Stratified

- Model training

- Model evaluation (chưa xong)

- Final

Model SVC và MultinomialNB được lưu trong 2 file moel_...sav tương ứng

File XuLyTiengViet.py không cần thiết

### Thư viện được sử dụng:

- Scikit-learn

- Underthesea

- Pandas
