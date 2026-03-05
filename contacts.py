contacts = {
    'number': 4,
    'students' : 
        [
            {'name':'Eren Yeager', 'email':'ereny@example.com'},
            {'name':'Mikasa Ackerman', 'email':'mikasaa@example.com'},
            {'name':'Levi Ackerman', 'email':'levia@example.com'},
            {'name':'Armin Arlert', 'email':'armina@example.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])