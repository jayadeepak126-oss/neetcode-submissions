class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False
        
        a = []
        characters = {")" : "(", "]" : "[", "}" : "{"}
        

        for i in s:
            if i in characters:
                if a and a[-1] == characters[i]:
                    a.pop()
                else:
                    return False
            else:
                a.append(i)
        return len(a) == 0

        