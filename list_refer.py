vec = [3, 4, 5]
vecRefer = [x * 3 for x in vec]
print(vecRefer)

todos = ["Wake Up", "Eating", "Do Homework", "Sleep"]
done = [todo + " Done" for todo in todos if len(todo) > 5]
print(done)