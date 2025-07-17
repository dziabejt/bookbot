# counts numbers of words in file
def number_of_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    list_of_words = file_contents.split()
    n_words = len(list_of_words)
    #print(f'{n_words} words found in the document')
    return n_words

def count_chars (filepath):
    with open(filepath) as f:
        file_contents = f.read()
        lower_content = file_contents.lower()
    counted = {}
    for char in lower_content:
        if char in counted:
            counted[char] += 1
            counted.update({char: counted[char]})
        else:
            counted[char] = 1
    return counted

# function that gives back list of characters used in book
def list_of_dictionaries(dict):
    new_list = list()
    for word in dict:
        new_list.append({"char": word, "num": dict[word]})
    def sort_on(items):
        return items["num"]
    new_list.sort(reverse=True, key=sort_on)
    return new_list
    