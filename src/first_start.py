import os
import configparser
from src import files_work
from start import hello_pic, clear


def start():
    files_work.create_conf()
    conf = files_work.get_conf()
    conf['default']['first_start'] = '0'
    os.mkdir(conf['paths']['tmp_path'])

    clear()
    hello_pic()
    print("Input path to directory with video files : ", end='')
    inp = input()
    if inp != '':
        conf['paths']['video_path'] = os.path.abspath(inp)

    clear()
    hello_pic()
    print("Input path to directory where will be video frames : ", end='')
    inp = input()
    if inp != '':
        conf['paths']['img_path'] = os.path.abspath(inp)

    clear()
    hello_pic()
    print("Input path to directory with music files : ", end='')
    inp = input()
    if inp != '':
        conf['paths']['music_path'] = os.path.abspath(inp)

    clear()
    hello_pic()
    print("Input width of screen : ", end='')
    inp = input()
    if inp != '':
        conf['video']['width'] = inp

    clear()
    hello_pic()
    print("Input height of screen : ", end='')
    inp = input()
    if inp != '':
        conf['video']['height'] = inp

    clear()
    hello_pic()
    print("Input fps : ", end='')
    inp = input()
    if inp != '':
        conf['video']['fps'] = inp


if __name__ == '__main__':
    start()
