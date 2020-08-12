# Multithreading
##What Is a Thread?
#A thread is a separate flow of execution. This means that your program
# will have two things happening at once. But for most Python 3 implementations
# the different threads do not actually execute at the same time: they merely appear to.

#It’s tempting to think of threading as having two (or more) different
# processors running on your program, each one doing an independent
# task at the same time. That’s almost right. The threads may be running
# on different processors, but they will only be running one at a time.

#Getting multiple tasks running simultaneously requires a non-standard
# implementation of Python, writing some of your code in a different
# language, or using multiprocessing which comes with some extra overhead.

#Because of the way CPython implementation of Python works, threading
# may not speed up all tasks. This is due to interactions with the GIL
# that essentially limit one Python thread to run at a time.

#Tasks that spend much of their time waiting for external events are
# generally good candidates for threading. Problems that require heavy
# CPU computation and spend little time waiting for external events
# might not run faster at all.



#Architecting your program to use threading can also provide
# gains in design clarity. Most of the examples you’ll learn
# about in this tutorial are not necessarily going to run
# faster because they use threads. Using threading in them
# helps to make the design cleaner and easier to reason about



# 1.Creating a thread without using any class
# 2.Creating a thread by using Thread class
# 3.Creating a thread without extending Thread class

####The threading module builds on the low-level features of thread
# to make working with threads even easier and more pythonic. Using threads
# allows a program to run multiple operations concurrently in the same process space.

# from threading import *


# def display():
#     for i in range(10):
#         print("Child Thread")

####The simplest way to use a Thread is to
#### instantiate it with a target function and call start() to let it begin working.
# t = Thread(target=display)
# t.start()
# for i in range(10):
#     print("Main Thread")

#########################################################################

# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             print("Child Thread")
#
# t = MyThread()
# t.start()
# for i in range(10):
#     print("Main Thread")
##############################################################################
# class Test:
#     def display(self):
#         for i in range(10):
#             print("Child Thread")
# obj = Test()
# t = Thread(target=obj.display)
# t.start()
# for i in range(10):
#     print("Main Thread")
#
####################################################

# import time
# def doubles(numbers):
#     for n in numbers:
#         time.sleep(3)
#         print("Double is : ",2*n)
#
# def squares(numbers):
#     for n in numbers:
#         time.sleep(3)
#         print("Square is : ",n*n)
#
# numbers = [1,2,3,4,5,6]
# begtime = time.time()
# doubles(numbers)
# squares(numbers)
# endtime = time.time()
# print("Total time is : ",+endtime-begtime)

#
##################################################################3
#
import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double is : ",2*n)

def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square is : ",n*n)

numbers = [1,2,3,4,5,6]
begtime = time.time()
t1 = Thread(target=doubles,args=(numbers,))
t2 = Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime = time.time()
print("Total time is : ", endtime-begtime)
#
