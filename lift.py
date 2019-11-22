import threading
import time

lift = []
current = 0

def get_input():
    input1 = input()
    lift.append(input1)

    
def increment():
    global current
    current+=1
    time.sleep(2)
    print("Up", current)
    
def decrement():
    global current
    current-=1
    time.sleep(2)
    print("Down", current)
    
def traverse():
    if lift:
        while(True):
            if lift:
                if(current > int(lift[0])):
                    decrement()
                    
                if(str(current) in lift):
                    print("Stop", current)
                    lift.remove(str(current))
                    break
                    
                if(current < int(lift[0])):
                    increment()
    

if __name__ == '__main__':
    print("Enter numbers")
    while(True):
        t1= threading.Thread(target=get_input, name='t1')
        t2= threading.Thread(target=traverse, name='t2')
        t1.start()
        time.sleep(5)
        traverse()
        t2.start()

