from django.shortcuts import render

def index(request):
    if request.GET.get('group'):
        return render(request,'message.html')
    return render(request,'index.html')