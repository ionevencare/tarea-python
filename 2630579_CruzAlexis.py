
# Alexis Gabriel Cruz Morales
# 2630579
# group 3 
# python homework
# numeric types and booleans


# in this homework i will use numbers in python
# int is used for whole numbers
# float is used for numbers with decimals
# bool is used for true or false
# comparisons help us make decisions
# checking the input helps avoid errors
# i will solve six different problems
# each problem will have its own tests


# problem 1 temperature converter
# description
# this program changes celsius to fahrenheit and kelvin
# it also checks if the temperature is high
# inputs
# temperature in celsius
# outputs
# fahrenheit kelvin and high temperature
# validations
# the temperature must be a valid number
# kelvin cannot be below zero
# test cases
# normal 25 gives 77 fahrenheit
# border 30 gives high temperature true
# error -300 is not a valid temperature

try:
    temp_c = float(input("Enter celsius: "))
    temp_k = temp_c + 273.15

    if temp_k < 0:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = temp_c >= 30

        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        print("High temperature:", str(is_high_temperature).lower())

except ValueError:
    print("Error: invalid input")

    
# problem 2 work hours and overtime payment
# description
# this program calculates how much a worker earns
# extra hours are paid more than normal hours
# inputs
# hours worked and payment per hour
# outputs
# regular pay overtime pay and total pay
# validations
# hours cannot be negative
# payment per hour must be greater than zero
# test cases
# normal 45 hours at 100 gives 4750
# border 40 hours at 100 gives 4000
# error -5 hours gives invalid input


try:
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5

        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40

        print("Regular pay:", round(regular_pay, 2))
        print("Overtime pay:", round(overtime_pay, 2))
        print("Total pay:", round(total_pay, 2))
        print("Has overtime:", str(has_overtime).lower())

except ValueError:
    print("Error: invalid input")


#
# this program checks if a customer gets a discount
# students seniors or purchases of 1000 get a discount
# the discount is 10 percent
# purchase total student and senio
# discount eligible and final total
# validations
# purchase total cannot be negative
# student and senior answers must be yes or no



try:
    purchase_total = float(input("Enter purchase total: "))
    is_student_text = input("Are you a student YES or NO: ").strip().upper()
    is_senior_text = input("Are you a senior YES or NO: ").strip().upper()

    if purchase_total < 0 or is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
        print("Error: invalid input")
    else:
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        discount_eligible = is_student or is_senior or purchase_total >= 1000

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print("Discount eligible:", str(discount_eligible).lower())
        print("Final total:", round(final_total, 2))

except ValueError:
    print("Error: invalid input")



# problem 4
# description
# this program works with 3 numbers
# inputs
# 3 numbers
# outputs
# sum average max min and even
# validations
# only whole numbers
# tests
# normal 2 4 6
# border 0 0 0
# error 2 hi 6


try:
    n1 = int(input("number 1: "))
    n2 = int(input("number 2: "))
    n3 = int(input("number 3: "))

    total = n1 + n2 + n3
    average = total / 3
    even = n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0

    print("sum:", total)
    print("average:", round(average, 2))
    print("max:", max(n1, n2, n3))
    print("min:", min(n1, n2, n3))
    print("all even:", str(even).lower())

except ValueError:
    print("error: invalid input")




# problem 5
# description
# this program checks if you can get a loan
# inputs
# income debt and credit score
# outputs
# debt ratio and eligible
# validations
# income must be greater than zero
# debt and score cannot be negative
# tests
# normal 10000 2000 700 gives true
# border 8000 3200 650 gives true
# error 0 2000 700 gives invalid input



try:
    income = float(input("income: "))
    debt = float(input("debt: "))
    score = int(input("credit score: "))

    if income <= 0 or debt < 0 or score < 0:
        print("Error: invalid input")
    else:
        ratio = debt / income
        eligible = income >= 8000 and ratio <= 0.4 and score >= 650

        print("Debt ratio:", round(ratio, 2))
        print("Eligible:", str(eligible).lower())

except ValueError:
    print("Error: invalid input")




# problem 6
# description
# this program calculates bmi
# inputs
# weight and height
# outputs
# bmi and weight category
# validations
# weight and height must be greater than zero
# tests
# normal 70 1.75 gives normal true
# border 25 1 gives overweight true
# error 70 0 gives invalid input



try:
    weight = float(input("weight: "))
    height = float(input("height: "))

    if weight <= 0 or height <= 0:
        print("Error: invalid input")
    else:
        bmi = weight / (height * height)

        underweight = bmi < 18.5
        normal = 18.5 <= bmi < 25
        overweight = bmi >= 25

        print("BMI:", round(bmi, 2))
        print("Underweight:", str(underweight).lower())
        print("Normal:", str(normal).lower())
        print("Overweight:", str(overweight).lower())

except ValueError:
    print("Error: invalid input")


# conclusions
# i learned how to use int and float
# i learned how true and false work
# i used if to make decisions
# i learned how to use and or and not
# checking numbers helps avoid errors
# these problems helped me practice python



# references
# 1 python docs built in types
# 2 python docs input and output
# 3 python docs control flow
# 4 w3schools python operators
# 5 w3schools python data types


