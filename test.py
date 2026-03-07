look_up = input('What software acronym would you like to look up?\m')

found = False
with open('dictionary.py') as file:
    for line in files:
        if look_up in line:
            print(line)
            found = True
            break
        
if not found:
    print('The acronym does not exist')