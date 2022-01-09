# Load model
import pickle
from TextPreprocess import *
loaded_model = pickle.load(open(r'model_SVC.sav', 'rb'))

n = input("Số tiêu đề muốn test: ")
n = int(float(n))

for i in range(n):
    title = input("Nhập tiêu đề cần phân loại: ")
    result = loaded_model.predict([title])
    print(predicts(result))
