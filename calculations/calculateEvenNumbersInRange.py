def calculate_sum_of_even_numbers_in_range (a):
    even_sum = 0
    for i in range(a + 1):
        if i % 2 == 0:
            even_sum += i
    return even_sum

print("sum of all even numbers in range 100 is:", calculate_sum_of_even_numbers_in_range(100))