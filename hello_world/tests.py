from django.test import TestCase

# Create your tests here.
def index(request):
    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)