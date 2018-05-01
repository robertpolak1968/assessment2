import getpass
import datetime
import os

print ("Welcome",getpass.getuser()+",")
print ("Another Beautiful Day !!!")
print ()
now = datetime.datetime.now()
print ("Current date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
print ()
cwd = os.getcwd()
print ("Current diretory : ", cwd)
print ("Demo Travis")
