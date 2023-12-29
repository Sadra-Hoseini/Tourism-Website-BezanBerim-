
from django import forms
from django.forms import ModelForm
from .models import Customer,Agency,Book,Tour
from django.core.exceptions import ValidationError




class CustomerRegistrationForm(ModelForm):
    

    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder' : " تکرار رمز عبور *" , 'class' :"form-control"}))
    password =  forms.CharField(widget = forms.PasswordInput(attrs={'placeholder' : " رمز عبور *" , 'class' :"form-control"}))

    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'first_name' : forms.TextInput(attrs={'placeholder' : "* نام " , 'class' :"form-control"}),
            'last_name' : forms.TextInput(attrs={'placeholder' : "* نام خانوادگی" , 'class' :"form-control"}),
            'password' : forms.PasswordInput(attrs={'placeholder' : " رمز عبور *" , 'class' :"form-control"}),
            'email' : forms.EmailInput(attrs={'placeholder' : "  پست الکترونیک *" , 'class' :"form-control"}),
            'phone_number' : forms.TextInput(attrs={'placeholder' : "* تلفن تماس" , 'class' :"form-control"}),

                          

        }


    def clean(self):
        
        cleaned_data = super(CustomerRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        

        if password != confirm_password:
            raise ValidationError('password and confirm_password does not match' , code='password_mismatch')

         
        



class AgencyRegistrationForm(ModelForm):

    password =  forms.CharField(widget = forms.PasswordInput(attrs={'placeholder' : " رمز عبور *" , 'class' :"form-control"}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder' : " تکرار رمز عبور *" , 'class' :"form-control"}))

    class Meta:
        model = Agency
        fields = '__all__'

        widgets = {

            'agency_name' : forms.TextInput(attrs={'placeholder' : "* نام شرکت  ", 'class' :"form-control"}),
            'password' : forms.PasswordInput(attrs={'placeholder' : " رمز عبور *" , 'class' :"form-control"}),
            'email' : forms.EmailInput(attrs={'placeholder' : "  پست الکترونیک *" , 'class' :"form-control"}),
            'phone_number' : forms.TextInput(attrs={'placeholder' : "* تلفن تماس" , 'class' :"form-control"}),

                          

        }


    def clean(self):
        cleaned_data = super(AgencyRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
           raise ValidationError('password and confirm_password does not match')  
        






class LoginForm(forms.Form):

    email = forms.CharField(max_length=200 , widget= forms.EmailInput(attrs= {'class':"box" ,  'placeholder':"ایمیل خود را وارد کنید" }))
    password =  forms.CharField(widget = forms.PasswordInput(attrs={'class' :"box" , 'placeholder' : " * رمز عبور" , }))        





class ForgotPasswordForm(forms.Form):

    email = forms.CharField(max_length=200 , widget = forms.EmailInput(attrs = {'class' : 'form-control', 'required placeholder' : "ایمیل خود را وارد کنید"}))    





class ResetPasswordForm(forms.Form):

    new_password = forms.CharField(max_length=200 , widget=forms.PasswordInput(attrs= {'class' : 'form-control', 'required placeholder' : "رمز عبور جدید را وارد کنید"}))
    confirm_password = forms.CharField(max_length=200 , widget=forms.PasswordInput(attrs= {'class' : 'form-control', 'required placeholder' : "تکرار رمز عبور "}))    


    def clean(self):
        cleaned_data = super(ResetPasswordForm, self).clean()
        password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
           raise ValidationError('password and confirm_password does not match')
        






class BookForm(forms.Form):

    CHOICES_list = []
    CHOICES_list.append((1,'لطفا تور مورد نظر را از این لیست انتخاب کنید'))
    tour_objects = Tour.objects.all()
    counter = 2
    for tour in tour_objects:
        CHOICES_list.append((tour,tour))
        counter += 1

    CHOICES = tuple(CHOICES_list)


    tour = forms.ChoiceField(choices = CHOICES ,initial='1' )
    number_of_persons = forms.IntegerField(widget= forms.NumberInput(attrs= { 'placeholder' : "تعداد افراد"}))
    names_of_persons = forms.CharField(max_length= 200 , widget= forms.TextInput(attrs= { 'placeholder' : "نام و نام خانوادگی نفر اول - نام و نام خانوادگی نفر دوم - ..."}))       