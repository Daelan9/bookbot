from stats import word_count

def read_text(path):
    with open(path) as r:
        return r.read()

def count_characters(text):
    unique_letters = {} #create new dictionary to contain single characters
    characters = text.lower() #lowers all characters
    for character in characters: #iterate over all the characters in the book
        if character in unique_letters:
            unique_letters[character] = unique_letters[character] + 1 #adds the character into the dictionary and keeps count
        else:
            unique_letters[character] = 1 #if a character isn't found, start it at 1

    return unique_letters #returns the characters with their counts


def report(text):
    letters = [] # create the empty list
    characters = count_characters(text) #pull dictionary into function
    for character, number in characters.items(): #iterate through the dictionary
        if character.isalpha(): #check to see if its an alphabetic letter
            letters.append((character, number)) #add tuple to empty list
    letters.sort(key=lambda x: x[1], reverse=True) #sort list by second element
    return letters

def print_report(letters, path):
    print(f"--Begin report:{path}--")
    for character,number in letters:
        print(f"The '{character}' was found {number} times")
    print("--End report--")

def main():
    path = "books/frankenstein.txt"
    text = read_text(path)
    words = word_count(text)
    book = count_characters(text)
    letters = report(text)
    print_report(letters, path)
    

if __name__ == "__main__":
    main()

    

