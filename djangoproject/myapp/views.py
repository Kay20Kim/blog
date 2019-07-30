from django.shortcuts import render
from .models import Blog
# Create your views here.
from .form import BlogPost
def home(request):
    blogs = Blog.objects #모델로 부터 객체 목록을 전달 받을 수 있음
    return render(request, 'home.html', {'blogs' : blogs})

def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_vaild():
            post =form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            retrun redirect('home')
    else:
        form = BlogPost()
        return render(request,'new.html',{'form':form})