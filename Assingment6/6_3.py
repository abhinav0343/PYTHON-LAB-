class Converter:
    conversion_rates = {
        "inches": 0.0254,
        "feet": 0.3048,
        "yards": 0.9144,
        "miles": 1609.34,
        "kilometers": 1000,
        "meters": 1,
        "centimeters": 0.01,
        "millimeters": 0.001
    }
  #dicionary with the values of units in meters
    def __init__(self, length, unit):
        unit = unit.strip().lower() 
        if unit not in self.conversion_rates:
            print("\nInvalid unit! Choose from: inches, feet, yards, miles, kilometers, meters, centimeters, millimeters.")
            self.length_meters = None
        else:
            self.length_meters = length * self.conversion_rates[unit]  

    def convert_to(self, target_unit):
        target_unit = target_unit.strip().lower()
        if target_unit not in self.conversion_rates:
            print("\nInvalid target unit! Choose a valid unit from the list.")
            return None
        return self.length_meters / self.conversion_rates[target_unit] if self.length_meters is not None else None

unit = input("Enter the original unit: ")
num = float(input("Enter the value: "))
target_unit = input("Enter the unit to convert to: ")
c = Converter(num, unit)  
result = c.convert_to(target_unit)  
if result is not None:
    print(f"{num} {unit} is equal to {result:.4f} {target_unit}")
