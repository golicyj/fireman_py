def greeting_intro(name = ''):
    print('hello ' + name + '!')

greeting_intro('233')

def string_in_text(string, text):
    return string in text

print(string_in_text('the', 'more then one'))

def sex_welcome(name, gender):
    if gender == 'm':
        print('Hello' + name + 'You look great today!')
        return gender
    elif gender == 'f':
        print('Hello' + name + 'You look so beautofull!')
        return gender
    else:
        print('I never seen the creature like u')
        return gender

user1 = sex_welcome('Jan', 'm')
user1 = sex_welcome('Ania', 'f')
user1 = sex_welcome('Bobo', 'kgs')