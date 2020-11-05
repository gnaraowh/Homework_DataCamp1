import os
import numpy as np
import pandas as pd
import locale
import matplotlib.pyplot as plt 
import string
from nltk.corpus import stopwords
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

pd.set_option('display.max_rows', None, 'display.max_columns', None)

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
print(dir_path)

file_path = os.path.join(dir_path, 'SMSSpamCollection')
# sms = [line.rstrip() for line in open(file_path,'r', encoding='cp932', errors='ignore')]
# print(len(sms))

# for sms in enumerate(sms[0:10]):
#     print('\n', sms)

sms = pd.read_csv(file_path, sep='\t', names=['label','message'])
#print(sms.groupby('label').describe())

#print(sms['message'].apply(len))

#sms['len'] = sms['message'].apply(len)
#print(sms['message'].iloc[1])

#sms['len'].plot(bins=100, kind='hist')

#print(sms.len.describe())
#print(sms[sms['len'] == 910]['message'].iloc[0])
#sms.hist(column='len',by='label',bins=100,figsize=(14,8))
#plt.show()

# for i in range(11):
#     print('\n', sms[sms['label']=='spam']['message'].iloc[i])

# ## -- Punctuation -- ##
# print(string.punctuation)
# test = 'I **want to try! to remove?? punctuation: in = the (sentence/<)'
# no_punc = [x for x in test if x not in string.punctuation]
# print(no_punc)
# no_punc = ''.join(no_punc)
# print(no_punc)

# ## -- Remove Stopwords -- ##
# print((stopwords.words('english')))
# new_test = [word for word in no_punc.split() if word.lower() not in stopwords.words('english')]
# print(new_test)

def text_process(mess):
    no_punc = [x for x in mess if x not in string.punctuation]
    no_punc = ''.join(no_punc)
    text = [word for word in no_punc.split() if word.lower() not in stopwords.words('english')]

    return text

#new_sms = sms['message'].head(5).apply(text_process)

## -- Bag-Of-Word -- ##
# bow_transformer = CountVectorizer(analyzer=text_process).fit(sms['message'])

# print(len(bow_transformer.vocabulary_))
# print(sms['message'][3])
# bow_test = bow_transformer.transform([sms['message'][3]])
# print(bow_test)
# print(bow_transformer.get_feature_names()[4068])
# print(bow_transformer.get_feature_names()[4629])
# print(bow_transformer.get_feature_names()[5261])
# print(bow_transformer.get_feature_names()[6204])
# print(bow_transformer.get_feature_names()[6222])
# print(bow_transformer.get_feature_names()[7186])
# print(bow_transformer.get_feature_names()[9554])

# bow_sms = bow_transformer.transform(sms['message'])

#print(bow_sms.nnz)

# print('Shape of Sparse Matrix:', bow_sms.shape)
# print('None Zero:', bow_sms.nnz)
# print('% of Sparsity:', bow_sms.nnz*100/(bow_sms.shape[0] * bow_sms.shape[1]))

# tfidf_transformer = TfidfTransformer().fit(bow_sms)
# print(tfidf_transformer)

# tfidf_test = tfidf_transformer.transform(bow_test)
# print(tfidf_test)

# tfidf_sms = tfidf_transformer.transform(bow_sms)
# print(tfidf_sms)

# nb = MultinomialNB()
# x = tfidf_sms
# y = sms['label']
# spam_detection = nb.fit(x,y)

## -- เราไม่ได้ split ข้อมูลมาเทส แต่แรก เราเลยใช้ ข้อมูลเดิม (x) -- ##
# predicted = spam_detection.predict(x)
# print(predicted)
# confusion_matrix(y, predicted)
# print('Acc:', accuracy_score(y, predicted))
# print('F1 Score:', f1_score(y, predicted, pos_label='ham'))
# print('Precision Score:', precision_score(y, predicted, pos_label='ham'))
# print('Recall Score:', recall_score(y, predicted, pos_label='ham'))


sms_train, sms_test, label_train, label_test = train_test_split(sms['message'], sms['label'], test_size=0.2)
print(len(sms_train))
print(len(sms_test))

## -- Data Pipeline -- ##
pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])

pipeline.fit(sms_train, label_train)
predicted = pipeline.predict(sms_test)

print(predicted)

cm = confusion_matrix(label_test, predicted)
print(cm)

print('Acc:', accuracy_score(label_test, predicted))
print('F1 Score:', f1_score(label_test, predicted, pos_label='ham'))
print('Precision Score:', precision_score(label_test, predicted, pos_label='ham'))
print('Recall Score:', recall_score(label_test, predicted, pos_label='ham'))

df = pd.DataFrame(data=sms_test)

df['label'] = label_test
df['predicted'] = predicted

print(df)