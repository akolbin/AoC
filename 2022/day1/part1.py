file1 = open('input.txt', 'r')
calorieSum = 0
maxCalories = 0
lines = file1.readlines()

for line in lines:
    if line != '\n':
        calorieSum += int(line)
    else:
        if calorieSum > maxCalories:
            maxCalories = calorieSum
        calorieSum = 0

print(maxCalories)

