def maximum (ls):
    theBiggest = ls[0];
    for el in ls:
        if el > theBiggest:
            theBiggest = el
    return theBiggest

print(maximum([0, -5.5, 3, 6, 10, 9, 1])) # Expected output: 10