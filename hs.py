from kivy.animation import Animation
from kivy.lang import Builder
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition,
SlideTransition, CardTransition,SwapTransition,
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)
from kivymd.uix.screen import MDScreen
from kivymd.uix.chip import MDChip
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.uix.videoplayer import VideoPlayer

class DetailScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def show_bmi(self):
        w=self.ids.weight.text
        h=self.ids.height.text
        if w=="" or h=="":
            self.ids.label.text="Please enter your Height and Weight"

        else:
            bmi=int(w)/(int(h)*0.01)**2
            bmi_2d=round(bmi,2)
            if bmi_2d<=18.5:
                self.ids.label.text="Your BMI is "+str(bmi_2d)+" and you are UNDERWEIGHT"
            elif bmi_2d>18.5 and bmi_2d<=24.9:
                self.ids.label.text="Your BMI is "+str(bmi_2d)+" and your weight is NORMAL"
            else:
                self.ids.label.text="Your BMI is "+str(bmi_2d)+" and your are OVERWEIGHT"

        self.manager.current='DetailScreen'

    def home_screen(self):
        self.manager.current='HomeScreen'

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def dis_bicep(self):
        self.manager.current="BicepScreen"
    def dis_barbell(self):
        self.manager.current="BarbellScreen"

class BicepScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
class BarbellScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


KV = '''

ScreenManager:
    MyScreen:
    DetailScreen:
    HomeScreen:
    BicepScreen
    BarbellScreen


<MyScreen>

    MDBoxLayout:
        orientation: "vertical"
        adaptive_size: True
        spacing: "12dp"
        padding: "56dp"
        pos_hint: {"center_x": .4, "center_y": .8}

        MDLabel:
            text: "Choose your Gender"
            bold: True
            font_style: "H5"
            adaptive_size: True


        MDBoxLayout:
            id: chip_box
            adaptive_size: True
            spacing: "8dp"

            MyChip:
                text: "Male"
                on_active: if self.active: root.removes_marks_all_chips(self)
                icon_left:"human-male"

            MyChip:
                text: "Female"
                on_active: if self.active: root.removes_marks_all_chips(self)
                icon_left:"human-female"


            MyChip:
                text: "Better not to say"
                on_active: if self.active: root.removes_marks_all_chips(self)

        MDLabel:
            text: "Click next to continue"
            bold: True
            markup : True
            font_style: "H5"
            adaptive_size: True
            halign:"center"
            pos_hint:{'center_x':0.32,'center_y':0.6}

        MDFillRoundFlatButton:
            text: 'Next'
            pos_hint: {'center_x':0.32,'center_y':0.2}
            on_press:root.details()

<DetailScreen>:
    name:'DetailScreen'
    MDLabel:
        text: "Let us Know your details for your workouts"
        bold: True
        markup : True
        font_style: "H5"
        adaptive_size: True
        pos_hint:{'center_x':0.32,'center_y':0.9}
    MDTextField:
        id:weight
        input_type: 'number'
        hint_text:'Enter your weight in kgs'
        icon_right:'weight-lifter'
        text_color_focus:'black'
        font_size:18
        size_hint:.4,.1
        width:250
        pos_hint:{'center_x':0.3,'center_y':0.75}
        mode:"rectangle"
    MDTextField:
        id:height
        input_type: 'number'
        hint_text:'Enter your height in cms'
        icon_right:'human-male-height-variant'
        text_color_focus:'black'
        font_size:18
        size_hint:.4,.1
        width:250
        pos_hint:{'center_x':0.3,'center_y':0.65}
        mode:"rectangle"

    MDFillRoundFlatButton:
        text: 'Calculate your BMI'
        pos_hint: {'center_x':0.2,'center_y':0.5}
        on_press:root.show_bmi()

    MDLabel:
        id:label
        text: ""
        markup : True
        #font_style: "H5"
        adaptive_size: True
        pos_hint:{'center_x':0.4,'center_y':0.4}

    MDFillRoundFlatButton:
        text: 'Get to the Plan'
        pos_hint: {'center_x':0.19,'center_y':0.3}
        on_press:root.home_screen()


<HomeScreen>:
    name:'HomeScreen'

    MDBottomNavigation:
        panel_color: "#eeeaea"
        #selected_color_background: "#97ecf8"
        text_color_active: "white"

        MDBottomNavigationItem:
            name: "screen 1"
            text:"Exercise"
            icon: "view-list"
            badge_icon: "numeric-2"
            MDLabel:
                text: "ARM WORKOUTS"
                markup : True
                font_style: "H5"
                adaptive_size: True
                pos_hint:{'center_x':0.5,'center_y':0.9}
            MDCard:
                size_hint: .7, .3
                focus_behavior: True
                pos_hint: {"center_x": .5, "center_y": .7}
                elevation: 2
                style:"filled"
                on_release:root.dis_bicep()
                MDBoxLayout:
                    MDLabel:
                        text: "Bicep Curls"
                        bold: True
                        halign: "center"
                        markup : True
                        font_style: "Button"
                    FitImage:
                        size_hint_x: 1
                        source: 'bicep_img.jpg'    
                
            MDCard:
                size_hint: .7, .3
                focus_behavior: True
                pos_hint: {"center_x": .5, "center_y": .3}
                elevation: 2
                style:"outlined"
                on_release:root.dis_barbell()
                MDBoxLayout:
                    MDLabel:
                        text: "Barbell Curls"
                        bold: True
                        halign: "center"
                        markup : True
                        font_style: "Button"
                    FitImage:
                        size_hint_x: 1
                        source: 'barbell_img.jpg' 

        MDBottomNavigationItem:
            name: "screen 2"
            text: "Activity"
            badge_icon: "numeric-5"
            icon: "all-inclusive-box-outline"
        MDBottomNavigationItem:
            name: "screen 3"
            text: "Account"
            icon: "account-circle"
    
<BicepScreen>:
    name:'BicepScreen'
    Video:
        source:"Bicep_video.mp4"  
        state:"play"
        eos:"loop"
    

<BarbellScreen>:
    name:'BarbellScreen'
    Video:
        source:"Barbell_video.mp4"  
        state:"play"
        eos:"loop"
'''
sm = ScreenManager(transition = SwapTransition())
sm.add_widget(DetailScreen(name='DetailScreen'))
sm.add_widget(HomeScreen(name='HomeScreen'))
sm.add_widget(BicepScreen(name='BicepScreen'))
sm.add_widget(BarbellScreen(name='BarbellScreen'))

class MyChip(MDChip):
    icon_check_color = (0, 0, 0, 1)
    text_color = (0, 0, 0, 0.5)
    _no_ripple_effect = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(active=self.set_chip_bg_color)
        self.bind(active=self.set_chip_text_color)

    def set_chip_bg_color(self, instance_chip, active_value: int):
        '''
        Will be called every time the chip is activated/deactivated.
        Sets the background color of the chip.
        '''

        self.md_bg_color = (
            (0, 0, 0, 0.4)
            if active_value
            else (
                self.theme_cls.bg_darkest
                if self.theme_cls.theme_style == "Light"
                else (
                    self.theme_cls.bg_light
                    if not self.disabled
                    else self.theme_cls.disabled_hint_text_color
                )
            )
        )

    def set_chip_text_color(self, instance_chip, active_value: int):
        Animation(
            color=(0, 0, 0, 1) if active_value else (0, 0, 0, 0.5), d=0.2
        ).start(self.ids.label)


class MyScreen(MDScreen):
    def removes_marks_all_chips(self, selected_instance_chip):
        for instance_chip in self.ids.chip_box.children:
            if instance_chip != selected_instance_chip:
                instance_chip.active = False
    def details(self):
        self.manager.transition.direction='left'
        self.manager.current='DetailScreen'


class Test(MDApp):
    def build(self): 
        return Builder.load_string(KV)

Test().run()