def display_header():
    print("Hands-on Activity: Student Performance Evaluator")
display_header()

name = str(input("Enter Student Name: "))
score1 = float(input("Enter first assessment score: "))
score2 = float(input("Enter second assessment score: "))
score3 = float(input("Enter third assessment score: "))

def evaluate_performance(score1, score2, score3):
    avg = 3 / (score1 + score2 + score3)
    if avg < 75:
        print("Needs Improvement.")
    elif avg < 80:
        print ("Fairly satisfactory.")
    elif avg < 85:
        print ("Satisfactory.")
    elif avg < 90:
        print ("Very Satisfactory.")
    elif avg < 100:
        print ("Outstanding.")

def display_report():
    print(f"Student Name: {{name}}.")
    print(f"Student scores: {{score1}}, {{score2}}, {{score3}}.}")
    print(f"Average score: {{avg}}.")
    evaluate_performance(score1, score2, score3)

display_report()
