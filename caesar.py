def alphabet_position(letter):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	if (letter.isupper()):
		# blah blah
		letter = letter.lower()
	index = alphabet.index(letter)
	return index

#letter = 'A'
#print(alphabet_position(letter))


def rotate_character(char, rot):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	if (not(char.isalpha())):
		encrypted = char
	else:
		initial_charindex = alphabet_position(char)
		rotated_index = int(initial_charindex) + rot
		if char.isupper():
			a = True
			char = char.lower()
		else:
			a = False
		if (rotated_index < 26):
			if a == True:
				encrypted = alphabet[rotated_index].upper()
			else:
				encrypted = alphabet[rotated_index]
		else:
			if (a == True):
				encrypted = alphabet[rotated_index % 26].upper()
			else:
				encrypted = alphabet[rotated_index % 26]
	return encrypted

def encrypt(text, rot):
	encrypted = ""
	for char in text:
		encrypted = encrypted + rotate_character(char, rot)
	return encrypted
