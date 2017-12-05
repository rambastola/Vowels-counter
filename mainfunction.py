from count_vowels import *

def main():

    user = input ("To upload file, type 'file', otherwise type 'text' ")
    if user == "text":
        text = input ("Enter your text ")
        text = text.lower()
        counter(text)

    elif user == "file":
        print("Make sure your file is encoded with Latin-US (DOS) ")
        filename = input("Type in your .txt file name ")
        file = open(filename, "r")
        file_counter(file)
    print(letterscount())
main()
