# Removes duplicate words (case-insensitive), keeping the first occurrence and original casing.
text = input("Enter a sentence: ").strip()
seen, out = set(), []
for w in text.split():
    k = w.lower()
    if k not in seen:
        seen.add(k)
        out.append(w)
print(" ".join(out))
