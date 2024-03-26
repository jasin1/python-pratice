task_ids = [1, 2, 3]
task_names = ['Do homework', 'Laundry', 'Pay bills']
task_urgencies = [5, 3, 4]

# for i in range(3):
#   print (f'{task_ids[i]:^12}{task_names[i]:^12}{task_urgencies[i]:^12}')

def create_formatted_records(fmt):
  for i in range(3):
    task_id = task_ids[i]
    name = task_names[i]
    urgency = task_urgencies[i]
    print(f'{task_id:{fmt}}{name:{fmt}}{urgency:{fmt}}')

create_formatted_records('^16')
create_formatted_records('#>16')