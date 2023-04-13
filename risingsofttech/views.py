

from django.shortcuts import render



def index(request):
    context = {}
    return render(request,'contents/index.html',context)

def error_404(request, exception):
    data = {}
    return render(request,'page-errors/page-404.html', data)