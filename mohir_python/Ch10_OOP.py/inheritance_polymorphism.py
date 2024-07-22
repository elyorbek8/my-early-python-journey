# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:36:55 2024

@author: Elyorbek
"""
# Person Class
class Person:
    """ Information about a person """
    def __init__(self, f_name, l_name, b_year, ID_number):
        """ the person's features """
        self.f_name = f_name
        self.l_name = l_name
        self.b_year = b_year
        self.ID_number = ID_number
        
    def get_info(self):
        """ getting information about the person """
        info = f"Full Name: {self.f_name} {self.l_name}"
        info += f" ID number: {self.ID_number} Birth year: {self.b_year}"
        return info
    
    def get_age(self, c_year):
        """ Getting the person's age """
        return c_year - self.b_year

# Student Class
class Student(Person):
    """ Student Class """
    def __init__(self, f_name, l_name, b_year, ID_number, address, university):
        """ Student features """
        super().__init__(f_name, l_name, b_year, ID_number)
        self.university = university
        self.stage = 1
        self.address = address
     
    def get_university(self):
        """ Student's University name """
        return self.university
    def get_stage(self):
        """ Getting student's study stage """
        return self.stage
    
    def get_info(self):
         """ getting information about the person """
         info = f"Full Name: {self.f_name} {self.l_name}, ID number: {self.ID_number}"
         info += f" Birth year: {self.b_year}, University: {self.university}, Stage: {self.stage}"
         return info

# Address Class
class Address:
    """ Address Class """
    def __init__(self, home, street, city, region):
        self.home = home
        self.street = street
        self.city = city
        self.region = region
    
    def get_address(self):
        """ getting address """
        address = f"Home: {self.home}, Street: {self.street}, "
        address += f"City: {self.city}, Region: {self.region}"
        return address
 
# Professor Class    
class Teacher(Person):
    """ Professor Class """
    def __init__(self, f_name, l_name, b_year, ID_number, degree):
        """ Student features """
        super().__init__(f_name, l_name, b_year, ID_number)
        self.degree = degree
        
    def get_info(self):
          """ getting information about the professor """
          info = f"Full Name: {self.f_name} {self.l_name}, ID number: {self.ID_number}"
          info += f" Birth year: {self.b_year}, Degree: {self.degree}"
          return info

teacher1 = Teacher("Ravshan", "Ravshanov", 1970, "AA87654321", "PhD")

student1_address = Address(23, "Mustaqillik", "Tashkent", "Tashkent")
person1 = Person("Sardor", "Doniyorov", 2004, "AA1234567")
student1 = Student("Asadbek", "Juramurodov", 2005, "AB12345678", student1_address, "Stanford")



















    
    