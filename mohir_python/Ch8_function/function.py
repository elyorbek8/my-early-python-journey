# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:40:09 2024

@author: Elyorbek
"""

# # a simple function

# def greet(name = 'vali'):
#     """ the function that recieves user name and greets """
#     print(f"Assalomu alaykum dear {name.title()}!")
    
# greet(name = 'ali')



# # function with return

# def full_name_creat(f_name, l_name):
#     """ the function that returns full name """
#     full_name = f'{f_name.title()} {l_name.title()}'
    
#     return full_name
# student_1 = full_name_creat('ali', 'valiyev')
# student_2 = full_name_creat('alibekov', 'diyor')

# print(f'Today {student_1} and {student_2} haven been absent!')


# # function with arbitrary argument

# def name_generator(*students):
#     print(students[1].title() + ' was given full ride scholarship!')

# name_generator('ali', 'vali', 'dilshod')


# # function with list and dictionary

# def car_info(company, model, condition, color, year, price):
#     """ the function working with a dictionary """
#     car = {'company':company,
#             'model':model,
#             'condition':condition,
#             'color':color,
#             'year':year,
#             'price':price}
#     return car

# car1 = car_info('tesla', 'model y', 'new', 'grey', 2024, 40_000)
# car2 = car_info('bmw', 'ix1', 'new', 'white', 2023, 85_000)

# cars = [car1, car2]

# print("Cars in our e-shopping store:\n")

# for car in cars:
#     print(car["company"], car['model'],
#           car['condition'], car['color'],
#           car['year'], car['price'])
    

# # range function with a step

# def make_range(bottom, top, step = 1):
    
#     """ make_range function can show numbers in a given range 
#     and can change the step if a user enters it. """
    
#     numbers = []
#     while bottom < top:
#         numbers.append(bottom)
#         bottom += step
#     return numbers

# bottom = int(input('bottom range:'))
# top = int(input('top range:'))
# step = int(input('step:'))

# print(make_range(bottom, top, step))



# function with list and dictionary, using user input

# function
def car_info(company, model, engine_type, color, year, price):
    """ the function working with a dictionary and user input """
    car = {'company':company,
            'model':model,
            'engine_type':engine_type,
            'color':color,
            'year':year,
            'price':price}
    return car

# entering car info
cars = []
while True:
    print('Enter following information:\n')
    company = input("Company: ").lower()
    model = input("Model: ").lower()
    engine_type = input("Engine type: ").lower()
    color = input("Color: ").lower()
    year = input("Year: ")
    price = input("Price: ")
    
    cars.append(car_info(company, model, engine_type, color, year, price))
    
    # asking user whether finish or continue
    quest = input("Would you like to add another car info (Yes/ No)?\n>>>")
    
    if quest.lower() == 'no':
        break
    
# show result
print("\nThese are the cars in our e-shopping store:")
for car in cars:
    print("\nCompany: ", car['company'].title(),
          "\nModel: ", car['model'].title(),
          "\nEngine type: ", car['engine_type'].title(),
          "\nColor: ", car['color'].title(),
          "\nProduced year: ", car['year'],
          "\nPrice: ", car['price'])
    
    
    













        

 










