import string
import threading
import time
t0= time.time()
texts = open("ebook.txt")
words = texts.read()

# j = string.punctuation
# i = words.strip(j)

# print (i)
worddic ={}

def count (words):
# iterates through words and adds to dictionary as keys if it doesn't already include it

# If word already included in the dictionary the value is incremented by 1
  
  for i in words.split():
          j = string.punctuation
          i = i.strip(j)
          if(worddic.get(i) == None):
                  worddic[i]=1
          else:
                  worddic[i] = worddic[i] + 1


def sort (worddic):
  a = sorted(worddic.items(), key = lambda x: x[1], reverse=True)
  print(a) 

def thread_task(lock):
    lock.acquire()
    count(words)
    sort(worddic)
    lock.release()

lock=threading.Lock()
# creating the threads 
t1 = threading.Thread(target=thread_task, args=(lock,))
t2 = threading.Thread(target=thread_task, args=(lock,))
t3 = threading.Thread(target=thread_task, args=(lock,))
t4 = threading.Thread(target=thread_task, args=(lock,))
t5 = threading.Thread(target=thread_task, args=(lock,))
t6 = threading.Thread(target=thread_task, args=(lock,))
t7 = threading.Thread(target=thread_task, args=(lock,))
t8 = threading.Thread(target=thread_task, args=(lock,))

#starting the threads 
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

#waiting for the locks to finish 
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()


# remove any punctions 
# set value pairs in order from highest to lowest 


times = time.time() - t0
print("Time elapsed: ", times)