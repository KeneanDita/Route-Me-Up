n = int(input())  # number of words

for _ in range(n):
    word = input()
    if len(word) > 10:
        abbreviation = f"{word[0]}{len(word) - 2}{word[-1]}"
        print(abbreviation)
    else:
        print(word)
