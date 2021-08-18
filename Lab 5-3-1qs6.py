# Lab 5-3-1 question 7
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

def convert_to_fahrenheit(temperature_celsius):
    """
        Returns the equivalent temperature using the Celsius scale. 

    """
    offeset = 32
    freezing_point = 9 / 5
    return round((temperature_celsius * freezing_point) + offeset, 1)


##cold_temperature = 10
##fahrenheit_temperature = convert_to_fahrenheit(cold_temperature)
##print(fahrenheit_temperature )
##cold_temperature = 11
##fahrenheit_temperature = convert_to_fahrenheit(cold_temperature)
##print(fahrenheit_temperature )
##hot_temperature = 20
##fahrenheit_temperature = convert_to_fahrenheit(hot_temperature)
##print(fahrenheit_temperature )
