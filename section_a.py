# section A(a)i
def calculateGrades():

    print("\n...Student Grade Calculations...")

    #student marks
    mark = int(input('Enter mark scored:\t'))
    
    #testing marks
    if mark>=90 and  mark<=100:
        print("Grade is A")

    elif mark>=80 and mark<=89:
        print("Grade is B")

    elif mark>=70 and mark<=79:   
        print("Grade is C") 

    elif mark>=60 and mark<=69:   
        print("Grade is D")   

    elif mark>=50 and mark<=59:   
        print("Grade is E")  

    else:
        print("Fail")  


#calling function
calculateGrades()        


#(ii)
#converting temperatures to and from celsius and fahrenheit.
def temperatureConvertions():

    print("Temperature Converting")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius ")

    option = int(input("Select your number of choice (1 or 2): "))

    if option == 1:
        celsius =  float(input("Enter temperature in Celsius Degrees: "))
        fahrenheit  = (9/5 * celsius) + 32
        print(f"{celsius}° C is equal to {fahrenheit}°F")

    elif option == 2:
        fahrenheit =  float(input("Enter temperature in Fahrenheit Degrees: "))
        celsius  = 5/9 * (fahrenheit -32 )
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid option!") 


temperatureConvertions()



# (b)(i)
# using afunction and variables entered from the keyboard
# calculating the area of a triangle

def areaOfTriangle():

    base = int(input('\nEnter the base of the triangle: '))
    height = int(input('Enter the height of the triangle: '))

    area = (1/2) * base * height

    print(f"The area of a triangle of base {base} and height {height} is {area:.2f}")
def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area


# (b)(ii)
# sum of all the numbers in a list.
# using looping.

def sum_list_numbers(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Sampling list
sample_list = [9, 2, 3, 5, 8]

# Calling the function with the sample list
result = sum_list_numbers(sample_list)
print("Sum of the numbers in the list:", result)















