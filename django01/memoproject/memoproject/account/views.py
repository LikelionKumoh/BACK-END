from django.shortcuts import render

# def home(request):
#     #  블로그 글들을 모두 띄우는 코드
#     # posts = Blog.objects.all()
#     posts = Blog.objects.filter().order_by('reg_date')

#     return render(request, 'index.html', {'posts' : posts})
