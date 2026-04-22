import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()

        self.music_folder = "C:\TT\Python\Practices\Practice9\music_player\music_folder"
        self.playlist = self.load_music()
        self.current_index = 0
        self.is_playing = False

    def load_music(self):
        files = []
        for file in os.listdir(self.music_folder):
            files.append(os.path.join(self.music_folder, file))
        return files

    def play(self):
        
        
        pygame.mixer.music.load(self.playlist[self.current_index])
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def previous_track(self):
        
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def get_current_track(self):
        
        return os.path.basename(self.playlist[self.current_index])

    def get_position(self):
        return pygame.mixer.music.get_pos() // 1000