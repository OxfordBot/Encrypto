
"""

    Encrypto by Github @OxfordBot (Zavier).
    Written in Python 3.8.6 on Windows 10 Professional.
    Created with permission from NuntCorp.

    (c) Copyright 2021; NuntCorp.

"""

# Import modules

import random
import sys

# Encrypto class

class Encrypto:

    def __init__(self):

        self.alphabets = [
            "a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x",
            "y", "z"
        ]

        self.characters = [
            "a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x",
            "y", "z", "A", "B", "C", "D",
            "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P",
            "Q", "R", "S", "T", "U", "V",
            "W", "X", "Y", "Z", "1", "2",
            "3", "4", "5", "6", "7", "8",
            "9", "0", "!", "@", "#", "$",
            "%", "^", "&", "*", "(", ")",
            "`", "~", "-", "_", "=", "+",
            "{", "}", "[", "]", ";", ":",
            '"', "'", "\\", "|", ",", "<",
            ".", ">", "/", "?", "\n"
        ]

        self.number = 0
        self.add = 0

        self.encodings = {}

        for self.character in self.characters:

            self.add += 1
            self.number += self.add

            self.encodings[self.character] = self.number
            self.encodings[self.number] = self.character

    def generate_key(self, length):

        self.length = length

        self.used_characters = []

        self.key = ""

        while len(self.used_characters) < self.length:

            if random.randint(1, 2) == 1:

                self.alphabet = random.choice(self.alphabets)

                if self.alphabet not in self.used_characters:

                    self.used_characters.append(self.alphabet)

                    self.key += self.alphabet

            else:

                self.number = random.randint(1, 9)
                self.number = str(self.number)

                if self.number not in self.used_characters:

                    self.used_characters.append(self.number)

                    self.key += self.number

        return self.key

    def encode(self, text):

        self.text = text

        self.words = self.text.split(" ")

        self.encoded_text = ""

        for self.word in self.words:

            for self.letter in self.word:

                self.encoded_letter = self.encodings[self.letter]

                self.encoded_text += str(self.encoded_letter)
                self.encoded_text += "-"

            self.encoded_text += "_"

        return self.encoded_text

    def decode(self, text):

        self.text = text

        self.words = self.text.split("_")

        self.decoded_text = ""

        for self.word in self.words:

            self.word = self.word.split("-")

            for self.number in self.word:

                try:

                    self.number = int(self.number)

                    self.decoded_letter = self.encodings[self.number]

                    self.decoded_text += self.decoded_letter

                except:

                    self.decoded_text += ""

            self.decoded_text += " "

        return self.decoded_text

    def read_key(self, key):

        self.key = key

        self.ords = []

        for self.character in self.key:

            self.ord = ord(self.character)
            self.ord = str(self.ord)
            self.ord = self.ord[0:1]

            self.ords.append(self.ord)

        return self.ords

    def encrypt(self, text, key):

        self.text = text

        self.key = key

        self.ords = self.read_key(self.key)

        self.encoded_text = self.encode(self.text)

        while len(self.ords) < len(self.encoded_text):

            self.ords += self.ords

        self.number = 1

        self.encrypted_text = ""

        self.file = open("encrypted.txt", "w")

        for self.character in self.encoded_text:

            self.character_ord = ord(self.character)

            self.ord = self.ords[self.number]
            self.ord = int(self.ord)

            if self.ord < 5:

                self.character_ord += self.ord + self.number - self.ord

            else:
                
                self.character_ord -= self.ord - self.number + self.ord

            self.character_ord = int(self.character_ord)
                
            self.character = chr(self.character_ord)

            self.file.write(self.character)

            self.encrypted_text += self.character

            self.number += 1

        self.file.close()

        return self.encrypted_text

    def decrypt(self, text, key):

        self.text = text

        self.key = key

        self.ords = self.read_key(self.key)

        while len(self.ords) < len(self.text):

            self.ords += self.ords

        self.number = 1

        self.decrypted_text = ""

        for self.character in self.text:

            self.character_ord = ord(self.character)

            self.ord = self.ords[self.number]
            self.ord = int(self.ord)

            if self.ord < 5:

                self.character_ord -= self.ord + self.number - self.ord

            else:

                self.character_ord += self.ord - self.number + self.ord
                
            self.character_ord = int(self.character_ord)

            self.character = chr(self.character_ord)

            self.decrypted_text += self.character

            self.number += 1

        self.decoded_text = self.decode(self.decrypted_text)

        return self.decoded_text
