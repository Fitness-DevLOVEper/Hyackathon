#this is main frontend
import basepackage as bp
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,RiseInTransition
from kv_helper import *
class Splash_Screen(MDScreen):
     def __init__(self, **kwargs):  
        super().__init__(**kwargs)

class Welcome_Screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def go_next(self):
        self.ids.ussername.focus=False
        self.ids.passw.focus=True
    
    def show_pass(self,checkbox,value):
        if self.ids.passw.password:
            self.ids.passw.password = False
        else:
            self.ids.passw.password = True
    
    def go_to_signup_screen(self):
        self.manager.transition.direction='left'
        self.manager.current='Signup_Screen'
    
    def go_to_forgot_screen(self):
        self.manager.transition.direction='left'
        self.manager.current='Forgot_Screen'
    
    def go_to_login_screen(self):
        backend_obj=bp.connect_backend()#create backend object
        retrieved=backend_obj.retrieve_data()
        username_flag=0
        for i in range(len(retrieved)):
            if('@' in self.ids.ussername.text):
                j=2
            else:
                j=0
            if(self.ids.ussername.text==retrieved[i][j] and username_flag==0):
                username_flag=1
                position=i
        if(username_flag==0):
              Snackbar(text="Invalid Username or Password..",duration=2).open()
        if(username_flag==1):
            if(self.ids.passw.text==retrieved[position][1]):
                self.manager.transition.direction = 'left'
                self.manager.current='Home_Screen'
                bp.text_to_speech().play_text('Welcome'+retrieved[position][3])
            else:
                 Snackbar(text="Invalid Username or Password..",duration=2).open()
        else:
             Snackbar(text="Unexpected Error has Occured",duration=2).open()         


class Signup_Screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current='Welcome_Screen'
    
    def check_valid_email_or_not(self):
        self.flag=0
        backend_obj=bp.connect_backend()
        retrieved=backend_obj.retrieve_data()
        for i in range(len(retrieved)):
                if(self.ids.ussername.text==retrieved[i][2] and self.flag==0):
                   self.flag=1
                   Snackbar(text="User with this email already exists!!",duration=2).open()
                   break
        if(self.flag!=1):
                 self.ids.icon_right_color_focus=(144/255,238/255,144/255)
                 self.manager.transition.direction = 'left'
                 self.manager.current='Signup_Screen2'
                 Signup_Screen.sent=bp.generate_otp.send_otp(self.ids.ussername.text)
                 Signup_Screen.email=self.ids.ussername.text


class Signup_Screen2(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current='Signup_Screen'
    
    def resendotp(self):
        Signup_Screen.sent=bp.generate_otp.send_otp(Signup_Screen.email)

    def verifyotp(self):    
        if(Signup_Screen.sent==int(self.ids.otpreceived.text)):
            self.manager.transition.direction = 'left'
            self.manager.current='Signup_Screen3'
        else:
            Snackbar(text="Invalid OTP",duration=2).open() 

class Signup_Screen3(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current='Signup_Screen2'   

    def verifyuser(self):
        Signup_Screen3.user=self.ids.username.text
        entered=self.ids.username.text
        backend_obj=bp.connect_backend()
        retrieved=backend_obj.retrieve_data()
        username_flag=0
        for i in range(len(retrieved)):
            if(entered==retrieved[i][0]):
                username_flag=1
                Snackbar(text="Username not available",duration=2).open()
                break
        if(username_flag!=1):
          self.manager.transition.direction = 'left'
          self.manager.current='Signup_Screen4'

class Signup_Screen4(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create(self):
          if(self.ids.passw.text!=self.ids.confirmpass.text):
                self.ids.confirmpass.error=True
          else:
              
               self.manager.transition.direction = 'left'
               self.manager.current='Hello_Screen'
               backend_obj=bp.connect_backend()
               data={}
               data['email']=Signup_Screen.email
               data['password']=self.ids.confirmpass.text
               data['user_name']=Signup_Screen3.user
               data['call_name']=self.ids.call_name.text
               backend_obj.insert_user_data(data)

    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current='Signup_Screen3'

class Home_Screen(MDScreen):
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)   

class Forgot_Screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def go_back(self):
         self.manager.transition.direction = 'right'
         self.manager.current='Welcome_Screen'
    def sendotp(self):
      self.flag=0
      backend_obj=bp.connect_backend()
      retrieved=backend_obj.retrieve_data()
      for i in range(len(retrieved)):
          if(self.ids.email.text==retrieved[i][2]):
              self.flag=1
              Forgot_Screen.position=i
      if(self.flag==0):
          Snackbar(text="No such user exists!!",duration=2).open()
      else:
         self.manager.transition.direction = 'left'
         self.manager.current='Forgot_Screen1'
         Forgot_Screen.sent=bp.generate_otp.send_otp(self.ids.email.text)
         Forgot_Screen.email=self.ids.email.text
    
class Forgot_Screen1(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current='Forgot_Screen'

    def verifyotp(self):
        if(int(self.ids.passw.text)==Forgot_Screen.sent):
            self.manager.transition.direction = 'left'
            self.manager.current='Reset_Screen'
        else:
            Snackbar(text="Invalid OTP",duration=2).open() 

class Reset_Screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current='Forgot_Screen1'

    def update(self):
            if(self.ids.passw.text!=self.ids.confirmpass.text):
                self.ids.confirmpass.error=True
            else:
               self.manager.transition.direction = 'left'
               self.manager.current='Hello_Screen2'
               obj=bp.connect_backend()
               query="UPDATE USER_DATA SET password='"+self.ids.confirmpass.text+"' WHERE email='"+Forgot_Screen.email+"'"
               obj.cursor.execute(query)
               obj.connection.commit()
               obj.connection.close()

class Hello_Screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Hello_Screen2(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

sm=ScreenManager(transition = RiseInTransition())
sm.add_widget(Splash_Screen(name='Splash_Screen'))
sm.add_widget(Welcome_Screen(name='Welcome_Screen'))
sm.add_widget(Welcome_Screen(name='Signup_Screen'))
sm.add_widget(Welcome_Screen(name='Login_Screen'))
sm.add_widget(Signup_Screen(name='Signup_Screen2'))
sm.add_widget(Welcome_Screen(name='Home_Screen'))
sm.add_widget(Signup_Screen3(name='Signup_Screen4'))
sm.add_widget(Welcome_Screen(name='Forgot_Screen1'))
sm.add_widget(Welcome_Screen(name='Forgot_Screen2'))
sm.add_widget(Signup_Screen4(name='Hello_Screen'))
sm.add_widget(Reset_Screen(name='Hello_Screen2'))

class Fitness_DevLOVEper(MDApp):
    def build(self):
        return Builder.load_string(kv)
    def on_start(self):
        #for splash screen
        pass
phone=Fitness_DevLOVEper()
phone.run()

