def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

if __name__ == "__main__":
    print(f"20C is {celsius_to_fahrenheit(20)}F")
    print(f"68F is {fahrenheit_to_celsius(68)}C")
    print(f"10km is {kilometers_to_miles(10)} miles")
    print(f"10 miles is {miles_to_kilometers(10)} km")
