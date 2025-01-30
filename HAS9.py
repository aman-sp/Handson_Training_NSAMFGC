def pattern(pattern: str, wrd: str) -> bool:
    wrd_list=wrd.split()
    if len(pattern)!=len(wrd_list):
        return False
    ch_to_wrd={}
    wrd_to_ch={}
    for ch, wrd in zip(pattern, wrd_list):
        if ch in ch_to_wrd:
            if ch_to_wrd[ch] != wrd:
                return False
        else:
            ch_to_wrd[ch] = wrd
        
        if wrd in wrd_to_ch:
            if wrd_to_ch[wrd] != ch:
                return False
        else:
            wrd_to_ch[wrd] = ch
    return True

pattern1 = "abba"
wrd = "dog cat cat dog"
print(pattern(pattern1, wrd)) 


