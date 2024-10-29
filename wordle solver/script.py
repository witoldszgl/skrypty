def load_words(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        words = [line.strip().lower() for line in file if line.strip()]
    return words


def filter_words_by_length(words, length):

    return [word for word in words if len(word) == length]


def filter_words_by_known_letters(words, required_letters):

    return [word for word in words if all(letter in word for letter in required_letters)]


def main():
    file_path = 'slowa.txt'
    words = load_words(file_path)
    word_length = int(input("Podaj liczbę liter w słowie: "))
    possible_words = filter_words_by_length(words, word_length) 
    known_letters = input("Podaj znane litery (np. smat): ").lower()
    filtered_words = filter_words_by_known_letters(possible_words, known_letters)
    print("Możliwe słowa:")
    for word in filtered_words:
        print(word)

if __name__ == "__main__":
    main()
