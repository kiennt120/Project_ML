from underthesea import word_tokenize
import string

def stopw():
    file = open(r'stopword.txt', 'r', encoding='utf-8')
    stopwords = []
    for line in file:
        stopwords.append(line.replace("\n", ""))
    file.close()

    punc = string.punctuation.replace("_", "").replace("/", "").replace("%", "") + '‘’'
    return stopwords, punc

def text_process(line):
    stopwords, punc = stopw()
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
    # Remove stop words

    # words = ' '.join(words)
    word = []
    for w in words:
        if w not in stopwords:
            word.append(w)

    return word