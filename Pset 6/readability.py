from cs50 import get_string

text = get_string("Text: ")

#
letterscount = 0
wordscount = 1
sentencecount = 0
index = 0
lettersper100 = 0
sentenceper100 = 0

for i in range(len(text)):
    if text[i].isalpha():
        letterscount += 1

    elif text[i].isspace():
        wordscount += 1

    elif text[i] == '?' or text[i] == '.' or text[i] == '!':
        sentencecount += 1

# print(letterscount, wordscount, sentencecount)
lettersper100 = (letterscount * 100) / wordscount
sentenceper100 = (sentencecount * 100) / wordscount

# Use Cole-Liau formula to find the grade
index = round(0.0588 * lettersper100 - 0.296 * sentenceper100 - 15.8)

if index < 1:
    print("Before Grade 1")

elif index >= 16:
    print("Grade 16+")

else:
    print(f"Grade {index}")
