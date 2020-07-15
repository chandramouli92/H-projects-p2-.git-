from django.http import HttpResponce
def index(request):
    return HttpResponce("hello world")
def home(request):
    return HttpResponce("<h1>welcome to home page</h1>")