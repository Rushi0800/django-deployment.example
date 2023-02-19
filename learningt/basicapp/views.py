from django.shortcuts import render

# Create your views here.
def index(request):
    rushi_dict = {'text':'heyy all', 'number':99 }
    return render(request,'basicapp/index.html',rushi_dict)

def other(request):
    return render(request,'basicapp/other.html')

def relative(request):
    return render(request,'basicapp/relative_templates.html')
