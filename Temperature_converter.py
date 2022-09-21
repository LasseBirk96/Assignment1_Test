
def convert_celsius_to_fahrenheit(degrees_in_celsius):
        degrees_in_fahrenheit = degrees_in_celsius * 1.8 + 32
        degrees_in_fahrenheit_formatted = float(("{:.2f}".format(degrees_in_fahrenheit)))
        return degrees_in_fahrenheit_formatted

def convert_fahrenheit_to_celsius(degrees_in_fahrenheit):
        degrees_in_celsius = (degrees_in_fahrenheit - 32) * 0.5556
        degrees_in_celsius_formatted = float(("{:.2f}".format(degrees_in_celsius)))
        return degrees_in_celsius_formatted

