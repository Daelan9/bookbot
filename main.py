def main():
    path = "books/frankenstein.txt"
    text = read_text(path)
    num_words = word_count(text)
    print (num_words)

def read_text(path):
    with open(path) as r:
        return r.read()

def word_count(text):    
    words = text.split()
    return len(words)

if __name__ == "__main__":
    main()

    

