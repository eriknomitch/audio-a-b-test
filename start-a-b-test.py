import os
import sys
import mutagen
import ipdb

def audio_file_information(path, skip_print=False):
    audio_file = mutagen.File(path)
    info_pprint = audio_file.info.pprint()
    if not skip_print:
        print(info_pprint)
    return info_pprint

audio_file_information("audio_pairs/test_flac.flac")
