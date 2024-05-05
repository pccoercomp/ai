QUESTIONS = [
 "Did the employee meet their deadlines consistently?",
 "Did the employee communicate effectively with their team?",
 "Did the employee demonstrate initiative and problem-solving skills?",
 "Did the employee achieve their set goals and targets?",
 "Did the employee collaborate well with colleagues?",
 "Did the employee handle constructive feedback positively?",
 "Did the employee demonstrate continuous learning and improvement?",
 "Did the employee adhere to company policies and procedures?",
 "Did the employee maintain a positive attitude and work ethic?",
 "Did the employee contribute positively to team morale?",
]
THRESHOLD = {
 "Poor": 20,
 "Fair": 40,
 "Good": 60,
 "Excellent": 80
}
def employeePerformanceEvaluation(questions, threshold):
    score = 0
    for question in questions:
 print(question+" (Y/N) ")
 ans = input("> ")
 if ans.lower() == 'y':
 print('On a scale of 1-10, how would you rate their performance?')
 ip = input('> ')
 while not ip.isnumeric() or int(ip) < 1 or int(ip) > 10:
 print('Enter a valid input !')
 ip = input('> ')
 score += int(ip)
 print("\n\nEmployee Performance Score: ", score)
 print("Performance Evaluation Result:")
 for level, threshold_score in threshold.items():
 if score >= threshold_score:
 print(f"The employee's performance is {level.upper()}.")
 break
 else:
 print("Unable to evaluate the employee's performance.")
if __name__ == '__main__':
 print("\n\n\t\tWelcome To the Employee Performance Evaluation 
System\n")
 print("\tNote : Please answer the following questions honestly.\n\n")
 employeePerformanceEvaluation(QUESTIONS, THRESHOLD)