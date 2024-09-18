class CMaxString:
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
    
    
max_str = CMaxString("<body text=%BODY>")
replaced_max_str = max_str.ireplace("%body%", "black")
print(replaced_max_str)

# Testing
test_case_seq_number = 1
for test_case in [
    {'string': "<body text=%BODY>", 'search': '%body', 'replace_with': 'black', 'expected': '<body text=black>'},
    {'string': "Hello, Max", 'search': 'max', 'replace_with': 'Serg', 'expected': 'Hello, Serg'},
    {'string': "A match I hope I can find", 'search': 'i ', 'replace_with': 'we ', 'expected': 'A match we hope we can find'},
]:
    aMaxStringInst = CMaxString(test_case['string'])
    if test_case['expected'] == aMaxStringInst.ireplace(test_case['search'], test_case['replace_with']):
        print('Test case {0} passed'.format(test_case_seq_number))
    else:
        print('Test case {0} failed: CMaxString({1}).ireplace("{2}", "{3}") != "{4}"'.format(
            test_case_seq_number, test_case['string'], test_case['search'], test_case['replace_with'], test_case['expected'])
        )
    test_case_seq_number += 1

