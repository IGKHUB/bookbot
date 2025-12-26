def num_of_words(book):
    with open(book, 'r') as f:
        file_content = f.read()
    words = file_content.split()
    return len(words)

def num_of_characters(book):
    tmp_dict = {}
    with open(book, 'r') as f:
        file_content = f.read()
    for word in file_content.split():
        for char in word.lower():
            tmp_dict[char] = tmp_dict.get(char, 0) + 1
    return tmp_dict

def sorted_count(book):
    tmp_dict = {}
    with open(book, 'r') as f:
        file_content = f.read()
    for word in file_content.split():
        for char in word.lower():
            if char.isalpha():
                tmp_dict[char] = tmp_dict.get(char, 0) + 1
    items = [{'char': k, 'count': v} for k, v in tmp_dict.items()]
    items.sort(key=lambda x: x['count'], reverse=True)
    return items 
    
    


    