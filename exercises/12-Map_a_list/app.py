celsius_values = [-2, 34, 56, -10]

def celsius_to_fahrenheit(celsius):
    # The magic happens here
    farenheit_value = (celsius * 9/5) + 32
    return farenheit_value
  

result = list(map(celsius_to_fahrenheit, celsius_values))

print(result)
