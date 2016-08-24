# Binary to Decimal and Back Converter - Develop a converter to convert a decimal number
# to binary or a binary number to its decimal equivalent.

another_round=True

def conv(number,type_of_conv):
        if type_of_conv=="B":
            return bin(number)
        elif type_of_conv=="D":
            return int(str(number),2)
        else:
            conv_type=input("Enter B for decimal to binary conversion or D for binary2decimal: ")
            conv(number,conv_type)

while(another_round):
    input_number=int(input("Please enter a number: "))
    conv_type=input("Enter B for decimal to binary conversion or D for binary2decimal: ")
    print (str(conv(input_number,conv_type)))
    
    if input("for another conversion press y, to abort press any other key: ")!="y":
        another_round=False
    print("----------------------------------------------------------")   

        


    
    
