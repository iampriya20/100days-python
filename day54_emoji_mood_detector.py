# Day 54: Emoji Mood Detector

def mood_emoji(word: str) -> str:
    moods = {
        "happy": "😊", "joy": "😄", "smile": "🙂",
        "sad": "😢", "cry": "😭",
        "angry": "😡", "mad": "😠",
        "love": "❤️", "like": "💖",
        "surprised": "😲", "wow": "🤯",
        "tired": "🥱", "sleepy": "😴",
        "sick": "🤒", "cool": "😎",
    }
    return moods.get(word.lower(), "🤔")  # default: thinking/unknown

if __name__ == "__main__":
    w = input("How are you feeling (one word)? ")
    print(mood_emoji(w))
