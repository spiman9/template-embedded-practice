from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request  , 'index.html')

def index2(request):
    return render(request  , 'index-2.html')

def contact(request):
    return render(request , 'contact.html')

def service(request):
    return render(request , 'service.html')

def _404(request):
    return render(request , '404.html')

def about(request):
    return render(request , 'about.html')

def accordion(request):
    return render(request , 'accordion.html')

def alert(request):
    return render(request , 'alert.html')

def archive(request):
    return render(request , 'archive.html')

def blog(request):
    return render(request , 'blog.html')

def button(request):
    return render(request , 'button.html')

def comingsoon(request):
    return render(request , 'comingsoon.html')

def page_fullwidth(request):
    return render(request , 'page-fullwidth.html')

def page_sidebar(request):
    return render(request , 'page-sidebar.html')
    
def pricing(request):
    return render(request , 'pricing.html')

def progress(request):
    return render(request , 'progress.html')

def project(request):
    return render(request , 'project.html')

def service_item(request):
    return render(request , 'service-item.html')

def single_fullwidth(request):
    return render(request , 'single-fullwidth.html')

def single(request):
    return render(request , 'single.html')

def tab(request):
    return render(request , 'tab.html')

def typography(request):
    return render(request , 'typography.html')
