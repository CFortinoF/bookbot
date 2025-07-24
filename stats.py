def get_num_words(text):
    return(len(text.split()))

def get_chars(text):
    chars = {}
    for char in text:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1
    return chars

def sorted_list_of_dictionaries(dict):
    list = []

    for dic in dict:
        if dic.isalpha():
            list.append({"char": dic, "num": dict[dic]})
    
    list.sort(reverse = True, key=lambda dict: dict["num"])

    return list