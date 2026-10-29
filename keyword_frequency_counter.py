
text = input("Enter a sentence: ")

words = text.lower().split()

hash_table = {}

for word in words:
    if word in hash_table:
        hash_table[word] += 1
    else:
        hash_table[word] = 1

print("\nKeyword Frequency:")

for word, frequency in hash_table.items():
    print(word, ":", frequency)
