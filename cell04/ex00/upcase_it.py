#!/usr/bin/env python3
word = input("Give me a word: ").split()
for i in range(len(word)):
    word[i] = word[i].upper()
    print(word[i], end="")
