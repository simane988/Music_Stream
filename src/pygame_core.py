import pygame
import os
import configparser
import numpy as np
import cv2
from src import music
from src import files_work


def end_music(inp):
    inp = False


def main():
    # Config init and read config file
    conf = files_work.get_conf()
    conf.read(os.path.dirname(os.path.abspath(__file__)) + '/conf.ini')

    width = int(conf['video']['width'])  # Get width from config file
    height = int(conf['video']['height'])  # Get height from config file
    fps = int(conf['video']['fps'])  # Get fps from config file

    # PyGame init
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    screen = pygame.display.set_mode((width, height))  # Creating window
    pygame.display.set_caption("Music_Stream")
    clock = pygame.time.Clock()

    running = True
    frame_counter = 0  # Counter for frames in video
    song_counter = 0
    text_alpha = 0
    is_playing = False
    img_array = sorted(os.listdir(conf['paths']['img_path']))  # Sorted array of frame files

    # Starting main loop
    while running:
        clock.tick(fps)  # Stuff for fps

        # Quit condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Window quit button
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Esc button
                    running = False

        # Video code block
        img = pygame.image.load(conf['paths']['img_path'] + '/' + img_array[frame_counter])  # Reading frame file
        img = pygame.transform.scale(img, (width, height))  # Scaling it for window size
        screen.blit(img, (0, 0))  # Displaying frame

        if frame_counter == len(img_array) - 1:  # If we come to last frame
            frame_counter = 0  # Start with first frame
        frame_counter += 1  # Change frames' number

        # Music code block
        queue = music.get_music_list()  # List of songs
        if not pygame.mixer.music.get_busy():  # If song is not playing returns False
            if song_counter >= len(queue)-1:
                song_counter = 0

            # Playing next song
            pygame.mixer.music.load(queue[song_counter])
            song_name = music.get_name(queue[song_counter])
            artist_name = music.get_artist(queue[song_counter])
            cover = music.get_cover(queue[song_counter])
            print('Playing ' + song_name + ' : ' + artist_name)
            pygame.mixer.music.play()
            song_counter += 1
            text_alpha = 0
            music.get_cover(queue[song_counter])

        # Display next song
        display_name = my_font.render(song_name, 1, (0, 0, 0))
        name_alpha = pygame.Surface(display_name.get_size(), pygame.SRCALPHA)
        name_alpha.fill((255, 255, 255, text_alpha))
        display_name.blit(name_alpha, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(display_name, (width-300-display_name.get_width(), 70+display_name.get_height()))

        display_artist = my_font.render(artist_name, 1, (0, 0, 0))
        artist_alpha = pygame.Surface(display_artist.get_size(), pygame.SRCALPHA)
        artist_alpha.fill((255, 255, 255, text_alpha))
        display_artist.blit(artist_alpha, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(display_artist, (width-300-display_artist.get_width(), 90+display_artist.get_height()))

        cover_surf = pygame.image.load(conf['paths']['tmp_path']+'/cover.png')
        cover_surf = pygame.transform.scale(cover_surf, (200, 200))
        cover_alpha = pygame.Surface(cover_surf.get_size(), pygame.SRCALPHA)
        cover_alpha.fill((255, 255, 255, 255-text_alpha))
        cover_surf.blit(cover_alpha, (0, 0))
        screen.blit(cover_surf, (width-90-cover_surf.get_width(), 10))

        if text_alpha < 255:
            text_alpha += 1

        pygame.display.update()  # Updating PyGame screen

    pygame.quit()  # Quit from PyGame, close window etc


if __name__ == '__main__':
    main()
