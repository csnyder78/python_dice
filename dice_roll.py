import numpy as np

def roll(n):
   dx = int(int(input("How many sided dice?" )))
   for i in range(n):
      print(np.random.randint(1, [dx]))
def greet():    
     dice = int(input("Hello friends, how many dice? "))
     for j in range(1):
        roll(dice)
greet()
