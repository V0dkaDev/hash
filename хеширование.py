import hashlib
import random

def hash_string():
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
  #Замените слова в данном списке на те которые вам нужны

    random_words = random.sample(english_words, 3) # Если вам нужна фраза более 3 слов то измените второе значение
    combined_string = ' '.join(random_words)
    
    hash_object = hashlib.sha256(combined_string.encode())
    hex_dig = hash_object.hexdigest()
    
    print(f"\nИсходная строка: {combined_string}")
    print(f"SHA-256 хеш: {hex_dig}")

hash_string()
