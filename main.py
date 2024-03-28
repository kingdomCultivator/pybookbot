def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        word_count(file_contents)
        print("")
        cdict = char_count(file_contents)
        char_report(cdict)
        print("--- End report ---")

def word_count(book):
    x = book.split()
    print(f"{len(x)} words found in the document")

def char_count(book):
    char_tallies = {}
    for c in book.lower():
        if c not in char_tallies:
            char_tallies[c] = 1
        else:
            char_tallies[c] += 1
    return char_tallies

def char_report(cdict):
    mess = []
    for c in cdict:
        if c.isalpha():
            mess.append({"char": c, "num": cdict[c]})
    mess.sort(reverse=True, key=sort_on)
    for x in mess:
        print(f"The '{x["char"]}' character was found {x["num"]} times")
    

def sort_on(dict):
    return dict["num"]

main()
