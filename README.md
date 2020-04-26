# The_Reddit_Project
 
 The Jupyter Notebooks:
This folder contains all the three jupyter notebooks along with the final dataset saved as a .csv file. It also contains a folder called attempts, which has all the previous attempts at the final notebooks.
Gathering Data Final - Contains the data gathering process.
Exploratory Data Analysis Final - Contains the data exploring process.
nl_algo - Contains the application of ML alogorithms to collected data. Also includes analysis of the algorithms in form of the classification report, confusion matrix and accuracy score.

The_Django_Website:
Contains the django app. It makes use of the django rest framework for the api.
Procfile,nltk.txt and requirements.txt are needed to deploy it on Heroku. 
The webapp contains the information regarding the website.
The api contains information regarding the api.

Requirements-

We need a Reddit account :
Then go to apps and create an app ( it needs to be a script )
Use the information to set up Reddit instance ( client_id, client_secret, username, password, user_agent ) in the data gathering notebook.

We also need a Google Could Platform account :
Create service account and download the JSON file with credentials and enter the path in the data gathering notebook in front of the GOOGLE_APPLICATION_CREDENTIALS.

(Python  : Python 3.7.3)

The following should be present to use the jupyter notebooks:
asgiref==3.2.7
cachetools==4.1.0
certifi==2020.4.5.1
chardet==3.0.4
click==7.1.1
cycler==0.10.0
DateTime==4.3
Django==3.0.5
google-api-core==1.17.0
google-auth==1.14.1
google-cloud==0.34.0
google-cloud-bigquery==1.24.0
google-cloud-core==1.3.0
google-resumable-media==0.5.0
googleapis-common-protos==1.51.0
idna==2.9
joblib==0.14.1
kiwisolver==1.2.0
matplotlib==3.2.1
nltk==3.5
numpy==1.18.3
pandas==1.0.3
pickle-mixin==1.0.2
praw==7.0.0
prawcore==1.3.0
protobuf==3.11.3
pyasn1==0.4.8
pyasn1-modules==0.2.8
pyparsing==2.4.7
python-dateutil==2.8.1
pytz==2019.3
regex==2020.4.4
requests==2.23.0
rsa==4.0
scikit-learn==0.22.2.post1
scipy==1.4.1
seaborn==0.10.0
six==1.14.0
sklearn==0.0
sqlparse==0.3.1
tqdm==4.45.0
update-checker==0.16
urllib3==1.25.9
websocket-client==0.57.0
zope.interface==5.1.0

For the django project, the following should be present:
asgiref==3.2.7
certifi==2020.4.5.1
chardet==3.0.4
click==7.1.1
dj-database-url==0.5.0
Django==3.0.5
django-heroku==0.3.1
djangorestframework==3.11.0
gunicorn==20.0.4
idna==2.9
joblib==0.14.1
nltk==3.5
numpy==1.18.3
pandas==1.0.3
praw==6.5.1
prawcore==1.0.1
psycopg2==2.8.5
python-dateutil==2.8.1
pytz==2019.3
regex==2020.4.4
requests==2.23.0
scikit-learn==0.22.2.post1
scipy==1.4.1
six==1.14.0
sklearn==0.0
sqlparse==0.3.1
tqdm==4.45.0
update-checker==0.16
urllib3==1.25.9
websocket-client==0.57.0
whitenoise==5.0.1

To host the website, copy the root directory (RedditFlair). Go inside it and start the server using manage.py

Website : https://test2muskan.herokuapp.com/flairr  
API : https://test2muskan.herokuapp.com/automated_testing
