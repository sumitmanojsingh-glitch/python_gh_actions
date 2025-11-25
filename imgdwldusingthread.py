import threading,time,requests
def download(url,name):
    print(f"starting download ffrom{url}")
    resp=requests.get(url)
    print(f"Finished download ffrom{url}, size: {resp.content}")
urls=["https://httpbin.org/image/jpeg",
      "https://httpbin.org/image/png",
      "https://httpbin.org/image/svg"]  
start=time.time()
threads=[]
for url in urls:
    i=0
    t=threading.Thread(target=download,args=(url,f"thread{i+1}")) 
    t.start()
    threads.append(t)
    print(f"current thread: {threading.current_thread().name}")
for t in threads:
    t.join()    
end=time.time()
print(f"All downloads fineshed in {end-start:.2f}seconds")


