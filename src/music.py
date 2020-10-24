import os
import logging
from mutagen.easyid3 import EasyID3
from definitions import ROOT_DIR


def get_music_list(inp_path):
    logging.basicConfig(filename='sample.log', filemode='w', level=logging.INFO)
    files_list = [inp_path + i for i in os.listdir(inp_path)]
    filtered_file_list = []
    for i in files_list:
        if i.endswith('.mp3'):
            filtered_file_list.append(i)
        else:
            logging.info("File %s is not mp3" % i)

    return filtered_file_list


def get_name(inp_path):
    audio = EasyID3(inp_path)
    return str(audio['title'][0])


def get_artist(inp_path):
    audio = EasyID3(inp_path)
    return str(audio['artist'][0])


if __name__ == '__main__':
    music_list = get_music_list(ROOT_DIR + '/media/covers/')
    print(get_artist(music_list[0]))
