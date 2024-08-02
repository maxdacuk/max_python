def dict_flip(a_dict: dict) -> dict:
    flipped_dict = {}
    for key in a_dict:
        value = a_dict[key]
        try:
            flipped_dict[value] = key
        except TypeError:
            print(f"Неможна використовувати нехешоване значення {value} як ключ.")
    return flipped_dict

dict3 = {
    'A': 11,
    'C': 'Rem',
    'D': [8]
}

print(dict_flip(dict3))
# {11: 'A', 'Rem': 'C'}
#прочитати що таке 'хеш'
#написати функцію max_key_merge(a_dict: dict, *args) -> dict:
#не використовувати множини

def max_key_merge(a_dict: dict, *args) -> dict:
    result = a_dict.copy()
    for dictionary in args:
        for key, value in dictionary.items():
            if key in result:
                result[key] = max(result[key], value)
            else:
                result[key] = value
    return result

# Приклад використання
dict1 = {'A': 1, 'B': 3}
dict2 = {'A': 2, 'C': 4}
dict3 = {'B': 1, 'D': 5}

merged_dict = max_key_merge(dict1, dict2, dict3)
print(merged_dict)
#{'a': 2, 'b': 3, 'c': 4, 'd': 5}