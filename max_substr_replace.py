def max_str_replace(a_str: str, a_search: str, a_replace_with) -> str:
    i = 0
    a_str_len: int = len(a_str)
    a_search_len: int = len(a_search)
    replaced = ''
    while i < a_str_len:
        if a_str[i:i+a_search_len] == a_search:
            replaced += a_replace_with
            i += a_search_len
        else:
            replaced += a_str[i]
            i = i+1
    return replaced


print(max_str_replace('Hello world!', 'world', '5'))
