# Python implementation of the 
# Sorting visualiser: Double Selection Sort 
 
# Imports
import pygame
import random
import time
import os
import numpy as np
import sys
from scipy.io.wavfile import write

# Samples per second
sps = 44100

# Frequency / pitch of the sine wave
freq_hz = 480.0

# Duration
duration_s = 0.1

each_sample_number = np.arange(duration_s * sps)
pygame.font.init()
pygame.mixer.init()
startTime = time.time()

# Total window
screen = pygame.display.set_mode((1800, 1000))
 
# Title and Icon 
pygame.display.set_caption("SORTING VISUALISER")

run = True
size = 300
counter = 0
 
# Window size and some initials
width = 750
array = [0] * size

arr_clr =[(128, 0, 0)] * size
clr_ind = 0

# Colors
clr =[(128, 0, 0), (0, 255, 0), 
(0, 0, 153), (255, 102, 0)] 
fnt = pygame.font.SysFont("comicsans", 30)
fnt1 = pygame.font.SysFont("comicsans", 20)

# Function to generate new Array
def generate_arr():
    for i in range(1, size):
        arr_clr[i]= clr[0]
        array[i]= random.randrange(1, 160)
 
# Initially generate a array
generate_arr() 
 
# Function to refill the 
# updates on the window 
def refill():
    screen.fill((0,0,0))
    draw()
    pygame.display.update()
    pygame.time.delay(30)
 
# Sorting Algorithm: Insertion sort
def minMaxSelectionSort(arr, n = size): 
    global counter
    i = 0
    j = n-1
    while(i < j): 
        min = arr[i] 
        max = arr[i] 
        min_i = i 
        max_i = i 
        refill()
        for k in range(i, j + 1, 1): 
            if (arr[k] > max): 
                max = arr[k] 
                max_i = k 
                freq_hz = (array[k]*3)
                waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
                waveform_quiet = waveform * 0.3
                waveform_integers = np.int16(waveform_quiet * 32767)
                write('first_sine_wave.wav', sps, waveform_integers)
                pygame.mixer.music.load('first_sine_wave.wav')
                pygame.mixer.music.play()
                os.remove('first_sine_wave.wav')
                counter +=1
            
            elif (arr[k] < min): 
                min = arr[k] 
                min_i = k 
                freq_hz = (array[k]*3)
                waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
                waveform_quiet = waveform * 0.3
                waveform_integers = np.int16(waveform_quiet * 32767)
                write('first_sine_wave.wav', sps, waveform_integers)
                pygame.mixer.music.load('first_sine_wave.wav')
                pygame.mixer.music.play()
                os.remove('first_sine_wave.wav')
                counter +=1
        
        # shifting the min. 
        temp = arr[i] 
        arr[i] = arr[min_i] 
        arr[min_i] = temp 
        counter +=1
  
        # Shifting the max. The equal condition 
        # happens if we shifted the max to  
        # arr[min_i] in the previous swap. 
        if (arr[min_i] == max): 
            temp = arr[j] 
            arr[j] = arr[min_i] 
            arr[min_i] = temp 
            counter +=1
        else: 
            temp = arr[j] 
            arr[j] = arr[max_i] 
            arr[max_i] = temp 
            counter +=1
  
        i += 1
        j -= 1
    
# Function to Draw the array values
def draw():
    # Text should be rendered
    txt = fnt.render("SORT: PRESS 'ENTER'", \
                                1, (255, 255, 255))
    # Position where text is placed
    screen.blit(txt, (20, 10))
    
    txt1 = fnt.render("NEW ARRAY: PRESS 'R'", \
                                1, (255, 255, 255))
    screen.blit(txt1, (20, 40))
    txt2 = fnt1.render("ALGORITHM USED : DOUBLE SELECTION SORT", 1, (255, 255, 255))
    screen.blit(txt2, (550, 60))
    text3 = fnt1.render("Running Time(sec): "+\
            str(int(time.time() - startTime)), \
                                  1, (255, 255, 255))
    screen.blit(text3, (575, 20))
    text4 = fnt1.render("Iterations: "+\
            str(int(counter)), \
                                  1, (255, 255, 255))
    screen.blit(text4, (800, 20))
    
    element_width =(width-150)//150
    boundry_arr = 900 / 150
    boundry_grp = 550 / 100
    pygame.draw.line(screen, (0,0,0), (0, 95), \
                                  (1800, 95), 6)
     
    # Drawing the array values as lines
    for i in range(1, size):
        pygame.draw.line(screen, arr_clr[i], \
                   (boundry_arr * i-3, 100), \
                   (boundry_arr * i-3, \
     array[i]*boundry_grp + 100), element_width)
 
# Program should be run 
# continuously to keep the window open
os.system('clear')

while run:
    # background
    screen.fill((0,0,0))
 
    # Event handler stores all event 
    for event in pygame.event.get():
 
        # If we click Close button in window
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                generate_arr()
                counter = 0 
            if event.key == pygame.K_q:
                sys.exit() 
            if event.key == pygame.K_RETURN:
                minMaxSelectionSort(array)    
    draw()
    pygame.display.update()
     
pygame.quit()