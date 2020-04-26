import pandas as pd
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import os
from . import pls_work as ps
try:
    import create_the_base as ps
except ImportError:
    from . import create_the_base as ps




modulePath = os.path.dirname(__file__)  # get current directory
filePath = os.path.join(modulePath, 'corrected_dataset.csv')

df=pd.read_csv(filePath)
print(df.head())
df.drop('Unnamed: 0',axis=1,inplace=True)
X=df['title'].fillna(value='')
y=df['flair']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
Tipeline=ps.pipeline
Tipeline.fit(X_train,y_train)
save_classifier=open("svc_f2_model_last"+"title"+".pickle","wb")
pickle.dump(Tipeline,save_classifier)
save_classifier.close()
predictions = Tipeline.predict(X_test)
print('This is for','')
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
print('accuracy : ',accuracy_score(y_test,predictions))



'''comb_feats=df['comments']+df['title']+df['url']
X=comb_feats.fillna(value='')
y=df['flair']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
print('into pipeline')
pipeline.fit(X_train,y_train)
print('out of pipeline')
save_classifier=open("svc_f2"+"comb2_correct"+".pickle","wb")
pickle.dump(pipeline,save_classifier)
save_classifier.close()
predictions = pipeline.predict(X_test)
print('This is for','')
print(confusion_matrix(y_test,predictions))
print(sns.heatmap(confusion_matrix(y_test,predictions)))
print(classification_report(y_test,predictions))
print('accuracy : ',accuracy_score(y_test,predictions))'''

    



