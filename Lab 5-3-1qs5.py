# Lab 5-3-1 question 5
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

def convert_to_celsius(temperature_fahrenheit):
    """
        Returns the equivalent temperature using the Celsius scale. 

    """
    offeset = 32
    freezing_point = 5 / 9
    return round((temperature_fahrenheit - offeset) * (freezing_point), 1)


cool_temperature = 50
celsius_temperature = convert_to_celsius(cool_temperature)
print(celsius_temperature)
bit_warmer = 51
celsius_temperature = convert_to_celsius(bit_warmer)
print(celsius_temperature)

fahrenheit_temp = 60
celsius_temperature = convert_to_celsius(fahrenheit_temp)
print(celsius_temperature)
