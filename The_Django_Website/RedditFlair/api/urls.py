from django.urls import path
from . import views

urlpatterns = [
    path(r'automated_testing',views.api_create_blog_view),
]

