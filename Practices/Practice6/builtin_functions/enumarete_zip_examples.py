names = ["Arman", "Nurali", "Magzhan"]
scores = [85, 90, 95]


for i, name in enumerate(names): #creates a nested list [[0,name1],[1,name2]...]
    print(i, name)


for name, score in zip(names, scores): #opposite of enumerate, melts together values with the same position
    print(name, score)