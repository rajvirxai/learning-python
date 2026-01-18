# Cricket Score

num = int(input("Enter number of betters batted: "))
scores = []

for i in range(num):
    score = int(input(f"Enter the score batter no {i+1}: "))
    scores.append(score)

total = 0
highest = scores[0]  # assuming that the first value is highest
lowest = scores[0]   # assuming that the first value is lowest

for score in scores:
    total += score
    if score > highest:
        highest = score

    if score < lowest:
        lowest = score
print(f"Total runs scored is: {total}")
print(f"The highest score is: {highest}")
print(f"The lowest score is: {lowest}")
