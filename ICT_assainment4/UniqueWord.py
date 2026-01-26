print("Enter a sentance: ")
d = input()

w = d.split()
uni_w = set(w)
print("Number of unique words ", len(uni_w))