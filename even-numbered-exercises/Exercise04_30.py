hexChar = input("Enter a hex character: ").strip()

if hexChar >= '0' and hexChar <= '9':
    print("The decimal value is" , ord(hexChar) - ord('0'))
elif hexChar <= 'F' and hexChar >= 'A':
    print("The decimal value is", ord(hexChar) - ord('A') + 10)
elif hexChar <= 'f' and hexChar >= 'a':
    print("The decimal value is", ord(hexChar) - ord('a') + 10)
else: 
    print(hexChar, "is an invalid input")
