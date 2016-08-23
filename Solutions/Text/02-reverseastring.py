# Reverse a String - Enter a string and the program will reverse it and print it out.

text = input('Enter a string to reverse: ')

def reverse_text (input_text):
    result=[]
    for i in range(0,len(input_text)):
        result.append(input_text[len(input_text)-i-1])
    return result

print ("".join(reverse_text(text)))
