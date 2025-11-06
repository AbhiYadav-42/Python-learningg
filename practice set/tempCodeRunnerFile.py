censored_words = [
    "fuck", "sexy","bitch", "boobs", "ass", "dick", "shit", "cunt",
    "porn", "sex", "nude", "xxx", "escort",
    "kill", "murder", "shoot", "bomb", "stab",
    "weed", "cocaine", "meth", "heroin"
]

with open("abusive.txt") as f:
  content = f.read()

def censor(text, censored_words):
  for word in censored_words:
    text=text.replace(word, "*" *len(word))
  return text


print(content)