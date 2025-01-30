txt = input("Enter a string:")
if len(txt)>5 and " " not in txt and 0<int(txt[4])<6:
    print(txt," is valid.")
else:
    print(txt," is invalid.")


