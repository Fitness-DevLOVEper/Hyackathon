import smtplib #package for sending email verification
import random#to generate otp
import sqlite3#to have database file
import pyttsx3 # for text to speech
class generate_otp:
    def send_otp(receiver):
        try:
          OTP=random.randint(1000,9999)
          content='''Dear user,we received a request to generate a OTP with your email in fitness guide app.
                      Your Verification code is '''+str(OTP)
          server=smtplib.SMTP('smtp.gmail.com',587)
          server.starttls()
          server.login('feelyourselffit@gmail.com','kmrmqgxduezkpjas')
          server.sendmail('feelyourselffit@gmail.com',receiver,content)
          return OTP
        except:
           print("error occured while sending OTP")
class connect_backend():
    def __init__(self):
        try:
           self.connection=sqlite3.connect("main_db.db")
           self.cursor=self.connection.cursor()
           self.cursor.execute('''CREATE TABLE  IF NOT EXISTS USER_DATA(username srting,password string,email string,call_name string)''')
        except:
            print('error occured while establishing connection with database')
    def insert_user_data(self,data):
        tuplee=(data['user_name'],data['password'],data['email'],data['call_name'])
        insert_query="INSERT INTO USER_DATA VALUES"+str(tuplee)
        self.cursor.execute(insert_query)
        print("record inserted")
        self.connection.commit()
        self.connection.close()
        return 0
    def retrieve_data(self):
        self.cursor.execute('''SELECT * FROM USER_DATA''')
        present_users_data=self.cursor.fetchall()
        self.connection.close()
        return present_users_data#returns list of tuples
    #connection should be closed all activities
class text_to_speech():
    def __init__(self):
        self.obj=pyttsx3.init()
    def play_text(self,text):
        self.obj.say(text)
        self.obj.runAndWait()