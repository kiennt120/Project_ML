from underthesea import word_tokenize
import string
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
import pickle

file = open(r'stopword.txt', 'r', encoding='utf-8')
df = pd.read_csv(r'data.csv', names=['label', 'title'], encoding='utf-8')

stopwords = []
for line in file:
    stopwords.append(line.replace("\n", ""))
file.close()

punc = string.punctuation.replace("_", "").replace("/", "").replace("%", "") + '‘’'

def text_process(line):
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

# print(df.groupby('label').describe())


# # Split data
# Lấy mẫu Stratified
stratified = StratifiedShuffleSplit(test_size=0.3)
for train_index, test_index in stratified.split(df['title'], df['label']):
    strat_train_set = df.loc[train_index]
    strat_test_set = df.loc[test_index]

msg_train, label_train = strat_train_set['title'], strat_train_set['label']
msg_test, label_test = strat_test_set['title'], strat_test_set['label']

# Lấy mẫu random
# msg_train, msg_test, label_train, label_test = train_test_split(df['title'], df['label'], test_size=0.3)

# Training a model
pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),
    ('tfidf', TfidfTransformer()),
    ('model', OneVsRestClassifier(MultinomialNB()))
])

pipeline.fit(msg_train, label_train)
filename = open(r'model_MultiNB.sav', 'wb')
pickle.dump(pipeline, filename)
filename.close()

pipeline2 = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),
    ('tfidf', TfidfTransformer()),
    ('model', OneVsRestClassifier(SVC()))
])
pipeline2.fit(msg_train, label_train)
filename2 = open(r'model_SVC.sav', 'wb')
pickle.dump(pipeline2, filename2)
filename2.close()

# Đánh giá model
# predictions = pipeline.predict(msg_test)
# predictions2 = pipeline2.predict(msg_test)
#
# print("Mô hình Muitinomial Naive Bayes: ")
# print(classification_report(label_test, predictions))
# print("Mô hình Support vector machine: ")
# print(classification_report(label_test, predictions2))
