import time

list = ['pos1', 'pos2', 'pos3', 'pos4','pos5','pos6','pos7' ];
a=0
b=0
while a<5:
  time.sleep(1)
  t= time.asctime( time.localtime(time.time())) 
    
 
  
  if (b<7):
     print "Yourstudent in ",list[b]
     print "   at time ",t
     if (b==7):
      b=0
  else:
     print "NOT VALId"
     a=a+1


