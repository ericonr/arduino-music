#! python3

import subprocess
from pathlib import Path

def main():
    track = '-t3'

    music = Path('./music')

    midi_files = [name.with_suffix('') for name in music.iterdir() if name.is_file() and '.mid' in str(name)]

    for midi in midi_files:
        subprocess.run(['miditones', track, '-dp', str(midi)], stdout=subprocess.PIPE)
        print(midi)

main()