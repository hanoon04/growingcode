def ft_water_reminder() -> None:
    nbr_days = int(input("Days since last watering: "))
    if nbr_days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
