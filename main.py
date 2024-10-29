def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = word_count(text)
    chars = char_count(text)
    return wc, chars, book_path

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = len(text.split())
    return words
    
def char_count(text):
    x = text.lower()
    z = x.replace(" ","")
    characters = []
    for letters in z:
        characters.append(letters)
        
    amount={}
    
    for y in range(len(characters)):
        if characters[y] not in amount:
            amount[characters[y]] = 1
        elif characters[y] in amount:
            amount[characters[y]] += 1
    return amount

cons = main()

def report(cons):
    cons = main()[1]
    cons = cons
    print(f"--- Begin report of {main()[2]} ---")
    print(f'{main()[0]} words found in the documents')
    print('')
    for index,letter in enumerate(cons):
     print(f"The '{letter}' character was found {cons[letter]} times")


report(cons)