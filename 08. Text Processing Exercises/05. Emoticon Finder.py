text = input()
emot = [text[idx]+text[idx+1] for idx in range(0, len(text)) if text[idx] == ":"]
print(f"\n".join(emot))