def ft_harvest_total() -> None:
    total = 0
    i = 1
    while i <= 3:
        harvest = int(input(f"Day {i} harvest: "))
        total += harvest
        i += 1
    print(f"Total harvest: {total}")
