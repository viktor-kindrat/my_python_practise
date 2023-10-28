def palindrome(s):
        """
        Finds all palindrome str
        :type s: str
        :rtype: str
        """
        result = []
        str_length = len(s)

        for key_1, letter in enumerate(s):
            for key_2 in range(key_1 + 1, str_length):
                if letter == s[key_2]:
                    palindrome = s[key_1 : key_2 + 1]
                    result.append(palindrome)

        return result


def select_the_longest_str(consistence):
    """
    Return the longest string in consistence
    """
    the_longest_str = consistence[0]

    for element in consistence:
        if(len(element) > len(the_longest_str)):
            the_longest_str = element
    return the_longest_str


def select_the_longest_palindrome(s):
    """
    Return the longest palindrome in str
    """
    return select_the_longest_str(palindrome(s))


if __name__ == "__main__":
    print(palindrome("babad"))
    print(select_the_longest_str(palindrome("babad")))