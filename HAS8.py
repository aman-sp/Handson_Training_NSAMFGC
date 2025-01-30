def len_of_str(s: str)->int:
    char_set = set()
    left = 0
    length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        length = max(length,right-left+1)
    return length
s = "abcabcbb"
print(len_of_str(s)) 

