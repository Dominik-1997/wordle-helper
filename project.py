# global variables

possible_words = []
words_to_remove = []


def main():
    open_file()
    loop()


def open_file():
    global possible_words
    f = open("words.txt")
    for i in f:
        possible_words.append(i)
    # possible_words.reverse()


def input_word():  # input validation
    word = str(input("What is your word?: "))
    inputted_word = []
    for letter in word:
        inputted_word.append(letter)
    return inputted_word


def input_errors():
    try:
        errors = input("And what are your errors?: ")
    except ValueError:
        print("excpected 5 numbers")
        quit()
    if len(errors) != 5:
        print("excpected 5 numbers")
    inputted_error = []
    for error in errors:
        inputted_error.append(error)
    return inputted_error


def loop():
    print("1 = good letter but bad position, 2 = good good, 0 = bad bad ")
    while True:
        word = input_word()
        errors = input_errors()

        helper(word, errors)

        for i in possible_words:
            print(i)

        if errors == ["2", "2", "2", "2", "2"]:
            print("Congratulations!")
            break


def helper(word, errors):
    y = 0
    global possible_words

    # test sequence
    # word = ["a", "d", "i", "e", "u"]
    # errors = [0, 0, 0, 0, 0]
    # output: story 486

    for i in errors:

        if int(i) == 0:
            for j in possible_words:
                if str(word[y]) in j:
                    words_to_remove.append(j)

        elif int(i) == 1:
            for k in possible_words:
                if str(word[y]) == k[y]:
                    words_to_remove.append(k)
            for m in possible_words:
                if str(word[y]) not in m:
                    words_to_remove.append(m)

        elif int(i) == 2:
            for n in possible_words:
                if word[y] != n[y]:
                    words_to_remove.append(n)

        y = y + 1

    possible_words = [
        word for word in possible_words if word not in words_to_remove]

    return possible_words
    # enumerate_possible = enumerate(possible_words)
    # for count, item in enumerate_possible:
    #     return item, count

    # for item in range(10):
    #     print(possible_words[item])


if __name__ == "__main__":
    main()
