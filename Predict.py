# Load model
from test import text_process
import pickle

# dict = {[1]: 'Đời sống', [2]: 'Du lịch', [3]: 'Giải trí', [4]: 'Giáo dục', [5]: 'Khoa học',
#         [6]: 'Kinh doanh', [7]: 'Pháp luật', [8]: 'Sức khỏe', [9]: 'Thể thao', [10]: 'Thời sự'}

loaded_model = pickle.load(open(r'model.sav', 'rb'))
result = loaded_model.predict(["12 người truy sát Quân 'Xa lộ' sắp hầu tòa"])
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

print(predicts(result))
