
# votes_obj_arr = []

# TODO: daca sunt mai multe obiecte cu acelasi count ?
# votes_obj_arr = [
#     { "value": "2", "count": 1, "assignable": 'true' },
#     { "value": "1", "count": 1, "assignable": 'true' },
#     { "value": "12", "count": 11, "assignable": 'true' },
#     { "value": "9", "count": 11, "assignable": 'true' },
#     { "value": "2", "count": 11, "assignable": 'true' },
#     { "value": "5", "count": 7, "assignable": 'true' },
#     { "value": "3", "count": 10, "assignable": 'true' },
#     { "value": "7", "count": 11, "assignable": 'true' },
# ]

current_max = None
for vote in votes_obj_arr:
    if current_max is None:
        current_max = vote
    else:
        if current_max['count'] < vote['count']:
            current_max = vote
        elif current_max['count'] == vote['count'] and int(current_max['value']) < int(vote['value']):
            current_max = vote

    # print(f'current_max {current_max}')

if current_max is None:
    print('No values provided')
else:
    print(current_max)
    print(current_max['value'])
    