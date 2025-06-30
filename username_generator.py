import random

def generate_username(include_number = False, format_style='camel'):
    #lists of adjectives and noun
    adjectives = ['Mtai','Elearning','Hyderabad','Innovations','Solutions']
    nouns = ['Forest','Park','Technology','god','Ocean']

    #selects random adjective and nouns fromm the list
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    #if it is true means any number added into the username
    if include_number:
        number= random.randint(1,99)
        username = f"{adjective}{noun}{number}"
    else:
        username = f"{adjective}{noun}" #it will not add any number

    #if format style is exactly world it will convert username to lowercase and replace space to '_'
    if format_style == 'world':
        username = username.lower()
        username = username.replace(' ', '_')
    return username


if __name__ == '__main__':
    print(generate_username(include_number = True,format_style='Solutions'))
    print(generate_username(include_number = False,format_style='Elearning'))
