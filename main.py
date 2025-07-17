from stats import *
import sys

if len(sys.argv) == 1:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    print(file_contents)

def main():
    #get_book_text('/Users/patrykgizdon/github.com/bookbot/books/frankenstein.txt')
    n_words = number_of_words(sys.argv[1])
    dict = count_chars(sys.argv[1])
    list_dict = list_of_dictionaries(dict)
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {n_words} total words')
    print('--------- Character Count -------')
    for item in list_dict:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print('============= END ===============')
main()
