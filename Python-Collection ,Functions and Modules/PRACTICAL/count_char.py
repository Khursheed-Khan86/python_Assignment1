#Counting occurrences of characters in a string using dictionaries.
name="khursheed"
count_char={}
for ch in name:
    if ch in count_char:
        count_char[ch]+=1
    else:
        count_char[ch]=1
print(count_char)        