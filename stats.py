def get_chars_dict(book):
    text = book.lower()
    count = {}
    
    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return count

def get_word_count(book):
    word_list = book.split()
    return len(word_list)

def sort_chars_dict(chars):
    dict_list = []

    for k in chars:
        dic = {"char" : k, "num" : chars[k]}
        dict_list.append(dic)

    def sort_on(items):
        return items["num"]

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    


