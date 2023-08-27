def find_the_same_elements_in_sets (setA, setB): 
    res = []
    for elA in setA:
        for elB in setB:
            if elA == elB:
                res.append(elA)
    return ", ".join(res)


def find_the_same_elements_in_sets_clever (setA, setB): 
    res = []
    for elA in setA:
        if elA in setB:
            res.append(elA)
    return ", ".join(res)

print("Finded same elements in your sets:", find_the_same_elements_in_sets({"vfdvsdfv", "abcd", "world"}, {"abcd", "cdab", "hello", "world"}))
print("Finded same elements in your sets:", find_the_same_elements_in_sets_clever({"vfdvsdfv", "abcd", "world"}, {"abcd", "cdab", "hello", "world"}))