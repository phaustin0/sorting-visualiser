# main file

#################
###  Imports  ###
#################
import pygame
import sys
from bar import Bar
from settings import *
from random import randint


###########################
###  Initialise PyGame  ###
###########################
pygame.init()


########################
###  Create a Clock  ###
########################
clock = pygame.time.Clock()


###################
###  Functions  ###
###################
# create array of bars
def create_bars(bars, num_of_bars):
    for i in range(num_of_bars):
        bar_height = randint(5, 95) * bar_multiplier
        bar = Bar(bar_height, num_of_bars)
        bars.append(bar)

# draw the bars
def draw_bars(screen):
    for i in range(len(bars)):
        bars[i].draw(screen, i * bars[i].width + 5, height - bars[i].height)

# draw everything
def draw(screen):
    clock.tick(fps)
    screen.fill(bg_colour)  # fill background
    draw_bars(screen)  # draw the bars

    # update display
    pygame.display.update()

# create window
def create_window(width, height, title):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    return screen

# help function
def display_help(error_msg):
    print("")
    print(f"    {error_msg}")
    print("")
    print("    Proper Usage:")
    print("      $ python main.py [num_of_bars (int)] [algorithm_to_use (str)]")
    print("          Algorithms available:")
    print("            -> 'bubble'    :  Bubble Sort")
    print("            -> 'selection' :  Selection Sort")
    print("            -> 'insertion' :  Insertion Sort")
    print("            -> 'merge'     :  Merge Sort")
    print("")

# main function
def main(screen):
    is_running = True  # run conditional
    while is_running:
        clock.tick(fps)
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if user pressed the 'X' button 
                is_running = False  # exit the loop

            # check if player pressed a key:
            if event.type == pygame.KEYDOWN:
                # check if the key is space
                if event.key == pygame.K_SPACE:
                    # sort
                    alg(lambda: draw(screen), bars)
                    make_red(screen)
                # check if user pressed 'r'
                if event.key == pygame.K_r:
                    bars.clear()
                    create_bars(bars, num_of_bars)

        # draw everything
        draw(screen)

    # exit the loop
    pygame.quit()

# make all bars red, just to be sure
def make_red(screen):
    for bar in bars:
        bar.make_sorted()
        draw(screen)


####################
###  Algorithms  ###
####################

# bubble sort
def bubble_sort(draw, bars):
    idx = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        max_idx = len(bars) - 1 - idx
        if max_idx == 0:
            bars[max_idx].make_sorting()
            break
        for i in range(max_idx):
            bars[i].make_minimum()
            bars[i + 1].make_minimum()
            draw()
            if bars[i].height > bars[i + 1].height:
                bars[i], bars[i + 1] = bars[i + 1], bars[i]
            bars[i].make_unsorted()
            bars[i + 1].make_unsorted()
            draw()
        bars[max_idx].make_sorting()
        idx += 1

# selection sort
def selection_sort(draw, bars):
    idx = 0
    while idx < num_of_bars:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        bars[idx].make_minimum()
        min_idx = idx
        draw()
        for i in range(idx + 1, num_of_bars):
            if bars[i].height < bars[min_idx].height:
                bars[idx].make_unsorted()
                bars[min_idx].make_unsorted()
                min_idx = i
                bars[min_idx].make_minimum()
                draw()
        bars[idx], bars[min_idx] = bars[min_idx], bars[idx]
        bars[idx].make_sorting()
        idx += 1

# insertion sort
def insertion_sort(draw, bars):
    bars[0].make_sorting()
    draw()
    for i in range(1, num_of_bars):
        current = bars[i]
        current.make_minimum()
        draw()
        j = i - 1
        while j >= 0 and current.height < bars[j].height:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            bars[j].make_minimum()
            draw()
            bars[j + 1] = bars[j]
            bars[j + 1].make_sorting()
            draw()
            j -= 1
        bars[j + 1] = current
        bars[j + 1].make_sorting()
        draw()

# merge sort
def merge_sort(draw, bars):
    if len(bars) > 1:
        mid_idx = len(bars) // 2
        left = bars[:mid_idx]
        right = bars[mid_idx:]
        merge_sort(draw, left)
        merge_sort(draw, right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            left[i].make_minimum()
            right[j].make_minimum()
            draw()
            if left[i].height < right[j].height:
                bars[k] = left[i]
                left[i].make_sorting()
                draw()
                i += 1
            else:
                bars[k] = right[j]
                right[j].make_sorting()
                draw()
                j += 1
            k += 1

        while i < len(left):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            bars[k] = left[i]
            left[i].make_sorting()
            draw()
            i += 1
            k += 1

        while j < len(right):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            bars[k] = right[j]
            right[j].make_sorting()
            draw()
            j += 1
            k += 1


############################
###  Algorithm Settings  ###
############################
str_to_alg_key = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "merge": merge_sort
}

str_to_alg_name_key = {
    "bubble": "Bubble Sort Algorithm",
    "selection": "Selection Sort Algorithm",
    "insertion": "Insertion Sort Algorithm",
    "merge": "Merge Sort Algorithm"
}

if __name__ == '__main__':
    if len(sys.argv) < 3:
        display_help("Insufficient Arguments")
        pygame.quit()
        quit()
    try:
        num_of_bars = int(sys.argv[1])
        alg = str_to_alg_key[sys.argv[2]]
    except Exception:
        display_help("Unexpected Error Occured")
        pygame.quit()
        quit()
    window_title = f"{str_to_alg_name_key[sys.argv[2]]} {title}"
    screen = create_window(width, height, window_title)
    create_bars(bars, num_of_bars)  # create the bars
    main(screen)

