#count number of digits present in a string
#inp = input("Enter the number of strings: ")
#count = 0
#for x in inp:
#    if x in "1234567890":
#        count = count + 1
#print("The number of digits present in the string is: ", count)


a = "This is computational problem solving"
#Sample string
#print("Original String: ", a)
#print("-"*40)

#len(): returns length of the string
#print("Length of the String is: ", len(a))

#lower(): convert all the characters of the string to lowercase
#print("Lowercase: ", a.lower())

#upper(): convert all the characters of the string to uppercase
#print("Uppercase",a.upper())

#replace(): replace a substring with another substring
#print("Replace: ", a.replace("problem","programming"))

#split(): splits the string into a list of substrings based on a delimiter (space by default)
#print("Split by '0': ", a.split("0"))

#find(): returns the lowest index of the substring if found in the string. If not found, it returns -1
#print("6. Find 'Computational':", a.find("Computational"))
#print(" Find 'solving':", a.find("solving"))

#index(): returns the lowest index of the substring if found in the string. If not found, it raises a ValueError
#print("Index of 'computational':", a.index("computational"))

#isalnum(): similar to find(), but raises error if not found
#print("Index of 'computatinal':", a.index("computational"))
# print(" Index of 'solving':", a.index("solving")) # Uncomment to see error


#isalnum() – True if all characters are alphanumeric (no spaces/symbols)
#print("Is 'Hello123' alphanumeric?:", "Hello123".isalnum())
#print(" Is 'Hello 123' alphanumeric?:", "Hello 123".isalnum())

#isdigit() – True if all characters are digits
#print("Is '123' all digits?:", "123".isdigit())
#print(" Is '123a' all digits?:", "123a".isdigit())

#isnumeric() – True if all characters are numeric (includes unicode digits)
#print("Is '½' numeric?:", "½".isnumeric())
#print(" Is '123' numeric?:", "123".isnumeric())

#islower() – True if all characters are lowercase
#print("Is 'hello' lowercase?:", "hello".islower())
#print(" Is 'Hello' lowercase?:", "Hello".islower())

#isupper() – True if all characters are uppercase
#print("Is 'HELLO' uppercase?:", "HELLO".isupper())
#print(" Is 'Hello' uppercase?:", "Hello".isupper())
#print("-" * 40)
#print("End of String Function Demo ")

#a = "Amrita University"
#print(a)
#print(type(a))
#print(a[3])
#for i in a:
#    print(a)
#print(len(a))
#for i in a:
#     if "rita" not in a:
#         print("absent")
#    else:
#        print("present")
#print(a[2:5])
#print(a[:4])
#print(a[2:])
#print(a[-4:-2])
#print(a.upper())
#print(a.lower())
#b = "Vishwa Vidyapeetham"
#print(b.strip())
#print(a.replace("U","H"))
#print(a.split())