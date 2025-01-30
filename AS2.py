def anagrams(st1, st2):
    st1 = ''.join(st1.lower().split())
    st2 = ''.join(st2.lower().split())
    return sorted(st1) == sorted(st2)

st1 = input("Enter the First string:")
st2 = input("Enter the Second string:")
if anagrams(st1, st2):
    print("The given two strings are Anagrams.")
else:
    print("The given two strings are not Anagrams.")