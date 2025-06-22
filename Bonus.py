# Bonus solution (Wasan Alqahtani)
#calculate fehrinhite 
def celsius_to_fahrenheit(celsius):
    '''Write a function 
    that takes a Celsius temperature as an argument and returns 
    the equivalent temperature in Fahrenheit.'''
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit,2)

#calculate celsius
def fahrenheit_to_celsius(fahrenheit):
     '''Write a function that takes a Fahrenheit temperature as an argument and 
     eturns the equivalent temperature in Celsius.'''
     celsius = (fahrenheit - 32) * 5/9
     return round(celsius,2)

def main():
    while True:
        try:
            print("-"*20)
            temperature_string = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
            print("-"*20)
            splited_input=temperature_string.split(" ")
            tempreature_value = splited_input[0]
            unit = splited_input[1].upper()
            #use another try to see if the user enter valid tempreture
            #when convert the string to float it will check if there an error it will raise error
            try:
                tempreture_degree= float(tempreature_value) 
            except Exception:
                 raise ValueError("Invalid value. please use numeric values")
            #check if the unit is valid or not 
            if unit == "F":
                  print(f"Temperature in Celsius: {fahrenheit_to_celsius(tempreture_degree)} C")
                  break 
            elif unit == "C":
                  print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(tempreture_degree)} F")
                  break
            else :
                  raise TypeError(" Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
       #handle the exception           
        except ValueError as e:
            print(e)
        except TypeError as e:
            print (e)
        except Exception as e:
            print(e)
        
        
    


main()
