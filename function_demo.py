

#defining a fucntion
def print_twice(whatever):
    print(whatever)
    print(whatever)


#calling a function
print_twice('Lily answered the question.')



def double(a):
    return 2 * a

result = double(10)
print(result)


#import myabs
from myabs import my_abs

b = -42
# abs_b = myabs.my_abs(b)
abs_b = my_abs(b)
print(abs_b)