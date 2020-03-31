# Exercise 5
# It is trying to determine if flag or c.islower is True or False in this particular string

# Exercise 6
def Rotate_word(str_, num_):
    result = ''
    for i in str_:
        i = chr(ord(i) + num_)
        result = result + i
    return (result)

str_ =input("Enter a string: ")
num_ = int(input("Enter rotate number: "))
print (Rotate_word(str_,num_))
