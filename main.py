from stats import (get_book_text, num_words, character_repeat, sort_dict)
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filename = sys.argv[1]

print("============ BOOKBOT ============")
print(f"Analyzing book found at {filename}...")
print("----------- Word Count ----------")
num_words(filename)

print("----------- Character Count ----------")

text = get_book_text(filename)
counts = character_repeat(text)
sorted_report = sort_dict(counts)

for entry in sorted_report :
    print(f"{entry['char']}: {entry['num']}")

print("============= END ===============")