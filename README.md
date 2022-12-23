# ProgLangWordSort
Programming Language Word Sort
Noel Mathew
Elizabeth Palacios 


Elizabeth Palacios									12/23/22
Noel Mathew
Word Sort Final Project Report

Word Sort Project Description:
The word sortproject aims to input text editor files from (https://www.gutenberg.org/) into our Python3 code. The purpose of the program is to count the number of unique words that have been frequently repeated. This project will use dictionaries, for-loops, and python string functions. During this project we were also able to implement threads and later use mpi4py to then shift it to parallel programming. 

Program Control Flow:
The program starts with an input .txt file, the one we chose was an ebook from www.guternberg.org 
The program then open and scan through the file, this information is then stored in a variable “words”
Then the count function is entered and the “words” are iterated through a for loop, this loop removes the punctuation using the string.punctuation and string.strip functions. Then in an if-else statement, the word is checked to see if it already occurred or if its the first time. The count will then get incremented accordingly. 
Then it flows to the sort function. This function uses the sorted python function to sort through the dictionary that is inputted into this function. As it is “reversed”, when the results are displayed we can see the most frequent words to the least frequent words. 
The next steps implements the mpi4py funtionings. This allows for parallel processing, workers are assigned the processes and the number of processes, then a copy of the “word” data is inputted. Messages are broadcasted to the workers during this process, finally calling both the “count” and “sort” functions and storing it in “finaldata”
Locks are implemented to organize the time stamps by each worker and then the final sorted data is displayed. 
Control Flow Diagram:















Thread Implementations: 
Prior to utilizing the mpi4py, we were using threads. The code that was implemented is as follows:


Tasks were spread from opening the file, reading it, count function and the sort function. The following are the execution times for the threads:
8  → 0.009795427322387695
7 →0.008106708526611328
6 → 0.0072400569915771484
5 → 0.008576154708862305
4 → 0.02951216697692871
3 → 0.049141883850097656
2→ 0.010788440704345703
1 →0.03251504898071289

As seen here, as the thread count decreases the time (seconds) increases. This is due to the split of the processes, as more threads are present the program is able to distribute its functionality synchronously. As the thread count increases though, we can see that the execution time isn’t making a drastic decrease. With a simple program like this, too many threads can sometimes not have efficient results. With the locks we were using, it can cause blocks between threads and priority inversion. Our solution to this was to utilize mpi4py, parallel processing. MPI stands for “Message Passing Interface”, this is very vital with parallel computing architectures as broadcasting messages allows for different workers to communicate. 










With a communicator that spans all the processes of our code and ranks the functions, we eliminate one downside of threads which was priority inversion. Ranks ensure that the most important main functions are executed. This communication of workers allows our program to work seamlessly and efficiently. The execution time for our program utilizing the mpi4py is 0.0476343631744 seconds. 

When all the processes are running simultaneously, we see the range of time elapsed with each worker. This value thus varies with the number of workers implemented. 

Our program outputs the dictionary we stored the word and its respective frequency value in order of most frequent to least frequent. 

Contributions:
In this project we both worked very cooperatively in the code and reports. In the code Elizabeth developed the count and sort code, and the mpi4py functionality. Noel turned these codes into functions and implemented the 8 threads prior. We both wrote the HLD, LLD and Final Report together as well as the final project demonstration video. In this project we learned a lot, we came into this project with questions on how to remove punctuations, using threads, and using mpi4py were just a few. We were able to refer to lectures provided through class to learn about threading processes, parallel threading and multi-process threading. As we began discussions about attempting the bonus we learned more about how we can use mpi4py in this project. This eliminated the use of threading that we initially had in our program. So, we changed the layout of our code to allow for a parallel processing architecture. 
