class Reverse:
    def __init__(self, text):
        self.text = text
        self.i = len(text) - 1   # start from last character

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < 0:
            raise StopIteration
        ch = self.text[self.i]
        self.i -= 1
        return ch


s = input()

for letter in Reverse(s):
    print(letter, end="")