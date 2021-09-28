import os
import random
import mutagen
import ipdb
import pexpect

def spawn_an_interactive_command(command):
    """
    Spawns an interactive shell command using pexpect.
    """
    child = pexpect.spawn(command)
    child.interact()

def audio_file_information(path, skip_print=False):
    audio_file = mutagen.File(path)
    info_pprint = audio_file.info.pprint()
    if not skip_print:
        print(info_pprint)
    return info_pprint

def play_audio_file(path):
    p = pexpect.spawn("vlc", ["--intf", "rc", path])
    p.interact()
    print(p)
    return p


def random_file_from_dir(dir, ext=False):
    """
    Return a random file from a directory of a certain extension.
    """
    files = os.listdir(dir)
    if ext:
        files = [f for f in files if f.endswith(ext)]
    return os.path.join(dir, random.choice(files))



