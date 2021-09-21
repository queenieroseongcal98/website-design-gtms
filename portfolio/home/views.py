from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    #return HttpResponse ("This is my homepage(/)")
    context = { 'name': 'Pawan', 'course': 'Python'}
    return render(request, 'home.htm', context)

def register(request):
    #return HttpResponse ("This is my about page (/about)")
    return render(request, 'register.htm')

def rates(request):
    #return HttpResponse ("This is my rates page(/rates)")
    return render(request, 'rates.htm')

def login(request):
    #return HttpResponse ("This is my login page(/contact)")
    return render(request, 'accounts/login.htm')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        desc = request.POST['desc']
        #print(name, email, phone, addresss, desc)
        ins = Contact(name=name, email=email, phone=phone, address=address, desc=desc)
        ins.save()
        print("The data has been written to the database")
    #return HttpResponse ("This is my contact page(/contact)")
    return render(request, 'contact.htm')