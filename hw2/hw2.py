# This like is a comment.
# This HW2 (Assignment of course MIS 3500)

#
# This HW contains problems from the Book from section 2.3 to 2.8.
# 

# 2.3 Problem
# This problem represents how if can be used to print conditional statements
def function_1():
    grade = int(input("What's your grade? "))
    if grade >= 90:
        print('Congratulations! Your grade of', grade,'earns you A in this course.\n')
        
# Running the function for problem 2.3
function_1()
#--------------------------------------------------------------------------------------------------

# 2.4 Problem
# This problem discusses about the arithmetic operations that can be performed with numbers.
# Operations to be performed: +, -, *, /, //, **
# Operands: Left(27.5) & Right(2)
def function_2():
    left_operand = 27.5
    right_operand = 2
    # Operation (+):
    add_var = left_operand + right_operand
    print('The addition of', left_operand, 'and', right_operand, 'leads to: ',add_var)
    
    # Operation (-):
    sub_var = left_operand - right_operand
    print('The subtraction of', left_operand, 'and', right_operand, 'leads to: ',sub_var)
    
    # Operation (*):
    mult_var = left_operand * right_operand
    print('The multiplication of', left_operand, 'and', right_operand, 'leads to: ',mult_var)
    
    # Operation (/):
    div_var = left_operand / right_operand
    print('The division of', left_operand, 'and', right_operand, 'leads to: ', div_var)
    
    # Operation (//):
    floor_div = left_operand // right_operand
    print('The floor division of', left_operand, 'and', right_operand, 'leads to: ',floor_div)
    
    # Operation (**):
    exp_var = left_operand ** right_operand
    print('The exponential of', left_operand, 'and', right_operand, 'leads to: ', floor_div)
    
# Running the function for problem 2.4
function_2()
#--------------------------------------------------------------------------------------------------

# 2.5 Problem
# This problem is about finding Circumference, Diameter and Area of a Circle.
# Radius = 2 (Provided)
# pi = 3.14159 (Provided)
# The problem will be solved without using math module from python library.
def function_3():
    radius_circle = 2
    pi = 3.14159
    
    # Area of the Circle:
    area_circle = pi * radius_circle ** 2
    print('Area of a Circle of Radius', radius_circle, 'is', area_circle)
    
    # Diameter of the Circle:
    dia_meter = 2*radius_circle
    print('Diameter of a Circle of Radius', radius_circle, 'is', dia_meter)
    
    # Circumference of the Circle:
    circum_ference = 2*pi*radius_circle
    print('Circumference of a Circle of Radius', radius_circle, 'is', circum_ference)
    
# Running the function for problem 2.5
function_3()
#--------------------------------------------------------------------------------------------------
# 2.6 Problem
# This problem is to see if a given integer is odd or even using if conditions.
# We will use remainder operator which will help us see if the integer is odd or even
def function_4():
    int_input = int(input('Please provide an integer to check: '))
    checker = int_input%2
    if (checker == 0):
        print('The integer', int_input, 'is even')
    else:
        print('The integer', int_input, 'is odd')
# Running the function for problem 2.6
function_4()
#--------------------------------------------------------------------------------------------------
# 2.7 Problem
# This problem is to check if 1024 is multiple of 4 and 2 is of 10
# Just like Problem 2.6, we will use remainder operator
def function_5():
    var_1 = 1024
    var_2 = 4
    var_3 = 10
    var_4 = 2
    check_1 = var_1%var_2 # 0 remainder means it is a multiple
    check_2 = var_3%var_4 # 0 remainder means it is a multiple
    if (check_1 == 0):
        print('Yes')
    else:
        print('No')
    
    if (check_2 == 0):
        print('Yes')
    else:
        print('No')

# Running the function for problem 2.7
function_5()
#--------------------------------------------------------------------------------------------------
# 2.8 Problem
# The problem is to print a table showing square and cubes of numbers from 0 to 5
# For this we will use loop
def function_6():
    
    # Below are the functions to generate square and cubes
    def square(i):
        return (i*i)
    def cube(i):
        return (i*i*i)
    
    # Setting the Table Header
    print('The Following is the table:')
    
    # Setting Indexes for the Table:
    print('Number','\t','Square','\t','Cubes')
    
    for i in range(0,5+1):
        print(i,'\t',square(i),'\t',cube(i))

# The function to run the program is as below
function_6()
#--------------------------------------------------------------------------------------------------
# Assignment Ends here:
print('\nAssignment Ends Here')
