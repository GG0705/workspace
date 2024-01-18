from django.http import HttpResponse

def homepage(request):
    print("Homepage Requested")
    return HttpResponse("<h1>This is home page.</h1>")