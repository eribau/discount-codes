import random
import string
 
def code_generator(length, n):
   # Define the set of characters that can be used to generate codes
   chars = string.ascii_letters + string.digits
   counter = 0
   
   while counter < n:
      yield''.join(random.choice(chars) for char in range(length))
      counter += 1
 
