


import os
#os.system('pico2wave -w /home/pi/test.wav "it works"')
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
TRIG=11
ECHO=13
p1=3
p2=5
p3=7
p4=15
p5=19
str=""
str1="12345"
print "Distance processsing"
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(p1,GPIO.OUT)
GPIO.setup(p2,GPIO.OUT)
GPIO.setup(p3,GPIO.OUT)
GPIO.setup(p4,GPIO.OUT)
GPIO.setup(p5,GPIO.OUT)
a=0;
while a<5:
 GPIO.output(TRIG,GPIO.LOW)

 print "waiting for sensor to settel"
 time.sleep(2)

 GPIO.output(TRIG,GPIO.HIGH)
 time.sleep(0.00001)
 GPIO.output(TRIG,GPIO.LOW)
 while GPIO.input(ECHO)==0:
   pulse_start=time.time()
 while GPIO.input(ECHO)==1:
  pulse_end=time.time()
  pulse_duration=pulse_end-pulse_start
  distance=pulse_duration*17150
  distance=round(distance,2)
 if distance>2 and distance <400:
  print "Distance",distance-0.5,"cm"
  if distance<5:
   str+="1"
   GPIO.output(p1,GPIO.HIGH)
   GPIO.output(p2,GPIO.LOW)
   GPIO.output(p3,GPIO.LOW)
   GPIO.output(p4,GPIO.LOW)
   GPIO.output(p5,GPIO.LOW)
   print "1"
   os.system('pico2wave -w /home/pi/test.wav "ooonnneee"')
   os.system('aplay /home/pi/test.wav')

  elif  distance<10:
   str+="2"
   GPIO.output(p1,GPIO.LOW)
   GPIO.output(p3,GPIO.LOW)
   GPIO.output(p4,GPIO.LOW)
   GPIO.output(p5,GPIO.LOW)
   GPIO.output(p2,GPIO.HIGH)
   print "2"
   os.system('pico2wave -w /home/pi/test.wav "twoooo"')
   os.system('aplay /home/pi/test.wav')

  elif distance<15:
   str+="3"
   print "3"

   GPIO.output(p1,GPIO.LOW)
   GPIO.output(p2,GPIO.LOW)
   GPIO.output(p4,GPIO.LOW)
   GPIO.output(p5,GPIO.LOW)

   GPIO.output(p3,GPIO.HIGH)
   os.system('pico2wave -w /home/pi/test.wav "threee"')
   os.system('aplay /home/pi/test.wav')

  elif  distance<20:
   str+="4"
   print "4"
   GPIO.output(p1,GPIO.LOW)
   GPIO.output(p2,GPIO.LOW)
   GPIO.output(p3,GPIO.LOW)
   GPIO.output(p5,GPIO.LOW)
 
   GPIO.output(p4,GPIO.HIGH)
   os.system('pico2wave -w /home/pi/test.wav "fourrrrr"')
   os.system('aplay /home/pi/test.wav')

  else :
   str+="5"
   print "5"
   GPIO.output(p1,GPIO.LOW)
   GPIO.output(p2,GPIO.LOW)
   GPIO.output(p3,GPIO.LOW)
   GPIO.output(p4,GPIO.LOW)
   
 
   GPIO.output(p5,GPIO.HIGH)
   os.system('pico2wave -w /home/pi/test.wav "fiveeeee"')
   os.system('aplay /home/pi/test.wav')

 
 else:
  print "OUT of RANGE"
 
 a=a+1;
print"Enterd is", str
print "pass is", str1
if str==str1:
  print "VALID"
  os.system('pico2wave -w /home/pi/test.wav "it is valid password"')
  os.system('aplay /home/pi/test.wav')

else :
  print "NOT VALID"
  str=""
  
  os.system('pico2wave -w /home/pi/test.wav "is not valid password"')
  os.system('aplay /home/pi/test.wav')


time.sleep(1)
GPIO.output(p1,GPIO.LOW)
GPIO.output(p2,GPIO.LOW)
GPIO.output(p3,GPIO.LOW)
GPIO.output(p4,GPIO.LOW)
GPIO.output(p5,GPIO.LOW)
