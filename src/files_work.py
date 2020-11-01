import os
import time
import cv2
import logging
import configparser


def conf_log():
    logging.basicConfig(filename='Music_stream.log', level=logging.DEBUG)


def get_conf():
    try:
        config = configparser.ConfigParser()
        config.read(os.path.dirname(os.path.abspath(__file__)) + '/conf.ini')
        return config
    except:
        logging.error('get_conf: Can\'t read config file %s' % os.path.dirname(os.path.abspath(__file__)) + '/conf.ini')


def is_dir_empty(inp_path):
    return len(os.listdir(inp_path)) == 0


def make_dir(inp_path):
    os.mkdir(inp_path)


def clear_dir(inp_path):
    file_list = os.listdir(inp_path)
    for i in file_list:
        os.remove(inp_path+'/'+i)


def video_to_frames(input_loc, output_loc):
    conf = get_conf()
    try:
        os.mkdir(conf['paths']['img_path'])
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
               'version = 0.0.1 prealpha\n'
               'github_link = https://github.com/simane988/Music_Stream\n'
               'license = Apache License 2.0\n'
               'DEBUG = 0\n'
               '\n')
    file.write('[paths]\n'
               f'project_path = {project_path}\n'
               f'src_path = {project_path}/src\n'
               f'video_path = {project_path}/media/video\n'
               f'img_path = {project_path}/media/img\n'
               f'music_path = {project_path}/media/music\n'
               f'tmp_path = {project_path}/media/tmp\n'
               f'\n')
    file.write('[video]\n'
               'src = None\n'
               'width = 1920\n'
               'height = 1080\n'
               'fps = 30\n'
               'font_size = 30\n'
               '\n')
    print(file.read())
    file.close()


if __name__ == "__main__":
    # clear_dir('/home/g3ck0/Code/Python/Music_Stream/media/img/')
    # video_to_frames('/home/g3ck0/Code/Python/Music_Stream/media/video/7TwT.gif', '/home/g3ck0/Code/Python/Music_Stream/media/img/')
    create_conf()
