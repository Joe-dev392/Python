while(True):
    print("1.Celsius to Fahrenheit [ (F - 32) * 5/9 ] \n\n2. Fahrenheit to Celcius [ (C * 9/5) + 32 ]\n\n")
    converter = int(input("Select 1 0r 2 for your temperature conversion type\t"));

    def fahrenheit(C):
        print((C * 9/5) + 32)

    def celsius(F):
        print((F - 32) * 5/9 )


    if converter == 1:
        celsius(float(input("Enter °C")))
    elif converter == 2:
        fahrenheit(float(input("Enter °F")))
    else:
        print("Wrong input encountered. Please enter 1 or 2\n\n")
