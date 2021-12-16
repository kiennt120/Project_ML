# Load model
import pickle
from TextPreprocess import predicts

loaded_model = pickle.load(open(r'model_MultiNB.sav', 'rb'))

n = input("Số tiêu đề muốn test: ")
n = int(n)

for i in range(n):
    title = input("Nhập tiêu đề cần phân loại: ")
    result = loaded_model.predict([title])
    print(predicts(result))
