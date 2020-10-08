def lengthOfLastWord( s: str) -> int:
    count = 0 
    if len(s)==0:
        return 0
    s=s[::-1]
    for i in range(len(s)):
        if count==0 and s[i]==" ":
            continue
        elif s[i]!=" ":
            count +=1
        elif count !=0 and s[i]==" ": 
            break


    return count
    
s="haosudh oiahwdo asdh oia"
print(lengthOfLastWord(s))
