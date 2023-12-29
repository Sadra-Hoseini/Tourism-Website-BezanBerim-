from tourism.forms import LoginForm
from django.http import HttpResponse,HttpRequest
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from tourism.models import Book,Tour
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


boolean = {'first':'' , 'second':'' , 'third' : ''}
member_obj = None

def global_context(request):
    
    login_form = LoginForm()
    #boolean ['first'] = 'true'

    

    if request.method == 'POST' and 'LoginBtn' in request.POST :
        
        #boolean['second'] = 'true'
        #boolean['third'] = 'false'
        login_obj = LoginForm(request.POST)
        if login_obj.is_valid():
            email = login_obj.cleaned_data.get('email')
            password = login_obj.cleaned_data.get('password')
            
            username = User.objects.get(email = email ).username

            
            
            #user = User.objects.get(email = email)
            #if username is not None:
            user = authenticate(request , username = username , password = password )

            

            if user is not None:
                login(request , user)
                #member_obj['first'] = user
                messages.success(request , 'شما وارد شده اید')
                
            elif username is not None:
                #boolean['second'] = 'false'
                #boolean['third'] = 'false'
                messages.error(request, 'رمز عبور اشتباه است')
            else:
                #boolean['second'] = 'false'
                #boolean['third'] = 'false'
                messages.error(request, 'شما هنوز ثبت نام نکرده اید')
        else:
                #boolean['second'] = 'false'
                #boolean['third'] = 'false'
                messages.error(request,'لطفا اطلاعات را دقیق وارد کنید')

        

    if request.method == 'POST' and 'LogoutBtn' in request.POST:
          logout(request)
          
          #boolean['second'] = 'false'
          #boolean['third'] = 'false'


    tour_cart = []
    current_user = request.user
    if current_user.is_authenticated:
        tours_id = Book.objects.filter(user_id = current_user.id).values_list('tour_id',flat = True)
        for id in tours_id:
             tour = Tour.objects.get(id = id)
             tour_cart.append(tour)
             
              
 
            
              
    context = {'login_form' : login_form , 'tour_cart' : tour_cart}
    return context
    '''login_form = LoginForm()
    boolean ['first'] = 'true'

    

    if request.method == 'POST':
        boolean['second'] = 'true'
        login_obj = LoginForm(request.POST)
        if login_obj.is_valid():
            email = login_obj.cleaned_data.get('email')
            password = login_obj.cleaned_data.get('password')

            username = User.objects.get(email = email).username
            if username is not None:
                user = authenticate(request , username = username , password = password)

            

                if user is not None:
                    login(request , user)
                    user_obj['first'] = User.objects.get(email = email , password = password)
                    messages.success(request , 'شما وارد شده اید')
                else:
                    messages.error(request, 'شما هنوز ثبت نام نکرده اید')
            else:
                messages.error(request, 'شما هنوز ثبت نام نکرده اید')
        else:
                messages.error(request,'لطفا اطلاعات را دقیق وارد کنید')

    context = {'login_form' : login_form , 'boolean': boolean , 'user': user_obj }'''
    
    