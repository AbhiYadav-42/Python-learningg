
censored_words = [
    "fuck", "sexy","bitch", "boobs", "ass", "dick", "shit", "cunt",
    "porn", "sex", "nude", "xxx", "escort",
    "kill", "murder", "shoot", "bomb", "stab",
    "weed", "cocaine", "meth", "heroin"
]



text =f.read()
with open("abusive.txt", "w") as f:
  for i in censored_words:
    text = text.replace(i,"*"*len(i))
  f.write(text)
  
print(text)