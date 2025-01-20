x = {"Sarthak": 5000000, "Ramlal": 32000}
y = {"Ramlal": 5000000, "Oggy": 3200}

z = x | y
# union of both dictionaries meanwhile secondictionary is taken as update if key matches but value doesnt

print(z)


with (
    open("maxVerstappen.txt", "w") as f1,
    open("charlesLeclerc.txt", "w") as f16
):
    f1.write("Here Goes the Max Verstappen\n")
    f1.write("Max Emilian Verstappen is a Dutch and Belgian racing driver, who competes under the Dutch flag in Formula One for Red Bull Racing. Verstappen has won four Formula One World Drivers' Championship titles, which he won consecutively from 2021 to 2024 with Red Bull, and has won 63 Grands Prix across 10 seasons. \n")
    f16.write("Here Goes the Charles Leclerc\n")
    f16.write("Charles Marc Hervé Perceval Leclerc is a Monégasque racing driver, who competes in Formula One for Ferrari. Leclerc was runner-up in the Formula One World Drivers' Championship in 2022 with Ferrari, and has won eight Grands Prix across seven seasons.\n")
