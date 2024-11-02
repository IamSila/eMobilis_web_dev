def celsius_to_fahrenheit(celsius: float) -> float:
    """converts degrees celcious to fahrenheit"""
    if not isinstance(celsius, float):
        raise TypeError("celsious must be of type float")
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius: float) -> float:
    """converts degrees celcious to kelvin"""
    if not isinstance(celsius, float):
        raise TypeError("celsious must be of type float")
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """converts farenheight to celcious"""
    if not isinstance(fahrenheit, float):
        raise TypeError("fahrenheight must be a float")
    if fahrenheit < -459.67:
        raise ValueError("Temperature cannot be below absolute zero (-459.67°F).")
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """converts farenheit to kelvin"""
    if not isinstance(fahrenheit, float):
        raise TypeError("Fareinheit must be a float")
    if fahrenheit < -459.67:
        raise ValueError("Temperature cannot be below absolute zero (-459.67°F).")
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin: float) -> float:
    """converts kelvin to celcious"""
    if not isinstance(kelvin, float):
        raise TypeError("Kelvin must of type float")
    if kelvin < 0:
        raise ValueError("Temperature cannot be below absolute zero (0 K).")
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin: float) -> float:
    """converts kelvin to farhenheight"""
    if not isinstance(kelvin, float):
        raise TypeError("Kelvin must of type float")
    if kelvin < 0:
        raise ValueError("Temperature cannot be below absolute zero (0 K).")
    return kelvin * 9/5 - 459.67

"""TESTING THE CODE"""
try:
    print("0°C to Fahrenheit:", celsius_to_fahrenheit(0))
    print("0°F to Kelvin:", fahrenheit_to_kelvin(0))
    print("0 K to Celsius:", kelvin_to_celsius(0))
except ValueError as e:
    print(e)
