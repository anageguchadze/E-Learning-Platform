from django.urls import path
from .views import index, login_view, register_view, course_list, course_detail, forum, question_detail

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('courses/', course_list, name='course_list'),
    path('courses/<int:id>/', course_detail, name='course_detail'),
    path('forum/', forum, name='forum'),
    path('forum/questions/<slug:slug>/', question_detail, name='question_detail'),
]
