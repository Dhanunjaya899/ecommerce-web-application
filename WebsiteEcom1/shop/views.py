from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Products, Order
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login(request):
    if request.method == "POST":
        user_name = request.POST["txtusername"]
        user_password = request.POST["txtpassword"]
        u1 = authenticate(username=user_name,password=user_password)
        if u1 is not None:
            if u1.is_superuser:
                request.session['uname'] = user_name
                # login(request,u1)
                return redirect('index')
        else :
            return render(request,"shop/login.html",{'msg':'username and password is incorrect'})
    else:
        return render(request,'shop/login.html')

def register(request):
    if request.method == "POST":
        user_name = request.POST["txtusername"]
        user_password = request.POST["txtpassword"]
        user_email = request.POST["txtemail"]

        if User.objects.filter(username=user_name).exists():
            return render(request,'shop/register.html',{'uexists':'this user name and email already exists'})
        else:
            u1 = User.objects.create_superuser(username=user_name,password=user_password,email=user_email)
            u1.save()
            return redirect("log")
    else:
        return render(request,'shop/register.html' )


def admin_fun(request):
    return render(request,"shop/admin.html")


def adddetails_fun(request):
    if request.method == "POST":
        d1 = Products()
        d1.title = request.POST["txttitle"]
        d1.discount_per = int(request.POST["txtdiscount"])
        d1.price = int(request.POST["txtpricec"])
        d1.mrp_price = int(request.POST["txtmrpprice"])
        d1.color = request.POST["txtcolor"]
        d1.model_item = request.POST["txtmodel"]
        d1.category = request.POST["txtcategory"]
        d1.image = request.POST["txtimage"]
        d1.description = request.POST["txtdescription"]
        d1.save()
        return redirect('adddetails')
    else:
        return render(request,'shop/add_products.html')
    


def viewproduct_fun(request):
    v1 = Products.objects.all()
    return render(request,"shop/view_products.html",{'detail':v1})



def index(request):
    product_objects = Products.objects.all()

    # search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    # paginator code
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    return render(request,'shop/index.html',{'product_objects':product_objects,'data':request.session['uname']})


def detail(request,id):
    product_object = Products.objects.get(id=id)
    # mrp = Products.mrp_price
    # price = Products.price
    # calculated_value = ((mrp / 100) * price) - mrp
    return render(request,'shop/detail.html',{'product_object':product_object})


def checkout(request):
    if request.method =='POST':
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()
    return render(request,'shop/checkout.html')


def logout_fun(request):
    logout(request)
    # del request.session['uname']
    return redirect('log')
