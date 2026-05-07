print("Welcome to the Word Counter")

text = input("Enter a sentence:")

words = text.split()

word_count = len(words)
character_count = len(text)
character_without_spaces = len(text.replace(" ", ""))
print("Total Words:", word_count)
print("Total Characters:", character_count)
print("Characters Without Spaces:", character_without_spaces)

#Output:
#Welcome to the Word Counter
#Enter a sentence:Python is a simple and popular programming language
#Total Words: 8
#Total Characters: 51
#Characters Without Spaces: 44
