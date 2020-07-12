from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"add.html")
def calc(request):
        a=int(request.POST["num1"])
        b=int(request.POST["num2"])
        if 'add' in request.POST:    
            c=a+b
            return c
        if 'sub' in request.POST:    
            c=a-b
            return c   
        if 'mul' in request.POST:    
            c=a*b
            return c
        if 'div' in request.POST:    
            c=a/b
            return c
    
def calprint(request):
        c=calc(request)
        return render(request,"result.html",{"result":c})