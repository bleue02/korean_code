from National_anthem import traditional_stories

import sys
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def print_difference(correct, user_input):
    for c, u in zip(correct, user_input):
        if c == u:
            print(c, end='')
        else:
            print('\033[31m' + u + '\033[0m', end='')
    print()

def korean_typing():
    while True:
        try:
            user_select = int(input('If you want to quit this game?\n'
                                    'please input "I want to quit this game"\n\n'
                                    '1: National_anthem\n'
                                    '2: Starry Night Poem \n'
                                    'Input: '))
            if user_select in [1, 2]:
                break
            else:
                print('Invalid selection. Please select 1 or 2.')
        except ValueError:
            print('Invalid input. Please enter a number.')

    stories = traditional_stories()
    if user_select in stories:
        selected_story = stories[user_select]
        story_lines = selected_story.splitlines()

        print('If you want to start game?\n'
              'Press Any Key!\n')

        start_time = time.time()
        for line in story_lines:
            print(line.strip())
            saved_text = input('Input: ')
            if 'I WANT TO QUIT THIS GAME' in saved_text.upper():
                print('Exited game!')
                sys.exit()
            print_difference(line.strip(), saved_text)
        end_time = time.time()
        total_time = int(end_time - start_time)
        print(f'Total time taken: {total_time} seconds')

        start_time = time.time()
        for line in story_lines:
            print(line.strip())
            saved_text = input('Input: ')
            if 'I WANT TO QUIT THIS GAME' in saved_text.upper():
                print('Exited game!')
                sys.exit()
            print_difference(line.strip(), saved_text)
        end_time = time.time()
        total_time = int(end_time - start_time)
        print(f'Total time taken: {total_time} seconds')

korean_typing()