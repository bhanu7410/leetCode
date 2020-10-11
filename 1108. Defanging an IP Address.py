class Solution:
    def defangIPaddr(self, address: str) -> str:
        if address == "":
            return ""
        final_add=""
        for i in address :
            if i==".":
                final_add+="["
                final_add+=i
                final_add+="]"
            else:
                final_add+=i
        return final_add