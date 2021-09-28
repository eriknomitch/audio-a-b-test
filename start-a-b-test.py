import os
import sys
import mutagen
import ipdb
import sh
import pexpect

# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
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

# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
audio_file_information("audio_pairs/test_flac.flac")
audio_file_information("audio_pairs/test_mp3_320.mp3")
audio_file_information("audio_pairs/test_mp3_128.mp3")

# play_audio_file("audio_pairs/test_flac.flac")

p = pexpect.spawn("htop")
p.interact()
