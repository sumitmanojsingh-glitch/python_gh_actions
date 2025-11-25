import threading 
lock=threading.Lock()
counter=0

def increment():

        print(f"Thread : {threading.current_thread().name} is executing")
        global counter
        for i in range(1000000):
            with lock:
                counter+=1

threads=[threading.Thread(target=increment,name=(f"thread{i+1}")) for i in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]
print(f"Final counter : {counter}")

