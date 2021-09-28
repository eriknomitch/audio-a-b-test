import os
import sys
import random
import mutagen
import ipdb
import pexpect

def clear_console_screen():
    """
    Clear the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def spawn_interactive_command(command, args=[]):
    """
    Spawns an interactive shell command using pexpect.
    """
    child = pexpect.spawn(command, args)
    child.interact()

def files_in_directory(dir, ext=False, absolute_path=True):
    """
    Return list of files in a directory.
    """
    if absolute_path:
        return list(map(lambda f: os.path.abspath(os.path.join(dir, f)), files_in_directory(dir, ext, False)))

    if ext:
        return [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f)) and f.endswith(ext)]
    else:
        return [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]

def random_file_from_dir(dir, ext=False):
    """
    Return a random file from a directory of a certain extension.
    """
    files = os.listdir(dir)
    if ext:
        files = [f for f in files if f.endswith(ext)]
    return os.path.join(dir, random.choice(files))

def prompt_menu(message, choices):
    """
    Show the user their choices (prefixed with A, B, C...) and prompt them for their choice.
    """
    print(message)
    for i, choice in enumerate(choices):
        print("{}) {}".format(chr(i + 65), choice))
    return input("Choice: ")

def audio_file_information(path, skip_print=False):
    audio_file = mutagen.File(path)
    info_pprint = audio_file.info.pprint()
    if not skip_print:
        print(info_pprint)
    return info_pprint

def play_audio_file(path):
    spawn_interactive_command("vlc", ["--intf", "rc", path])

