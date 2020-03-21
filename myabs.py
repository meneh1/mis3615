# to create a function that returns the absolute value of any number

def my_abs(number):
  """
   returns the absolute value of any number.
  
  number: an int.
  """
  if number < 0:
    return 0 - number
  else: 
    return number

    
a = -10
abs_a = my_abs(a)
print(abs_a)

# print(my_abs)(-10))






