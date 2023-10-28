def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    char_index = {}  # A dictionary to store the most recent index of each character
    start = 0  # The start of the current substring
    max_length = 0  # The length of the longest substring
    
    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)
        print(char_index)
        print(start)
    
    return max_length
print(lengthOfLongestSubstring("aab")) # 2