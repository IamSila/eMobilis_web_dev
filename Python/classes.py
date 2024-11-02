#!/usr/bin/env python3

class Computer:
    """class to store information about all computers"""
    def __init__(self, name, cpu, ram):
        self.name = name
        self.cpu = cpu
        self.ram = ram

    def info(self):
        """returns information about any instance of this class"""
        return (f"name: {self.name} cpu: {self.cpu} ram: {self.ram}")


"""another class"""
class Car():
    def __init__(self, brand, year, model):
        self.brand = brand
        self.year = year
        self.model = model

    """instance methods"""
    def info(self):
        return (f"{self.model} model belongs to {self.brand}")



car1 = Car("Toyota", 2015, "v8")
print(car1.info())














"""comp1 = Computer("hp", "i7", "8gb")
comp2 = Computer("dell", "i7", "4gb")
print((comp1.info()))
print((comp2.info()))"""