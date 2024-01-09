import string


book_path = "/Users/prashantvgaikar/Documents/workspace/github.com/1729prashant/bookbot/books/"
book_name = "frankenstein.txt"
f_path = book_path + book_name
alphabet_count_dict = dict.fromkeys(string.ascii_lowercase, 0)
document_words = 0


def read_file():
    with open(f_path) as f:
        file_contents = f.read()

    words = file_contents.split()
    document_words = len(words)

    for w in words:
        for a in w.lower():
            if a in alphabet_count_dict:
                alphabet_count_dict[a] += 1
        

def main():
    read_file()
    print(f"--------- Begin Report {book_name} ---------")
    print(f"{document_words} words found in document")
    sorted_by_letter_count_list = sorted(alphabet_count_dict.items(), key = lambda x:x[1], reverse = True)
    sorted_by_letter_count_dict = dict(sorted_by_letter_count_list)
    for k,v in sorted_by_letter_count_dict.items():
        print(f"The '{k}' character was found {v} times ")
    print(f"--------- End Report ---------")


main()