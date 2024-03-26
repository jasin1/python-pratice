name = "Homework"
urgency = 5
task = f'Name: {name}; Urgency level: {urgency}'

# print(task)

tasks = ["homework", "laundry", "grocery shopping"]

assert f'First Task: {tasks[0]}' == 'First Task: homework'

scores = [95, 98, 97, 96, 97, 93]

total_score = sum(scores)
subject_count = len(scores)
average_score = total_score / subject_count

summary_text = f'Your Average Score: {average_score}'

print(summary_text)