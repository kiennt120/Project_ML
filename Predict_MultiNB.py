# Load model
import pickle

loaded_model = pickle.load(open(r'model_MultiNB.sav', 'rb'))
n = input("Số tiêu đề muốn test: ")
n = int(n)

def predicts(res):
    if res == [1]:
        return 'Đời sống'
    elif res == [2]:
        return 'Du lịch'
    elif res == [3]:
        return 'Giải trí'
    elif res == [4]:
        return 'Giáo dục'
    elif res == [5]:
        return 'Khoa học'
    elif res == [6]:
        return 'Kinh doanh'
    elif res == [7]:
        return 'Pháp luật'
    elif res == [8]:
        return 'Sức khỏe'
    elif res == [9]:
        return 'Thể thao'
    else:
        return 'Thời sự'

for i in range(n):
    title = input("Nhập tiêu đề cần phân loại: ")
    result = loaded_model.predict([title])
    print(predicts(result))
