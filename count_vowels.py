listofvowels = []
def counter(user):

    """
    Count number of vowels that is typed.
    :param user: user's input
    :return:none
    """

    for i in user:
        if i == ("a") or i == ("e") or i == ("i") or i == ("o") or i == ("u"):
            listofvowels.append(i)
    print(" There are ",(len(listofvowels))," Vowels")

def file_counter (file):
    """
    checks for vowels in a .txt file a and prints how many are there.
    :param file:
    :return:none
    """

    for lines in file:
        for letters in lines:
            letters = letters.lower()
            if letters == ("a") or letters == ("e") or letters == ("i") or letters == ("o") or letters == ("u"):
                listofvowels.append(letters)
    print(" There are ",(len(listofvowels))," Vowels")

def letterscount():
    """
    count how many of each vowels are there.
    :return: none
    """
    a = 0
    for i in listofvowels:
        if i == "a":
            a += 1
        else:
            continue
    print("There are ", a, " a")
    e = 0
    for i in listofvowels:
        if i == "e":
            e += 1
        else:
            continue
    print("There are ", e, " e")
    i = 0
    for l in listofvowels:
        if l == "i":
            i += 1
        else:
            continue
    print("There are ", i, " i")
    o = 0
    for i in listofvowels:
        if i == "o":
            o += 1
        else:
            continue
    print("There are ", o, " o")
    u = 0
    for i in listofvowels:
        if i == "u":
            u += 1
        else:
            continue
    print("There are ", u, " u")


def main():

    pass

if __name__ == "main":

    main()
