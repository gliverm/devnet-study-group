schoolClass = {}

while True:
    name = input("Enter the student's name (or type exit to stop): ")
    if name == 'exit':
        break

    score = int(input("Enter the student's score (0-10): "))

    if name in schoolClass:
        schoolClass[name] += (score,)
    else:
        schoolClass[name] = (score,)

for name in sorted(schoolClass.keys()):
    sum = 0
    counter = 0
    for score in schoolClass[name]:
        sum += score
        counter += 1
    print(name, ":", sum / counter)