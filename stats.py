def word_counter(book_text):
    word_count = len(book_text.split())

    return word_count

def character_counter(book_text):
    words = book_text.split()
    character_count = {}

    for word in words:
        for char in word.lower():
            if char not in character_count:
                character_count[char] = 0
            character_count[char] += 1

    return character_count

def sort_on(items):
    return items["num"]

def sort_characters(char_dict):
    sorted_list = []

    for char in char_dict:
        if char.isalpha():
            sorted_list.append({"char": char, "num": char_dict[char]})

    sorted_list.sort(key=sort_on, reverse=True)

    return sorted_list 
