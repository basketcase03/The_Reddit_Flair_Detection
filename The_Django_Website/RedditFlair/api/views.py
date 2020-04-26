from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
import io
import pathlib
import os
from io import TextIOWrapper
import json
import praw
from webapp import detect_the_flair as dtf



# Create your views here.

reddit=praw.Reddit(client_id='',
                   client_secret='',
                   username='',
                   password='',
                   user_agent=''
                   )


@api_view(['POST'])
@permission_classes([AllowAny])
def api_create_blog_view(request):
	if request.method=="POST":
		uploaded_file=request.FILES['upload_file']
		###########with open('name.txt', 'wb+') as destination:
			#for chunk in uploaded_file.chunks():
				#destination.write(chunk)
		#with open('name.txt','r') as f:
		'''print(uploaded_file.file)
		with open('name.txt','wb+') as f:
			f.write(uploaded_file.file)'''
		'''pathlib.Path('file1.txt').write_bytes(uploaded_file.file.read())
		tables=('file1.pdf') 
		with open('file1.txt','r') as f:
			print(f.read()) ##########'''
		d={}
		text_f = TextIOWrapper(uploaded_file, encoding='utf-8')
		text=text_f.readlines()
		######'''for chunk in uploaded_file.chunks():
			############text=TextIOWrapper(chunk,encoding='utf-8')'''
		for url in text:
			d[url.rstrip('\n')]=dtf.get_flair(reddit.submission(url = url).title)[0]   


		
		#if uploaded_file.content_type=='application/text':
		data={'text':text}
		#with open('person.txt', 'w') as json_file:
			#json.dump(d, json_file)
		return JsonResponse(d)


		