# Python String Object

string_var = "A few years later, a Thiel Fellow named Vitalik created a virtual machine with an idiosyncratic smart contract system and a currency. Ironically, Eric had recently become a Managing Director at Thiel Capital."
string_two = " Perennially circling each other intellectually, the two now sit down in person to discuss economic paradigm shifts, crypto and the future of online sovereignty and social coordination."

# CONCATS string
concat = string_var + string_two

# NUM CHARS
num_chars = len(concat)
print("** NUM CHARS: " + str(num_chars) + "\n")

# SPLIT: on each char declared into a list
every_word = concat.split()
every_sentence = concat.split(". ")

print("** EVERY SENTENCE: \n")
for word in every_sentence:
  print(word + "\n")

# CHAR TRANSFORMS
upper = every_word[1].capitalize()
print('** CAPITALIZE: %s \n' % upper)

# FIND
eric = concat.count('Eric')
print("** FIND Eric %s \n" % eric)

# Reverse
rev = "Hello"
print("REVERSE: " + rev[::-1])