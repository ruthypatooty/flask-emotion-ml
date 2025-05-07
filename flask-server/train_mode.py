import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import numpy as np

df = pd.read_csv('./data/emotion_sentimen_dataset.csv')
X=df['text']
y=df['Emotion']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.5,random_state=None)

tfidf_vec = TfidfVectorizer()
X_train_tf = tfidf_vec.fit_transform(X_train)
X_test_tf = tfidf_vec.transform(X_test)

clf = MultinomialNB()
clf.fit(X_train_tf,y_train)

#evaluate
y_pred = clf.predict(X_test_tf)
accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy score: {accuracy}")
print(classification_report(y_test,y_pred, zero_division=0))
# print(classification_report(y_test,y_pred, zero_division=np.nan))
with open('trained_model.pkl', 'wb') as f:
    pickle.dump(clf, f)
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf_vec, f)