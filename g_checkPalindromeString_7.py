word = input("Masukan kata: ")
wordLength = len(word)
is_palindrome = True

for i in range(wordLength // 2):
    if word[i] != word[wordLength -1 - i]:
        is_palindrome = False

if is_palindrome:
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")

