import os
import pickle
try:
    import create_the_base as ps
except ImportError:
    from . import create_the_base as ps



modulePath = os.path.dirname(__file__)  # get current directory
filePath = os.path.join(modulePath, 'svc_f2_model_lasttitle.pickle')
print('fiepath',filePath)

Dtree_classifier = pickle.load(open('svc_f2_model_lasttitle.pickle','rb'))

def get_flair(text):
    return Dtree_classifier.predict([text])




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

    






