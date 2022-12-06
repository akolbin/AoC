file1 = open('input.txt', 'r')
calorieSum = 0
maxCalories = 0
lines = file1.readlines()
topThree = [0, 0, 0]

for line in lines:
    if line != '\n':
        calorieSum += int(line)
    else:
        if calorieSum > topThree[2]:
            topThree[2] = calorieSum
        topThree.sort(reverse=True)
        calorieSum = 0

print(sum(topThree))

