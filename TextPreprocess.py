from underthesea import word_tokenize
import string

def stop_word():
    file = open(r'stopword.txt', 'r', encoding='utf-8')
    stopwords = []
    for line in file:
        stopwords.append(line.replace("\n", ""))
    file.close()

    punc = string.punctuation.replace("_", "").replace("/", "").replace("%", "") + '‘’'
    return stopwords, punc

def text_process(line):
    stopwords, punc = stop_word()
    a = line.split()
    for i, x in enumerate(a):
        for j in a[i]:
            if j == '%':
                a[i] = 'percents'
                break
    line = ' '.join(a)
    str = word_tokenize(line, format="text").lower()
    words = [char for char in str if char not in punc]
    words = ''.join(words)
    words = words.split()
    n = len(words)
    for i in range(n):
        for j in words[i]:
            if j == '/':
                words[i] = 'days'
                break
        try:
            float(words[i])
            words[i] = 'numbers'
        except:
            continue

    word = []
    for w in words:
        if w not in stopwords:
            word.append(w)

    return word

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