# votes_obj_arr = []

# TODO: daca sunt mai multe obiecte cu acelasi count ?
votes_obj_arr = [
    { "value": "2", "count": 1, "assignable": 'true' },
    { "value": "1", "count": 1, "assignable": 'true' },
    { "value": "12", "count": 11, "assignable": 'true' },
    { "value": "9", "count": 11, "assignable": 'true' },
    { "value": "2", "count": 11, "assignable": 'true' },
    { "value": "5", "count": 7, "assignable": 'true' },
    { "value": "3", "count": 10, "assignable": 'true' },
    { "value": "7", "count": 11, "assignable": 'true' },
]

highest_vote = None
for vote in votes_obj_arr:
    if highest_vote is None:
        highest_vote = vote
    else:
        if highest_vote['count'] < vote['count']:
            highest_vote = vote
        elif highest_vote['count'] == vote['count'] and int(highest_vote['value']) < int(vote['value']):
            highest_vote = vote

    # print(f'current_max {current_max}')

if highest_vote is None:
    print('No values provided')
else:
    print(highest_vote)
    print(highest_vote['value'])
    