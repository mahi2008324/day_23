a = input("Enter the values to convert Celsius to Fahrenheit (separated by spaces): ").split()

def conversion():
    for i in a:
        celsius = float(i)
        fahrenheit = (celsius * 9/5) + 32
        print("{}°C = {}°F".format(celsius,fahrenheit))

conversion()
