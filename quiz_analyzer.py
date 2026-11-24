scores = []
scores.append(int(input("Enter the first quiz score:  ")))
scores.append(int(input("Enter the second quiz score:  ")))
scores.append(int(input("Enter the third quiz score:  ")))
scores.append(int(input("Enter the fourth quiz score:  ")))
scores.append(int(input("Enter the fifth quiz score:  ")))

avg = sum(scores) / len(scores)


print(f"All Scores: {scores}")
print(f"Total Quizzes: {len(scores)}")
print(f"Average Scores: {avg:.2f}")
print(f"Lowest Score: {min(scores)}")
print(f"Highest Score: {max(scores)}")