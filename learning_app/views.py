from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, QuestionForm, AnswerForm
from .models import Course, Question, Answer

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

@login_required
def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'course_detail.html', {'course': course})

@login_required
def forum(request):
    questions = Question.objects.all()
    return render(request, 'forum.html', {'questions': questions})

@login_required
def question_detail(request, slug):
    question = get_object_or_404(Question, slug=slug)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('question_detail', slug=slug)
    else:
        form = AnswerForm()
    return render(request, 'question_detail.html', {'question': question, 'form': form})
