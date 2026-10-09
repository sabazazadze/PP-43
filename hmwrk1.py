text = "Python არის მარტივი, Python არის ძლიერი და Python პოპულარულია."

clean = text.lower().replace(",", "").replace(".", "")
words = clean.split()
print(words)

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
    print(f"{word}: {count}")

top_word = None
top_count = 0
for word, count in counts.items():
    if count > top_count:
        top_word = word
        top_count = count

print(f"ყველაზე ხშირი: '{top_word}' ({top_count}-ჯერ)")

print("==="* 10)

print(f"სხვადასხვა სიტყვა: {len(counts)}")