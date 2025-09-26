#Threads are NOT effective in , 
# High computational tasks, imgae processing , or any high intensive cpu tasks, all because of mutex(GIL)
#Threads are MOST effective in , 
# i/o bound operations , some like , disk read/write , web requests 

#Code to download images from web via web requests using threads.
import threading
import requests
import time

def downloadimage(url):
    print(f"Starting Download from {url}")
    resp = requests.get(url)
    print(f"Finished Downloading from {url} of { len(resp.content) } bytes.")

url = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image",
    "https://httpbin.org/image/svg"
]

start = time.time()

threads = [ ]

for i in url :
    t = threading.Thread(target=downloadimage , args=(url ,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"Time taken : {end-start: .2f} seconds")