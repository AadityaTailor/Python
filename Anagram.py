s1=input("Enter first String: " )
s2=input("Enter Second String: " )

# count1=0
# count2=0

# for i in range(len(s1)):
#     count1+=ord(s1[i])

# for i in range(len(s2)):
#     count2+=ord(s2[i])

# if count1==count2:
#     print(f"{s1} and {s2} are anagram")
# else:
#     print(f"{s1} and {s2} are not anagram")

if sorted(s1)==sorted(s2):
    print(f"{s1} and {s2} are anagram")
else:
    print(f"{s1} and {s2} are not anagram")
