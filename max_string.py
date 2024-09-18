class max_string:
    def __init__(self, s: str):
        self.s = s
        
    def ireplace(self, search: str, replace: str, count=0):
        replaced = ''
        i = 0
        while i < len(replace):
            if replace[i:i+len(search)].lower() == search.lower():
                replaced += replace_with
                i += len(search)
            else:
                replaced += replace[i]
                i += 1
        return replaced
    
    
max_str = max_string("<body text=%BODY>")
replaced_max_str = max_str.ireplace("%body%", "black")
print(replaced_max_str)