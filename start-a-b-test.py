import os
import sys
from ipdb import set_trace
import random

from utility import *

# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
def play_random_file_from_pairs(test_name):
    test_path = f"audio_pairs/{test_name}"
    to_play = random_file_from_dir(test_path)
    file_choices = files_in_directory(test_path)

    random.shuffle(file_choices)

    clear_console_screen()

    play_audio_file(to_play)
    clear_console_screen()

    guess = prompt_menu("Your guess", map(lambda f: audio_file_information(f, True), file_choices))
    clear_console_screen()

    if file_choices[int(guess)-1] == to_play:
        print("Correct")
    else:
        print("Incorrect")

    print()
    print("File played:")
    audio_file_information(to_play)

play_random_file_from_pairs("fragments_of_time")
