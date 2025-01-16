
def Conv(c):
    return (((float(9)/5) * c) + 32)


c = float(input("Enter the Temperature in Celsius: "))
print("Celcius:", c)
print("Faranheit:", Conv(c))
