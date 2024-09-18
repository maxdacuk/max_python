class max_string2:
    def __init__(self, s: str):
        self.s = s
        
    def ireplace(self, search: str, replace: str, count=0):
        replaced = ''
        i = 0
        while i < len(self.s):
            if self.s[i:i+len(search)].lower() == search.lower():
                replaced += replace
                i += len(search)
            else:
                replaced += self.s[i]
                i += 1
        return replaced
    
max_str = max_string2("<body text=%BODY>")
replaced_max_str = max_str.ireplace("%BODY%", "black")
print(replaced_max_str)