
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



