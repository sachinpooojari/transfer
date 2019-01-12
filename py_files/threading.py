import time
import threading
def cal_sqr(number):
    print ("CALCULATE square ")
    for n in number:
        time.sleep(2)
        print ('square ',n*n)

def cal_cube(number):
    print ("CALCULATE CUBE ")
    for n in number:
        time.sleep(2)
        print ('CUBE',n*n*n)

arr=[2,3,8,9]

t=time.time()
t1=threading.Thread(target=cal_sqr,args=(arr,))
t2=threading.Thread(target=cal_cube,args=(arr,))

t1.start()
t2.start()
t1.join()
t2.join()

print("Done in :",time.time()-t)
print"aLL done "
