from itertools import permutations
import hashlib

english_words = [
    "apple", "banana", "car", "dog", "elephant",
    "fish", "guitar", "house", "ice", "jungle",
    "king", "lion", "moon", "night", "orange",
    "pencil", "queen", "river", "sun", "tree",
    "umbrella", "violet", "water", "xylophone", "yellow",
    "zebra", "air", "book", "cat", "desk",
    "earth", "fire", "grass", "hat", "island",
    "jacket", "kite", "lake", "mountain", "notebook",
    "ocean", "piano", "quiet", "rose", "sky",
    "train", "unicorn", "volcano", "window", "yoga"
]
#Также поменяйте список на свой

hash = input("Введите ваш хеш: ")

for words in permutations(english_words, 3): #Также смените количество слов при необходимости
    combined = " ".join(words)
    hex_dig = hashlib.sha256(combined.encode()).hexdigest()
    if hex_dig.startswith(hash):
        print("Найдено:", combined, hex_dig)
        break
