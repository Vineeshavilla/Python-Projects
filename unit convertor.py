def unit_converter(value, from_unit, to_unit):
    conversions = {
        'meters': {'meters': 1, 'kilometers': 0.001, 'miles': 0.000621371},
        'kilometers': {'meters': 1000, 'kilometers': 1, 'miles': 0.621371},
        'miles': {'meters': 1609.34, 'kilometers': 1.60934, 'miles': 1},
    }

    if from_unit in conversions and to_unit in conversions[from_unit]:
        converted_value = value * conversions[from_unit][to_unit]
        return converted_value
    else:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

def main():
    print("Unit Converter")
    print("Available units: meters, kilometers, miles")
    
    try:
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from: ").lower()
        to_unit = input("Enter the unit to convert to: ").lower()

        converted_value = unit_converter(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {converted_value} {to_unit}.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
