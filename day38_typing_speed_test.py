# day38_typing_speed_test.py

import time

print("⌨️ Typing Speed Test")

# Fixed sentence for simplicity
sentence = "Typing speed tests help improve accuracy."
print(f"\nType this sentence:\n\n👉 {sentence}\n")

input("Press Enter when you're ready...")
start = time.time()

typed = input("\nStart typing: ")
end = time.time()

# Calculate time and speed
time_taken = end - start
words = len(sentence.split())
wpm = (words / time_taken) * 60

# Accuracy calculation (character-wise)
correct = 0
for i in range(min(len(sentence), len(typed))):
    if sentence[i] == typed[i]:
        correct += 1

accuracy = (correct / len(sentence)) * 100

# Display results
print(f"\n⏱️ Time taken: {time_taken:.2f} seconds")
print(f"⚡ Typing Speed: {wpm:.2f} WPM")
print(f"🎯 Accuracy: {accuracy:.2f}%")
