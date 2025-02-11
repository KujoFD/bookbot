with open("books/frankenstein.txt") as f:
    file_contents = f.read()
word_count = len(file_contents)
lowered = file_contents.lower()
counts = {}
for char in lowered:
    if char in counts:
        counts[char] +=1
    else:
        counts[char] = 1
print("--- Begin report of books/frankenstein.txt")
print (f"{word_count} words found in the document")
for char in counts:
    if char.isalpha():
        print(f"The '{char}' character was found {counts[char]} times")