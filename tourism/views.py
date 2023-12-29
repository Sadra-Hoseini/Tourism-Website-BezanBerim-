from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django import forms
from .forms import CustomerRegistrationForm , AgencyRegistrationForm , LoginForm , ForgotPasswordForm , ResetPasswordForm , BookForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.hashers import make_password
from .models import Customer,Agency,Tour,Book
import re
from BezanBerim.context_processors import  member_obj , boolean , global_context
#from ..BezanBerim import context_processors






def home(request):
    
    #BookLink = request.GET.get('BookLink')

    if 'is_not_authenticated' in request.GET and request.user.is_authenticated != True  :
        messages.error(request,'لطفا ابتدا وارد حساب کاربری خود شوید')
        return redirect(reverse('home'))
    context = {}
    
    return render(request, 'home.html' , context)


def book(request):
    form = BookForm()
    current_user = request.user
    if current_user.is_authenticated :

        if request.method == 'POST' and 'BookBtn' in request.POST :
            BookForm_obj = BookForm(request.POST)
            if BookForm_obj.is_valid():
                tour_name = BookForm_obj.cleaned_data.get('tour')
                tour = Tour.objects.get(name = tour_name)
                number_of_persons = BookForm_obj.cleaned_data.get('number_of_persons')
                names_of_persons = BookForm_obj.cleaned_data.get('names_of_persons')

                book_obj = Book.objects.create(user = current_user , tour = tour , number_of_persons = number_of_persons , names_of_persons = names_of_persons)
                book_obj.save()
                messages.success(request,'تور جدید با موفقیت به سبد خرید شما افزوده شد')
                return redirect(reverse('home'))
                
            else:
                messages.error(request , 'لطفا اطلاعات را صحیح وارد کنید')

      

    context = {'BookForm' : form , 'current_user': current_user}

    return render(request, 'book.html' , context)




def tours(request):

    tour_objects = Tour.objects.all()
    context = {
        'tours': tour_objects,

        }

    return render(request, 'tours.html' , context)








def register(request):

    CustomerForm = CustomerRegistrationForm()
    AgencyForm = AgencyRegistrationForm()
    error = {'boolean' : 'False' , 'password' : '' , }

    if request.method == 'POST' and 'CustomerBtn' in request.POST  : 
        customer_obj = CustomerRegistrationForm(request.POST)
        if customer_obj.is_valid():
            model_obj = customer_obj.save()
            customer = Customer.objects.get(id = model_obj.id)
            user = User.objects.create_user(username = f"{customer.first_name} {customer.last_name} " ,email = customer.email ,password = customer.password)
            user.save()
            login(request , user)
            boolean['third'] = 'true'
            boolean['second'] = 'false'
            member_obj['second'] = user.username
            global_context(request)
            messages.success(request,'ثیت نام شما با موفقیت انجام شد')
            return redirect(reverse('home'))
        else  :
            messages.error(request , 'پسورد را صحیح وارد کنید')
            #error['boolean'] = 'True'
            #error['password'] = 'password and confirm_password does not match'
            
            
            

    elif request.method == 'POST'  and  'AgencyBtn' in request.POST:
        agency_obj = AgencyRegistrationForm(request.POST)
        if agency_obj.is_valid():
            model_obj = agency_obj.save()
            agency = Agency.objects.get(id = model_obj.id)
            user = User.objects.create_user(username = agency.agency_name,email = agency.email ,password = agency.password)
            user.save()
            login(request , user)
            boolean['third'] = 'true'
            boolean['second'] = 'false'
            member_obj['second'] = user.username
            global_context(request)
            messages.success(request,'ثیت نام شما با موفقیت انجام شد')
            return redirect(reverse('home'))
        else  :
            messages.error(request , 'پسورد را صحیح وارد کنید')
    
    context = {'CustomerForm' : CustomerForm , 'AgencyForm' : AgencyForm , 'error' : error , }

    return render(request, 'register.html' , context)    






def forgot_password(request):
    
        form = ForgotPasswordForm()

        
        if request.method == 'POST':
            
            fpf_obj = ForgotPasswordForm(request.POST)
            if fpf_obj.is_valid():
                
                email = fpf_obj.cleaned_data.get('email')
                try:
                    user = User.objects.get(email = email)
               
                    if user is not None:
                        return redirect(reset_password,username = user.username , id = user.pk)
                
                except:
                    messages.error(request , 'شما با این ایمیل ثبت نام نکرده اید')


            else:
                messages.error(request , 'لطفا ایمیل را صحیح وارد کنید')        
        context = {'form' : form}


        return render(request,'forgot_password.html', context)

    


def reset_password(request,username,id):
     form = ResetPasswordForm()

     
     if request.method == 'POST':
          
        rpf_obj = ResetPasswordForm(request.POST)
        if rpf_obj.is_valid():
             password = rpf_obj.cleaned_data.get('new_password')
             new_password = make_password(password,hasher = 'default')
             User.objects.filter(username = username , id = id).update(password = new_password)
             
             messages.success(request,'رمز عبور شما با موفقیت تغییر یافت')
             return redirect(reverse('home'))

        else:
             messages.error(request,'لطفا اطلاعات خواسته شده را دقیق وارد کنید')

     context = {'form' : form}


     return render(request,'reset_password.html', context)




def display_tour_items(request , pk = None):

    if pk:
        tour_item = Tour.objects.get(pk = pk)

    else:
        tour_item = ''

    destination_description = tour_item.destination_description
    x = re.sub('\r|\n' , '@' , destination_description)
    y = re.sub(r'@+' , '@' , x)
    z = re.split('@' , y)

    additional_description = tour_item.additional_description
    str_list = re.split('\.' , additional_description)
    ad = list(filter(None,str_list))    

    context = {'tour_item' : tour_item , 'destination_description' : z , 'additional_description' : ad}

    return render(request,'tour_item.html' , context)    





def services(request):
    context = {}

    return render(request, 'services.html' , context)





def gallery(request):
    context = {}

    return render(request, 'gallery.html' , context)




def review(request):
    context = {}

    return render(request, 'review.html' , context)






def contact(request):
    context = {}

    return render(request, 'contact.html' , context)






    