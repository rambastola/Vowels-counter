
def counter(user):
    '''
    Count number of vowels that is typed.
    :param user: user's input
    :return:
    '''
    listofvowels = []
    for i in user:
        if i == ("a") or i == ("e") or i == ("i") or i == ("o") or i == ("u"):
            listofvowels.append(i)
    print(" There are ",(len(listofvowels))," Vowels")

def file_counter (file):
    """
    checks for vowels in a .txt file a and prints how many are there.
    :param file:
    :return:
    """
    fileVowels = []
    for lines in file:
        for letters in lines:
            letters = letters.lower()
            if letters == ("a") or letters == ("e") or letters == ("i") or letters == ("o") or letters == ("u"):
                fileVowels.append(letters)
    print(" There are ",(len(fileVowels))," Vowels")

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


main()
