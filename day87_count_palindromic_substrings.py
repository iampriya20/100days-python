# Counts all palindromic substrings in a string using center expansion (O(n^2))
def count_palindromic_substrings(s: str) -> int:
    n, total = len(s), 0

    def expand(l: int, r: int) -> int:
        c = 0
        while l >= 0 and r < n and s[l] == s[r]:
            c += 1
            l -= 1
            r += 1
        return c

    for i in range(n):
        total += expand(i, i)       # odd-length centers
        total += expand(i, i + 1)   # even-length centers
    return total

text = input("Enter a string: ")
print("Palindromic substrings:", count_palindromic_substrings(text))
