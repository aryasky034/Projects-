def length_converter(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34,
        'feet': 0.3048,
        'inches': 0.0254
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'grams': 1,
        'kilograms': 1000,
        'pounds': 453.592,
        'ounces': 28.3495
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value  # If units are the same

def main():
    print("Unit Converter")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    choice = input("Choose a conversion type (1/2/3): ")

    if choice == '1':
        value = float(input("Enter value: "))
        from_unit = input("From unit (meters, kilometers, miles, feet, inches): ")
        to_unit = input("To unit (meters, kilometers, miles, feet, inches): ")
        result = length_converter(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")

    elif choice == '2':
        value = float(input("Enter value: "))
        from_unit = input("From unit (grams, kilograms, pounds, ounces): ")
        to_unit = input("To unit (grams, kilograms, pounds, ounces): ")
        result = weight_converter(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")

    elif choice == '3':
        value = float(input("Enter value: "))
        from_unit = input("From unit (Celsius, Fahrenheit, Kelvin): ")
        to_unit = input("To unit (Celsius, Fahrenheit, Kelvin): ")
        result = temperature_converter(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
