import getpass,datetime
t=datetime.datetime.now()
class Login:
   def __init__(self,aemail,apass):
      self.email=aemail
      self.pas=apass
   def shu(self):
      rr=getpass.getpass('pass\n')
      sh=open('shukur_login_info.txt','a')
      if User_inp==shukur.email and rr==self.pas:
         sh.write(F"your last login,Date:{t.date()}, Time:{t.time()}")
         sh.close()
         print('Allah')
      elif User_inp==alam.email and rr==self.pas:
         sh.write(F"your last login,Date:{t.date()}, Time:{t.time()}")
         sh.close()
         print(' I love Allah')
      else:
         sh.close()
   @classmethod
   def sty(cls,strt):
      return cls(*strt.split('-'))

shukur=Login.sty('x-y') #x emil
alam=Login.sty('x-y') # x email , y password

User_inp=input('email\n')

if  User_inp == shukur.email:
   shukur.shu()
elif User_inp == alam.email:
   alam.shu()
else:
   pass
