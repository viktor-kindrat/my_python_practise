def reverseLists (ls):
    res = []
    donor = ls
    for i in range(len(ls)):
        res.append(donor.pop())
    return res

def reverseListsSmart (ls):
    return ls[::-1]

print(reverseLists([1, 2, 3]))
print(reverseListsSmart([1, 2, 3]))