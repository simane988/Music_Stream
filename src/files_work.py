import os
import time
import cv2
import mutagen.mp3
import logging
import src.music as music
from definitions import ROOT_DIR


def extract_covers(track_path, covers_path):
    local_file = track_path
    covers_dir = covers_path
    cover_name = music.get_name(track_path) + '.jpg'

    try:
        tags = mutagen.mp3.Open(local_file)
        data = ""
        for i in tags:
            if i.startswith("APIC"):
                data = tags[i].data
                break
        if not data:
            return False
        else:
            with open(covers_dir + cover_name, "wb") as cover:
                cover.write(data)
                return True
    except:
        logging.error('extract_cover: File \"%s\" not found in %s', local_file, covers_dir)
        return False


def is_dir_empty(inp_path):
    return len(os.listdir(inp_path)) == 0


def make_dir(inp_path):
    os.mkdir(inp_path)


def clear_dir(inp_path):
    file_list = os.listdir(inp_path)
    for i in file_list:
        os.remove(inp_path+'/'+i)


def video_to_frames(input_loc=ROOT_DIR+'/media/video/1.mp4', output_loc=ROOT_DIR+'/media/img/'):
    try:
        os.mkdir(output_loc)
    except OSError:
        pass

    time_start = time.time()

    cap = cv2.VideoCapture(input_loc)

    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print("Number of frames: ", video_length)
    count = 0
    print("Converting video..\n")

    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
        count = count + 1
        if count > (video_length-1):
            time_end = time.time()
            cap.release()
            print("Done extracting frames.\n%d frames extracted" % count)
            print("It took %d seconds for conversion." % (time_end-time_start))
            break


def create_conf(path=os.path.dirname(os.path.abspath(__file__))):
    file = open(path + '/conf.ini', 'w+')
    project_path = path[:-4]
    file.write('[default]\n'
               'first_start = 1\n'
               'project_name = Music_Stream\n'
               'version = 0.0.1a\n'
               '')
    file.write('[paths]\n'
               f'project_path = {project_path}\n'
               f'src_path = {project_path}/src\n'
               f'video_path = {project_path}/media/video\n'
               f'img_path = {project_path}/media/img\n'
               f'music_path = {project_path}/media/music\n'
               f'covers_path = {project_path}/media/covers\n'
               f'\n')
    file.write('[video]\n'
               'width = 1920\n'
               'height = 1080\n'
               'fps = 30')
    print(file.read())
    file.close()


if __name__ == "__main__":
    create_conf()
