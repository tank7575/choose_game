from chose_game_CS50.attack import attack_narrative
from chose_game_CS50.peanut_butter_jar import peanut_butter_jar_narrative
from chose_game_CS50.telepathy import telepathy_narrative
from chose_game_CS50.undercover import undercover_narrative





TITLE = 'Aliens Intergalactic Marvel'
INTRO = '''
These earthlings are not using their full potential.
They are eating peanut butter, but is the most precious resource in
the universe, since it allows for intergalactic travel.  If our race is to survive, we must obtain
as much of it as possible.

'''
HERO = 'Zywgeh'
FIRST_PROMPT = f'''
You are an alien named {HERO} from a galaxy far, far away.   A monumental task has been given to you by high command.
From your mission depends the future of our plant.   Your are sent to carry out a secret operation to steal
peanut butter from the Earth.  How will you first infiltrate Planet Earth?
'''

FIRST_PROMPT_OPTIONS = '''
1) Become an undercover earthling
2) Give humans the power of telepathy in the hopes they enage in civil war
3) Become a peanut butter jar.
4) Attack the humans
'''

### UNDERCOVER EARTHLING NARRATIVE

### TELEPATHY NARRATIVE

### PEANUT BUTTER JAR NARRATIVE

### ATTACK HUMANS NARRATIVE



def main():
    print(TITLE)
    print(INTRO)
    print(FIRST_PROMPT)
    infiltrate_option = int(input(FIRST_PROMPT_OPTIONS))



    if infiltrate_option == 1:
        undercover_narrative()
    elif infiltrate_option == 2:
        telepathy_narrative()
    elif infiltrate_option == 3:
        peanut_butter_jar_narrative()
    else:
        attack_narrative()




if __name__ == '__main__':
    main()