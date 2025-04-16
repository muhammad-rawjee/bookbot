def word_count(text):
    word_list = text.split()
    print(f"Found {len(word_list)} total words")

def char_count(text):
    count_dict = {}
    for char in text:
        count_dict[char.lower()] = 1 + count_dict.get(char.lower(), 0)
    return count_dict

def sort_on(dict):
    return dict["count"]

def sort_dict(some_dict):
    dict_list = []
    # populate dict_list
    for k, v in some_dict.items():
        dict_item = {}
        dict_item["char"] = k
        dict_item["count"] = v
        dict_list.append(dict_item)
    # sort dict list
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

# print(sort_dict({"a":20, "b":200}))
