from django.shortcuts import render
import praw
import pickle
import os
from . import detect_the_flair as dtf
#from . import train_the_model as dtf



# Create your views here.

reddit=praw.Reddit(client_id='',
                   client_secret='',
                   username='',
                   password='',
                   user_agent=''
                   )


'''def RedditFlair2(request):
	if request.method=='GET':
		return render(request,'redditflair.html',{})
	if request.method=='POST':
		reddit_url=request.POST.get('reddit_url')
		submission = reddit.submission(url = reddit_url)
		title=submission.title

		#modulePath = os.path.dirname(__file__)  # get current directory
		#filePath = os.path.join(modulePath, 'svc_f2title.pickle')

		#open_file = open(filePath, "rb")
		#Dtree_classifier = pickle.load(open_file)
		#open_file.close()

		dec_flair=s.sentiment(title)
		return render(request,'redditflair.html',{'sub_text':dec_flair})'''

def RedditFlair(request):
	if request.method=='GET':
		return render(request,'redditflair.html',{})
	if request.method=='POST':
		reddit_url=request.POST.get('reddit_url')
		submission = reddit.submission(url = reddit_url)
		title=submission.title
		dec_flair=title+'ok'
		return render(request,'redditflair.html',{'sub_text':dec_flair})

def RedditFlair2(request):
	if request.method=='GET':
		return render(request,'redditflair.html',{})
	if request.method=='POST':
		reddit_url=request.POST.get('reddit_url')
		submission = reddit.submission(url = reddit_url)
		title=submission.title

		dec_flair=dtf.get_flair(title)
		return render(request,'redditflair.html',{'sub_text':dec_flair})






