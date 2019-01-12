import thread
import time


import calendar
cal = calendar.month(2008, 1)
print cal





def gps(msg):
  list = ['pos1', 'pos2', 'pos3', 'pos4','pos5','pos6','pos7' ];
  a=0
  b=0
  while a<5:
   #def get( str ):
   time.sleep(1)
   t= time.asctime( time.localtime(time.time())) 
    
 
  

   if (msg<7):
    if (b<7):
     print "Yourstudent in ",list[b]
     print "   at time ",t
     b=b+1
    
     if (b==7):
      b=0
   else:
     print "NOT VALId"
   a=a+1
     
try:
 msg=input("enter 1 to know location ");
 thread.start_new_thread( gps, (msg, ) )
except:

  print "Error: unable to start thread"
#while 1:
 #pass
