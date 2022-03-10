import string
import random

if __name__ == "__main__":
    # s1 = string.ascii_letters
    # print(s1)
    s2 = string.ascii_lowercase
    # print(s2)
    s3 = string.ascii_uppercase
    # print(s3)
    s4 = string.digits
    # print(s4)
    s5 = string.punctuation
    # print(s5)
    
    # passwordlen = int(input("Enter Password length:\n"))
    while True:
        try:
            passwordlen = int(input("Enter Password length:\n"))
            break
        except ValueError :
            print("Oops! That's not the valid number. Please try again...")
    
    s = []
    s.extend(s2)   # extend--> adds the elements of s2 to list s
    s.extend(s3)   # extend--> adds the elements of s3 to list s
    s.extend(s4)   # extend--> adds the elements of s4 to list s
    s.extend(s5)   # extend--> adds the elements of s5 to list s
    # print(s)     #This gives sorted list 
    
    random.shuffle(s)
    # print(s)     #this gives shuffled list
    
    print("Your password is:")
    print("".join(s[0:passwordlen]))
    
    