def longestCommonPrefix(inn):        
    if len(inn)==0 :
        return ""
    shortest = min(inn,key=len)
    for i, ch in enumerate(shortest):
        for other in inn:
            if other[i] != ch:
                return shortest[:i]
    return shortest

strs=["future","futel","futanari"]
print(longestCommonPrefix(strs))