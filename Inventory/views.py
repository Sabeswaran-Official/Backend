from django.shortcuts import render

# Create your views here.

def samp(request):
    data={
        "name":"ram",
        "age":21
    }
    return render(request,'samp.html',data)