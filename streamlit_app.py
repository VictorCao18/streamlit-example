import streamlit as st
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    dollars = (dollars_per_gallon / miles_per_gallon) * miles_driven
    return dollars 

miles_per_gallon = float(input())
dollars_per_gallon = float(input())

miles1 = driving_cost(miles_per_gallon, dollars_per_gallon, 10.0)
miles2 = driving_cost(miles_per_gallon, dollars_per_gallon, 50.0)
miles3 = driving_cost(miles_per_gallon, dollars_per_gallon, 400.0)

print(f'{miles1:.2f}')
print(f'{miles2:.2f}')
print(f'{miles3:.2f}')
