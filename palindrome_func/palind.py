def palindrome():
    input_1=input("enter the values:")
    x=str(input_1).replace(" ","")

    y=x[::-1]
    if x ==y:
        print("it is palindrome:")
    else:
        print("not a palindrome:")
    return y
print(palindrome())