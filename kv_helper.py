
kv='''
ScreenManager:
    
    Welcome_Screen:
    Signup_Screen:
    Signup_Screen2:
    Splash_Screen:
    Signup_Screen3:
    Signup_Screen4:
    Home_Screen:
    Forgot_Screen:
    Forgot_Screen1:
    Reset_Screen:
    Hello_Screen:
    Hello_Screen2:
<Splash_Screen>:
    name:"Splash_Screen"
    MDLabel:
        id:label_in_splash_screen
        text:'THIS IS SPLASH SCREEN'
        pos_hint:{'center_x':0.5,'center_y':0.5}
<Welcome_Screen>:    
    name:'Welcome_Screen'
    MDLabel:
        id:'welcometext'
        text:'Welcome to Fitness DevLOVEper '
        font_style:'H4'
        font_name:'hont'
        halign:'center'
        pos_hint:{'center_x':.5,'center_y':.9}   
    MDLabel:
        id:'supporttext'
        text:'The place where you find your virtual trainer :)'
        font_style:'H6'
        halign:'center'
        pos_hint:{'center_x':.5,'center_y':.78}
    MDIcon:
        id:'weightlogo'
        icon:'weight-lifter'
        pos_hint:{'center_x':.83,'center_y':.9}
    MDFillRoundFlatButton:
        id:'signinbutton'
        text: 'Signin'
        font_style:'Subtitle1'
        bold:True
        hailgn:'center'
        md_bg_color:'red'
        pos_hint: {'center_x':0.5,'center_y':0.40}
        on_release:root.go_to_login_screen()
    MDLabel:
        id:"new_user"
        text:'New User? Create your account now'
        halign:'center'
        size_hint:.5,.01
        pos_hint:{'center_x':0.5,'center_y':0.34}    
    MDFillRoundFlatButton:
        id:'signupbutton'
        text: 'Signup'
        font_style:'Subtitle1'
        bold:True
        hailgn:'center'
        md_bg_color:'green'
        pos_hint: {'center_x':0.5,'center_y':0.28}
        on_press:root.go_to_signup_screen()
    MDTextField:
        id:ussername
        focus:False
        hint_text:'Enter your Username or Email id'
        text_color_focus:'black'
        font_name:'Candara.ttf'
        icon_right:'lock'
        font_size:18
        size_hint:.4,.1
        width:250
        pos_hint:{'center_x':0.5,'center_y':0.65}
        mode:"rectangle"
        on_text_validate:root.go_next()
    MDTextField:
        id:passw
        focus:False
        hint_text:'Enter Password'
        text_color_focus:'black'
        font_name:'Candara.ttf'
        font_size:18
        size_hint:.4,.1
        width:250
        pos_hint:{'center_x':0.5,'center_y':0.55}
        password:False
        mode:"rectangle"
        icon_right:'key-outline'
        icon_right_color_focus:(244/255,187/255,41/255,1)
        on_text_validate:root.go_to_login_screen()
    MDCheckbox:
        size_hint:.08,.08
        pos_hint:{'center_x':0.32,'center_y':0.47}
        on_active:root.show_pass(*args)
    MDTextButton:
        text:'forgot password?'
        halign:'center'
        theme_text_color:'Custom'
        text_color:'black'
        pos_hint:{'center_x':0.62,'center_y':0.47}
        on_release:root.go_to_forgot_screen()
    MDLabel:
        id:'passtext'
        text:'Hide password'
        size_hint:(.5,.5)
        theme_text_color:'Custom'
        text_color:'black'
        halign:'center'
        pos_hint:{'center_x':.39,'center_y':.47}

<Signup_Screen>:
    name: 'Signup_Screen'
    MDLabel:
        id:'welcometext'
        text:'You can Join our Family in few steps.. '
        pos_hint:{'center_x':.5,'center_y':.9}
        theme_text_color:'Custom'
        font_style:'H4'
        text_color:'black'
        font_name:'hont'
        halign:'center'
    MDTextField:
        id:ussername
        hint_text:'Enter your Email id'
        color:'black'
        helper_text:"please enter valid email!"
        helper_text_mode:'on_error'
        icon_right:'email'
        text_color_focus:"black"
        size_hint:.5,.1
        width:300
        pos_hint:{'center_x':0.5,'center_y':0.5}
        mode:"fill"
        on_text_validate:root.check_valid_email_or_not()
    MDFillRoundFlatButton:
        id:'nextbutton'
        text: 'next >'
        hailgn:'center'
        md_bg_color:'green'
        bold:True
        pos_hint: {'center_x':0.6,'center_y':0.35}
        on_press:root.check_valid_email_or_not()
    MDFillRoundFlatButton:
        id:'back button'
        text: '< back'
        hailgn:'center'
        bold:True
        md_bg_color:'cyan'
        pos_hint: {'center_x':0.4,'center_y':0.35}
        on_press:root.go_back()
    MDProgressBar:
        size_hint_x:.5
        value:33.33
        pos_hint:{'center_x':.5,'center_y':.28}
        color:0,1,0,1
        back_color:1,0,0,0.5
        
<Signup_Screen2>:
    name: 'Signup_Screen2'
    MDLabel:
        id:'enterotptext'
        text:'please enter OTP that has been sent to your email '
        theme_text_color:'Primary'
        font_style:'H6'
        halign:'center'
        pos_hint:{'center_x':.5,'center_y':.8}
    MDTextField:
        id:otpreceived
        color:'black'
        text_color_focus:'black'
        size_hint:.050,.093
        font_style:'H3'
        width:100
        focus:True
        pos_hint:{'center_x':0.38,'center_y':0.53}
        mode:"rectangle"
    MDFillRoundFlatButton:
        id:'verifybutton'
        text: 'VERIFY'
        hailgn:'center'
        md_bg_color:'green'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press:root.verifyotp()
    MDTextButton:
        id:'resend'
        text: 'Resend OTP'
        hailgn:'center'
        pos_hint: {'center_x':0.31,'center_y':0.41}
        on_press:root.resendotp()
    MDProgressBar:
        pos_hint:{'center_x':.5,'center_y':.26}
        size_hint_x:.5
        value:66.66
        color:0,1,0,1
        back_color:1,0,0,0.5
    MDFillRoundFlatButton:
        id:'back button'
        text: '< back'
        hailgn:'center'
        md_bg_color:'cyan'
        pos_hint: {'center_x':0.5,'center_y':0.32}
        on_press:root.go_back()   

<Signup_Screen3>:
    name: 'Signup_Screen3'
    MDLabel:
        id:'createusername'
        text:'please fill your details '
        pos_hint:{'center_x':.5,'center_y':.8}
        theme_text_color:'Primary'
        font_style:'H6'
        halign:'center'
    MDTextField:
        id:username
        hint_text:'Create Username'
        color:'black'
        size_hint:.5,.1
        width:300
        text_color_focus:'black'
        font_name:'Candara.ttf'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        mode:"rectangle"
    MDFillRoundFlatButton:
        id:'nextbutton'
        text: 'next >'
        hailgn:'center'
        bold:True
        md_bg_color:'green'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press:root.verifyuser()
    MDProgressBar:
        pos_hint:{'center_x':.5,'center_y':.26}
        size_hint_x:.5
        value:83.83
        color:0,1,0,1
        back_color:1,0,0,0.5
    MDFillRoundFlatButton:
        id:'back button'
        text: '< back'
        hailgn:'center'
        md_bg_color:'cyan'
        pos_hint: {'center_x':0.5,'center_y':0.32}
        on_press:root.go_back()
<Signup_Screen4>
    name:'Signup_Screen4'
    MDLabel:
        id:'newpassword'
        text:'Create New Password'
        theme_text_color:'Primary'
        font_style:'H6'
        halign:'center'
        pos_hint:{'center_x':.5,'center_y':.8}
    MDTextField:
        id:call_name
        hint_text:'what should we call you?'
        color:'black'
        text_color_focus:'black'
        font_name:'Candara.ttf'
        size_hint:.5,.1
        width:300
        pos_hint:{'center_x':0.5,'center_y':0.66}
        mode:"rectangle"
    MDTextField:
        id:passw
        hint_text:'Enter New Password'
        color:'black'
        text_color_focus:'black'
        font_name:'Candara.ttf'
        size_hint:.5,.1
        width:300
        pos_hint:{'center_x':0.5,'center_y':0.55}
        mode:"rectangle"
    MDTextField:
        id:confirmpass
        hint_text:'Confirm New Password'
        color:'black'
        text_color_focus:'black'
        font_name:'Candara.ttf'
        helper_text:"Both Passwords Don't Match!!"
        helper_text_mode:'on_error'
        size_hint:.5,.1
        width:300
        pos_hint:{'center_x':0.5,'center_y':0.44}
        mode:"rectangle"
    MDFillRoundFlatButton:
        id:'otpbutton'
        text: 'Proceed'
        hailgn:'center'
        md_bg_color:'green'
        pos_hint: {'center_x':0.5,'center_y':0.35}
        on_press:root.create() 
    MDFillRoundFlatButton:
        id:'back button'
        text: '< back'
        pos_hint: {'center_x':0.5,'center_y':0.28}
        hailgn:'center'
        md_bg_color:'cyan'
        on_press:root.go_back()
<Home_Screen>:
    name:'Home_Screen'
    MDLabel:
        id:'sample'
        text:'This is Home Screen'
        pos_hint:{'center_x':.5,'center_y':.8}
        theme_text_color:'Primary'
        font_style:'H6'
        halign:'center'
<Forgot_Screen>
    name:'Forgot_Screen'
    MDLabel:
        id:'forgotemailtext'
        text:'please enter your details'
        pos_hint:{'center_x':.5,'center_y':.8}
        theme_text_color:'Primary'
        font_style:'H6'
        halign:'center'
    MDTextField:
        id:email
        hint_text:'Enter your email id'
        color:'black'
        text_color_focus:'black'
        font_name:'Candara.ttf'
        size_hint:.5,.1
        width:300
        pos_hint:{'center_x':0.5,'center_y':0.5}
        mode:"rectangle"
    MDFillRoundFlatButton:
        id:'otpbutton'
        text: 'SEND OTP'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        hailgn:'center'
        md_bg_color:'green'
        on_press:root.sendotp()
    MDFillRoundFlatButton:
        id:'back button'
        text: '<  Back'
        pos_hint: {'center_x':0.5,'center_y':0.32}
        hailgn:'center'
        md_bg_color:'cyan'
        on_press:root.go_back()
<Forgot_Screen1>
    name:'Forgot_Screen1'
    MDLabel:
        id:'forgototptext'
        text:'Enter OTP sent to Your mail'
        pos_hint:{'center_x':.5,'center_y':.8}
        theme_text_color:'Primary'
        font_style:'H6'
        halign:'center'
    MDTextField:
        id:passw
        hint_text:'Enter OTP'
        text_color_focus:'black'
        font_name:'Candara.ttf'
        color:'black'
        size_hint:.5,.1
        width:300
        pos_hint:{'center_x':0.5,'center_y':0.5}
        mode:"rectangle"
    MDFillRoundFlatButton:
        id:'otpbutton'
        text: 'VERIFY'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        hailgn:'center'
        md_bg_color:'green'
        bold:True
        on_press:root.verifyotp() 
    MDFillRoundFlatButton:
        id:'back button'
        text: '< back'
        pos_hint: {'center_x':0.5,'center_y':0.32}
        hailgn:'center'
        md_bg_color:'cyan'
        on_press:root.go_back()
<Reset_Screen>
    name:'Reset_Screen'
    MDLabel:
        id:'newpassword'
        text:'Create New Password'
        pos_hint:{'center_x':.5,'center_y':.8}
        theme_text_color:'Primary'
        font_style:'H6'
        halign:'center'
    MDTextField:
        id:passw
        hint_text:'Enter New Password'
        color:'black'
        size_hint:.5,.1
        text_color_focus:'black'
        font_name:'Candara.ttf'
        width:300
        pos_hint:{'center_x':0.5,'center_y':0.55}
        mode:"rectangle"
    MDTextField:
        id:confirmpass
        hint_text:'Confirm New Password'
        color:'black'
        helper_text:"Both passwords don't match!!"
        helper_text_mode:"on_error"
        text_color_focus:'black'
        font_name:'Candara.ttf'
        size_hint:.5,.1
        width:300
        pos_hint:{'center_x':0.5,'center_y':0.44}
        mode:"rectangle"
    MDFillRoundFlatButton:
        id:'otpbutton'
        text: 'Proceed'
        pos_hint: {'center_x':0.5,'center_y':0.32}
        hailgn:'center'
        md_bg_color:'green'
        on_press:root.update() 
    MDFillRoundFlatButton:
        id:'back button'
        text: '< back'
        pos_hint: {'center_x':0.5,'center_y':0.25}
        hailgn:'center'
        md_bg_color:'cyan'
        on_press:root.go_back()
<Hello_Screen>
    name:"Hello_Screen"
<Hello_Screen2>
    name:"Hello_Screen"
'''
