from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from.models import*
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    if "email" in request.session:
        try:
            uid = User.objects.get(email=request.session["email"])  # User ko fetch karo
            filter_data = request.GET.get("filter")
            main_cid = Category.objects.all()
            sub_cid = SubCategory.objects.all()
            pid = Product.objects.all()
            show_click_pid= request.GET.get("catagary")
            if filter_data:
                pid = pid.filter(filter_data = main_cid)
            if show_click_pid:
                pid = Product.objects.filter(main_cid=show_click_pid) 
            else:
                pid = Product.objects.all() 
        
            con = {
                "uid": uid,
                "main_cid":main_cid,
                "sub_cid": sub_cid,
                "pid":pid,
                "filter_data":filter_data,
                "show_click_pid":show_click_pid
                  
                   }
            return render(request, "index.html", con)
        except User.DoesNotExist:  # Agar user nahi milta
            return render(request, "login.html")  # Ya kisi aur page par redirect karein
    else:
        return render(request, "login.html")  # Agar email session mein nahi hai
    
def cart(request):
    if "email" in request.session:
        try: 
            uid = User.objects.get(email=request.session['email'])
            cart_item = Add_to_cart.objects.filter(user_id=uid)

            Subtotal = 0
            Shipping = 200
            Total = 0
            for i in cart_item:
                Subtotal = Subtotal + i.total_price
                Total = Subtotal + Shipping 


            con = {
                "uid": uid,
                "cart_item": cart_item,
                "Subtotal":Subtotal,
                "Shipping":Shipping,
                "Total":Total,
                }   
            return render(request, "cart.html", con)

        except User.DoesNotExist:
            messages.error(request, "User Does Not Exist.")
            return render(request, "login.html")
    else:
        return render(request, "login.html")
    
from django.shortcuts import redirect, render
from django.contrib import messages

def add_to_cart(request, id):
    if "email" in request.session: 
        uid = User.objects.get(email=request.session["email"])
        pid = Product.objects.get(id=id)
        cart_item = Add_to_cart.objects.filter(user_id=uid, product_id=pid).first()
        if cart_item:
            cart_item.quantity += 1
            cart_item.total_price = cart_item.original_price * cart_item.quantity
            cart_item.save()
        else:
            Add_to_cart.objects.create(
                user_id=uid,
                product_id=pid,
                name=pid.name,
                image=pid.image,
                original_price=pid.original_price,
                quantity=1,
                total_price=pid.original_price
            )
        return redirect("cart")
    else:
        return render(request, "login.html")
    
def increment(request,id):
    cart_item = Add_to_cart.objects.get(id=id)
    if cart_item:
        cart_item.quantity += 1 
        cart_item.total_price = cart_item.original_price*cart_item.quantity
        cart_item.save() 
        return redirect('cart')
    
def decrement(request,id):
    cart_item = Add_to_cart.objects.get(id=id)
    if cart_item.quantity >1:
        cart_item.quantity -=1
        cart_item.total_price = cart_item.original_price*cart_item.quantity
        cart_item.save()
        return redirect('cart')
    else:
        cart_item.delete()
        return redirect('cart')
def delet_item(request,id):
    cart_item = Add_to_cart.objects.get(id=id)
    if cart_item:
        cart_item.delete()
    return redirect('cart')  


           

def checkout(request):
    if "email" in request.session:
        try:
            uid = User.objects.get(email=request.session["email"])
            con = {
                "uid":uid
            }
            return render(request,"checkout.html",con)
        except User.DoesNotExist:
            messages.error(request,"User Dose not Exist.....")
            return render(request,"login.html")
    else:
        return render(request,"login.html")

    
def detail(request,id):
    if "email" in request.session:
        try:
            uid = User.objects.get(email=request.session["email"])
            pid = Product.objects.get(id = id)
            con = {"uid":uid,
                    "pid":pid,
                    }
            return render(request,"detail.html",con)
        except User.DoesNotExist:
            messages.error(request,"User Does Not Exist.")
            return render(request,"login.html")
    else:
        return render(request,"login.html") 
       
def fackdetail(request):
    if "email" in request.session:
        try:
           uid = User.objects.get(email=request.session["email"])
           pid = Product.objects.all()
        
           con = {"uid":uid,"pid":pid}
           return render(request,"detail.html",con)
   
        except User.DoesNotExist:
            messages.error(request,"User Does Not Exist.")
            return render(request,"login.html")
    else:
        return render(request,"login.html")
    
def wishlist(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        wishlist_item = Add_to_Wishlist.objects.filter(user_id=uid)

    
        con = {
            "uid":uid,
            "wishlist_item":wishlist_item
        }

        return render(request,"wishlist.html",con) 
    else:
        return render(request,"login.html")
    
def add_to_wishlist(request, id):
    if "email" in request.session:
        uid = User.objects.get(email=request.session["email"])
        pid = Product.objects.get(id=id)
        wishlist_item = Add_to_Wishlist.objects.filter(user_id=uid, product_id=pid).first()

        if not wishlist_item:
            Add_to_Wishlist.objects.create(
                user_id=uid,
                product_id=pid,
                name=pid.name,
                image=pid.image,
                original_price=pid.original_price
            )
            messages.error(request,"Your Wishlist item Create.") 
        else:
            wishlist_item.delete()
            messages.error(request,"Your Wishlist item deleted.")
        return redirect('shop')     
    else:
        return render(request, "login.html")
    
def remove_wishlist(request,id):
    wishlist_item = Add_to_Wishlist.objects.get(id=id)
    if wishlist_item:
        wishlist_item.delete()
    return redirect('wishlist')

       
       
from django.core.paginator import Paginator  
def shop(request):
    if "email" in request.session:
        try:
            uid = User.objects.get(email=request.session["email"])
            main_cid = Category.objects.all()
            sub_cid = SubCategory.objects.all()
            pid = Product.objects.all().order_by("-id")

            # color filtering  syntex : request.GET.getlist('key_name') 
            price_fil = request.GET.get("price")
            color_fil = request.GET.getlist("color")
            size_fil = request.GET.getlist("size")

            sorting = request.GET.get("sort")

            search = request.GET.get("search")
            if size_fil:
                pid = Product.objects.filter(size__in=size_fil)
            else:
                pid = Product.objects.all()     

            filter_data = request.GET.get("filter")
            show_click_pid= request.GET.get("catagary")
           

            if filter_data:
                pid = Product.objects.filter(filter_data = main_cid)
            elif color_fil:
                pid = Product.objects.filter(color__in = color_fil)
           
            elif search:
                pid = Product.objects.filter(name__icontains=search)
            elif show_click_pid:
                pid = Product.objects.filter(main_cid=show_click_pid)    
            else:
                pid = Product.objects.all()
             # product sorting
            if sorting == "ltoh":
                pid = Product.objects.order_by("original_price")
            elif sorting == "htol":
                pid = pid.order_by("-original_price")
            elif sorting == "atoz":
                pid = pid.order_by("name")  
            elif sorting == "ztoa":
                pid = pid.order_by("-name") 
            else:
                pid = Product.objects.all() 
            # filter product by price
            # __gte: Greater than or equal to (>=)
            # __gt: Greater than (>)
            # __lt: Lese than (<)
            # __lte: Less than or equal to (<=)
            if price_fil == "0-100":
                pid = Product.objects.filter(original_price__gte=0, original_price__lte=100)
            elif price_fil == "100-200":
                pid = Product.objects.filter(original_price__gte=100, original_price__lte=200)  # Typo fixed here
            elif price_fil == "200-300":
                pid = Product.objects.filter(original_price__gte=200, original_price__lte=300)  # Typo fixed here
            elif price_fil == "300-400":
                pid = Product.objects.filter(original_price__gte=300, original_price__lte=400)  # Typo fixed here
            elif price_fil == "400-500":
                pid = Product.objects.filter(original_price__gte=400, original_price__lte=3000)  # Typo fixed here
            else:
                pid = Product.objects.all().order_by("-id")  # No filtering

            paginator = Paginator(pid,3)
            page_number = request.GET.get("page",1)
            try:
             page_number = int(page_number)
            except ValueError:
             page_number = 1 
            pid = paginator.get_page(page_number)
            show_page = paginator.get_elided_page_range(page_number, on_each_side=1, on_ends=1) 
            
            con = {
                "uid":uid,
                "pid":pid,
                "main_cid":main_cid,
                "sub_cid":sub_cid,
                "sorting":sorting,
                "price_fil":price_fil,
                "color_fil" :color_fil,
                "show_page":show_page,
                "search":search,
                "show_click_pid":show_click_pid,
               
                  }
            return render(request,"shop.html",con)
        except User.DoesNotExist:
            messages.error(request,"User Does not Exist.")
            return render(request,"login.html",con)
    else:
        return render(request,"login.html")    

    

def contact(request):
    if "email" in request.session:

        if request.method == "POST":
            name = request.POST["name"]
            email = request.POST["email"]
            subject = request.POST["subject"]
            message = request.POST["message"]

            # user = User.objects(name=name,email=email,subject=subject,message=message)
            # user.save()
            Contact.objects.create(name=name, email=email, subject=subject, message=message)
            return redirect('contact')
        else:     
          return render(request, "contact.html")
    else:
        return render(request,"login.html")    

def register(request):

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST['email']
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # if not name:
        #     messages.error(request,"Name is Required.....")
        # elif len(name) < 8 :
        #     messages.error(request,"Full name is must be 8 char long")
        # elif len(password) < 8 :
        #     messages.error(request,"Password is must be 8 char long")

        # if not messages.get_messages(request):

        if password == confirm_password:
            User.objects.create(name=name,email=email,password=confirm_password)
            return render(request,"login.html")
        else:
            messages.error(request,"password is not match.")
            return render(request,"register.html")
        
        # else:
            # return render(request,"register.html")
             
    else:
        return render(request,"register.html")  
      
def login(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session["email"])
        return render(request,"index.html")

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST["password"]

        try:
            uid = User.objects.get(email=email)  
            if uid.password == password:
                uid = request.session["email"] = uid.email
                return render(request, "index.html")
            else:
                messages.error(request, "Invalid Password")
                return render(request, "login.html")
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
            return render(request, "login.html")
    else:
        return render(request, 'login.html')
    
def log_out(request):
    if "email" in request.session:
        del request.session["email"]
        return render(request,"login.html") 
    else:
        return render(request,"login.html")   
    
import random 
from django.core.mail import send_mail 
def forgot(request):
    if request.POST:
        email = request.POST["email"]
        otp = random.randint(100000,999999)

        try:
            uid = User.objects.get(email=email)
            uid.otp = otp
            uid.save()
        
            send_mail(
                "Django",
                f"Your OTP is := {otp}.",
                "pareshbharda06@gmail.com",  # Sender's email
                [email],                     # Recipient's email
                fail_silently=False,
            )
            context={
                "email":email
            }

            return render(request,"reset_password.html",context)

        except User.DoesNotExist:
            messages.error(request,"User Does Not Exist.")
            return render(request,"forgot.html")

    return render(request, "forgot.html")

def reset_password(request):
    if request.POST:
        email = request.POST["email"]
        otp = request.POST["otp"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        try:
            uid = User.objects.get(email=email)

            if str(uid.otp) != str(otp):
                messages.error(request,"OTP is Invalide.....")
                return render(request,"reset_password.html")
            
            if password != confirm_password:
                messages.error(request,"Password does Not Match")
                return render(request,"reset_password.html")
            
            uid.password = password
            uid.save()
            messages.success(request,"Your Password Reset Succesfuly...")
            return redirect("index")

        except User.DoesNotExist:
            messages.error(request,"User Does Not Exist") 
            return render(request,"reset_password.html")   

    return render(request, "reset_password.html")




    
   

import pyotp

# Secret key create करना
secret = pyotp.random_base32()

# 5 minute (300 seconds) के लिए TOTP object बनाना
totp = pyotp.TOTP(secret, interval=300)   # 5 minute....., 600 means ki 10 minute.

# OTP Generate करना (यह 10 मिनट तक valid रहेगा)
otp = totp.now()
print(f"Generated OTP: {otp}")

# OTP Verify करना (5 मिनट तक valid रहेगा)
if totp.verify(otp):
    print("OTP is valid")
else:
    print("OTP is invalid")
