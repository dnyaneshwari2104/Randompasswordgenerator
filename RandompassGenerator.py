import random
import string
print("Welcome to our Random Password Generator")
def main():
    length=int(input("Enter the Length of password you want :"))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digitD=string.digits
    symbolD=string.punctuation
    combine=lowerD+upperD+digitD+symbolD
    x= random.sample(combine,length)
    password="".join(x)
    print(password)
    main()

main()