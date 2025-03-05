year = input()

while True:
    year = int(year) + 1
    digits_in_year = set(map(int, str(year)))
    if len(digits_in_year) == 4:
        print(year)
        break