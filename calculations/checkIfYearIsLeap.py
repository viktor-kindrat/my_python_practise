def check_if_year_leap(year):
    if year % 4 == 0:
        return "Yes"
    else: 
        return "No"

print("Is year 2024 leap:", check_if_year_leap(2024))
print("Is year 2023 leap:", check_if_year_leap(2023))