def max_substr_count(aString, needle):
    '''
    The function searches overlapped substring occurences
    '''
    max_count = 0
    needle_len = len(needle)
    
    for i in range(len(aString)):
        if aString[i:i+needle_len] == needle:
            max_count += 1
            
    return max_count

# myStr = 'Good Morning!'
myStr = 'aaaaaaaaaa'
print(max_substr_count(myStr, 'aa'))
