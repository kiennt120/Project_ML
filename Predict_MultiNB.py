# Load model
from PhanLoaiTieuDeBaiBao import text_process
import pickle

# dict = {[1]: 'Đời sống', [2]: 'Du lịch', [3]: 'Giải trí', [4]: 'Giáo dục', [5]: 'Khoa học',
#         [6]: 'Kinh doanh', [7]: 'Pháp luật', [8]: 'Sức khỏe', [9]: 'Thể thao', [10]: 'Thời sự'}

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
