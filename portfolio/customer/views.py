from django.shortcuts import render, HttpResponse
from customer.models import Transaction, Feedback

# Create your views here.

def hcustomer(request):
    #return HttpResponse("This is my homepage(/)")
    context = {'name': 'Mars','course': 'Django'}
    return render(request, 'customer/hcustomer.htm', context)


def rates(request):
    #return HttpResponse ("This is my projects page(/projects)")
    return render(request, 'customer/rates.htm')


def sender(request):
    allTransaction = Transaction.objects.all()
    print(allTransaction)   
    for item in allTransaction:
        print(item.sender)
    context = {'transaction' : allTransaction}

    return render(request, 'customer/sender.htm', context)

def transaction(request):
    #context = {'sucess' : False}
    if request.method=="POST":
        sender = request.POST['sname']
        address = request.POST['saddress']
        goods = request.POST['gname']
        gtype = request.POST['gtype']
        price = request.POST['price']
        fee = request.POST['sfee']
        method = request.POST['pmethod']
        receiver = request.POST['rname']
        destination = request.POST['raddress']
        date = request.POST['tdate']
        #print(sname, saddress, gname, gtype, price, sfee, pmethod, rname, raddress, tdate )
        transaction = Transaction(sender=sender, address=address, goods=goods, gtype=gtype, price=price, fee=fee, method=method, receiver=receiver, destination=destination, date=date)
        transaction.save()
        print("the data has been written to the db")
        #context = {'success': True}

    #allTransaction = Transaction.objects.all()
    #print(allTransaction)   
    #for item in allTransaction:
    #    print(item.sender)
    #context = {'transaction' : allTransaction}


    return render(request, 'customer/transaction.htm')

def receiver(request):
    if 'receiver' in request.GET:
        receiver=request.GET['receiver']
        filteredTransaction = Transaction.objects.filter(receiver__icontains=receiver)
    else:
         filteredTransaction = Transaction.objects.none()    
    print(filteredTransaction)   
    for item in filteredTransaction:
        print(item.goods)
    context = {'transaction' : filteredTransaction}



    return render(request, 'customer/receiver.htm', context)

def feedback(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name, email, phone, desc)
        feedback = Feedback(name=name, email=email, phone=phone, desc=desc)
        feedback.save()
        print("the data has been written to the db")
        
    #return HttpResponse("This is my myaccount page(/myaccount)")
    return render(request, 'customer/feedback.htm')