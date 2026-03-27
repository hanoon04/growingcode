def helper(day: int, current: int = 1) -> None:
    if current > day:
        print("Harvest time!")
        return
    print(f"Day : {current}")
    helper(day, current + 1)


def ft_count_harvest_recursive() -> None:
    day = int(input("Days until harvest: "))
    helper(day)
