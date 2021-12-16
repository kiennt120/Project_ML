import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
import pickle
from TextPreprocess import text_process

df = pd.read_csv(r'data.csv', names=['label', 'title'], encoding='utf-8')
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
pickle.dump(pipeline, open(r'model_MultiNB.sav', 'wb'))

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
predictions = pipeline.predict(msg_test)
predictions2 = pipeline2.predict(msg_test)

print("Mô hình Muitinomial Naive Bayes: ")
print(classification_report(label_test, predictions))
print("Mô hình Support vector machine: ")
print(classification_report(label_test, predictions2))
