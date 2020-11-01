import os
import logging
import mutagen.mp3
import cv2
import configparser
import numpy as np
from src import files_work
from mutagen.easyid3 import EasyID3


def get_music_list():
    files_work.conf_log()
    try:
        conf = files_work.get_conf()
        music_dir = conf['paths']['music_path']
        files_list = [os.path.join(music_dir, i) for i in os.listdir(music_dir)]
        filtered_file_list = []
        for i in files_list:
            if i.endswith('.mp3'):
                filtered_file_list.append(i)
            else:
                logging.info("get_music_list: File %s is not mp3" % i)

        return filtered_file_list
    except:
        logging.error('get_music_list: Something wrong with music dir path %s', music_list)
        return None


def get_cover(track_path):
    files_work.conf_log()
    try:
        tags = mutagen.mp3.Open(track_path)
        data = ""
        for i in tags:
            if i.startswith("APIC"):
                data = tags[i].data
                break
        if not data:
            logging.error('get_cover: File \"%s\" don\'t have cover', track_path)
            return None
        else:
            conf = files_work.get_conf()
            nparr = np.fromstring(data, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            cv2.imwrite(conf['paths']['tmp_path'] + "/cover.png", img_np)
            return 0
    except:
        logging.error('get_cover: File \"%s\" have something wrong with cover', track_path)
        return None


def get_name(inp_path):
    files_work.conf_log()
    try:
        audio = EasyID3(inp_path)
        return str(audio['title'][0])
    except:
        logging.error('get_name: File \"%s\" have something wrong with name', inp_path)
        return None


def get_artist(inp_path):
    files_work.conf_log()
    try:
        audio = EasyID3(inp_path)
        return str(audio['artist'][0])
    except:
        logging.error('get_artist: File \"%s\" have something wrong with artist', inp_path)
        return None


if __name__ == '__main__':
    music_list = get_music_list()
    print(get_artist(music_list[0]))
