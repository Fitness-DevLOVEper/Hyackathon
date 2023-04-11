from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import basepackage as bp
def redirect_to_login_page(request):
    return HttpResponseRedirect('http://127.0.0.1:5724/Login/')
def view_login_page(request):
    return render(request, 'login_screen.html')

def forgot_screen1(request):
    return render(request, 'forgot_screen1.html')

class sample:
    OTP=0
    email=''
    password=''
    username=''
    call_name=''
def forgot_screen2(request):
        sample.email=request.POST['email']
        sample.OTP=bp.generate_otp.send_otp(sample.email)
        return render(request,'forgot_screen2.html')
def verify_otp(request):
        entered_otp=int(request.POST['OTP'])
        if(entered_otp==sample.OTP):
            return render(request,'reset_screen.html')
        else:
            return HttpResponseRedirect('http://127.0.0.1:5724/Login/forgot1')

def send_otp(request):
        sample.email=request.POST['email']
        sample.password=request.POST['password']
        sample.call_name=request.POST['call_name']
        sample.OTP=bp.generate_otp.send_otp(sample.email)
        return render(request,'signup_screen2.html')
        
def verify_otp1(request):
    entered_otp=int(request.POST['OTP'])
    if(entered_otp==sample.OTP):
            return render(request,'signup_screen3.html')
    else:
            return HttpResponseRedirect('http://127.0.0.1:5724/Login/signup1/')


def verify(request):
    username=request.POST["username"]
    password=request.POST["password"]
    key,call=verify_user(username,password)
    if(key==1):
        bp.text_to_speech().play_text(call)
        return render(request,'home_screen1.html',{'call_name':call})
    else:
        return HttpResponseRedirect('http://127.0.0.1:5724/Login/')


def reset_password(request):
               password=request.POST['password']
               obj=bp.connect_backend()
               query="UPDATE USER_DATA SET password='"+password+"' WHERE email='"+sample.email+"'"
               obj.cursor.execute(query)
               obj.connection.commit()
               obj.connection.close()
               return HttpResponseRedirect('http://127.0.0.1:5724/Login/')


def signup_screen1(request):
    return render(request, 'signup_screen1.html')

def signup_screen2(request):
    return render(request, 'signup_screen2.html')

def signup_screen3(request):
    return render(request, 'signup_screen3.html')

def signup_screen4(request):
    return render(request, 'signup_screen4.html')





def verify_user(username,password):
        obj=bp.connect_backend()
        retrieved=obj.retrieve_data()
        flag=0
        for i in range(len(retrieved)):
            if('@' in username):
                j=2
            else:
                j=0
            if(username==retrieved[i][j] and flag==0):
                flag=1
                position=i
        if(flag==0):
              return 0,None
        if(flag==1):
            if(password==retrieved[position][1]):
                call=retrieved[position][3]
                return 1,call
            else:
                return 0,None
   