
#  Interactive Music Visualizer

import pygame
import numpy as np
import soundfile as sf
import threading

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def display_waveform(file_path):
    pygame.init()
    width = 800
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Music Visualizer')

    try:
        audio_data, sr = sf.read(file_path)  # Load audio data
        audio_data = audio_data[:, 0]  # Only use first column is stereo 

        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 

            screen.fill((0, 0, 0))

            # Scale audio data to fit the screen height
            scaled_audio = audio_data * (height / 4)

            # x-axis coords for the waveform
            x = np.linspace(0, width, len(scaled_audio))

            # Draw a waveform 
            for i in range(1, len(scaled_audio)):
                pygame.draw.aaline(screen, (55, 0, 255),
                                   (int(x[i - 1]), int(height / 2 - scaled_audio[i - 1])),
                                   (int(x[i]), int(height / 2 - scaled_audio[i])), 2)

            pygame.display.flip()
            clock.tick(30)

    except Exception as e:
        print("Error:", e)

    pygame.quit()

def main():
    file_path = 'mk1.mp3'
    audio_thread = threading.Thread(target=play_audio, args=(file_path,))
    audio_thread.start()

    
    display_waveform(file_path)

if __name__ == "__main__":
    main()
