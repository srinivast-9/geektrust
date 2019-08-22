import random

def randomizetoss(teams):
    return random.choice(teams)

def main():
    cond = input()
    weather = cond.split()[0].lower()
    time = cond.split()[1].lower()

    teams = ['Lengaburu', 'Enchai']
    tosswinner = randomizetoss(teams)

    choice = 'bats'
    if tosswinner == teams[0]:
        output = teams[0] + " wins toss and "
        if weather == 'cloudy' and time == 'night':
            choice = 'bowls'
        output += choice
    else:
        output = teams[1] + " wins toss and "
        if weather == 'clear' and time == 'day':
            choice = 'bowls'
        output += choice

    print(output)

if __name__ == '__main__':
    main()