conversion=input("Celsius or Fahrenheit:")
if conversion=='celsius':
    celsius=int(input("Enter celsius:"))
    fahrenheit=(celsius*9/5)+32
    print('Fahrenheit:')
    print(fahrenheit)

if conversion=='fahrenheit':
    fahrenheit=int(input("Enter fahrenheit:"))
    celsius=(fahrenheit-32)*5/9
    print("Celsius:")
    print(celsius)