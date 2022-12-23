from mpi4py import MPI
import string
import threading
import time

texts = open("ebook.txt")                   #opens the text file
words = texts.read()                        #reads the text file
worddic ={}                                 #create an empty dictionary 

def count (words):                          #function for word count in text file
    returnd ={}                             #create another empty dictionary
    for i in words.split():                 #For loop to iterate through each word
            j = string.punctuation          #string.punctuation is a built in library that stores all the punctuation !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
            i = i.strip(j)                  #i.strip removes any punctuation as the for loop iterates through each word
            if(returnd.get(i) == None):     # if dictionary doesn't include word set it value to 1
                  returnd[i]=1
            else:                     
                  returnd[i] = returnd[i] + 1 #else if word is already included increment value to 1
    return returnd


def sort (worddic):
  return sorted(worddic.items(), key = lambda x: x[1], reverse=True)    #sorts dictionary from most frequent repeated word to lowest repeated word using built in function called sorted


comm = MPI.COMM_WORLD                 # assign default communicator       
t0= time.time()                       # marks the inital time stamp for that procress
worker = comm.Get_rank()              # gets the current process
size = comm.Get_size()                 # gets the size of the number of processes 
if worker == 0:                         # used broadcasting to send the same message to every worker
    data = words                        # starts first worker that has the first copy of the data. 
else:
    data = None                         #else return none
data = comm.bcast(data, root=0)         #declare type of collective communcation method (broadcasting)

finaldata = sort(count(data))         #calling both 'count' and 'sort' function
times = time.time()                   #marks the second time stamp for that procress

lock=threading.Lock()                  # use threading lock to lock current time stamp and worker for that process

with lock:
    print("Time Elapsed: ", times-t0, "by Worker", worker, finaldata[0:20])
   
