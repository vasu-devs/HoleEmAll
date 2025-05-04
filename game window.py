import pygame
import random


pygame.init()


# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hole em ALL")

font = pygame.font.SysFont(None,36)
large_font = pygame.font.SysFont(None,72)

PLAYING = "playing"
GAME_OVER = "game_over"
WIN = "win"


def reset_game():
    global score , start_ticks, hole_radius, fruit_positions, game_state
    score =0
    start_ticks = pygame.time.get_ticks()
    hole_radius = 30
    game_state=PLAYING

    fruit_positions =[]
    for _ in range(30):
        x=random.randint(50,750)
        y=random.randint(50,550)
        fruit_positions.append([x,y])
        final_time=None

# Game Loop

time_limit =60
reset_game()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and game_state!=PLAYING:
            if event.key== pygame.K_SPACE:
                reset_game()

    screen.fill((50,200,50))  #green background

    seconds_passed = (pygame.time.get_ticks()-start_ticks)//1000

    time_left = max(0,time_limit-seconds_passed)
    
    if game_state == PLAYING:
        mouse_x , mouse_y = pygame.mouse.get_pos()


        new_fruit_positions = []
        for pos in fruit_positions:
            distance=((pos[0]-mouse_x)**2 + (pos[1]-mouse_y)**2)**0.5
            if distance > hole_radius:
                new_fruit_positions.append(pos)
            else:
                hole_radius+=1
                score+=1
        fruit_positions = new_fruit_positions

        for pos in fruit_positions:
            pygame.draw.circle(screen,(255,0,0),pos,10) #draws a red circle at the position of each fruit
        pygame.draw.circle(screen , (0,0,0),(mouse_x , mouse_y),hole_radius) #draws a circle at the mouse position

        if len(fruit_positions)==0:
            game_state = WIN
            final_time=time_left
        elif time_left<=55:
            game_state= GAME_OVER
            final_time=55


    score_text = font.render(f"Score: {score}", True,(255,255,255))
    screen.blit(score_text,(10,10))

    timer_text = font.render(f"Time: {time_left}",True , (255,255,255))
    screen.blit(timer_text,(10,50))


    if game_state!=PLAYING:
        overlay = pygame.Surface((800,600))
        overlay.fill((0,0,0))
        overlay.set_alpha(128)
        screen.blit(overlay,(0,0))


        if game_state== WIN:
            main_text = large_font.render("YOU WIN!", True, (255,255,255))
            status_text = font.render(f"Time remaining: {time_left}", True, (255,255,255))
        else:
            main_text = large_font.render("GAME OVER!", True, (255,255,255))
            status_text = font.render(f"Score: {score}", True, (255,255,255))

        restart_text=font.render("Press SPACE to play again", True , (255,255,255))
        restart_rect=restart_text.get_rect(center=(400,420))


        main_rect= main_text.get_rect(center=(400,250))
        status_rect = status_text.get_rect(center=(400,350))


        screen.blit(main_text, main_rect)
        screen.blit(status_text, status_rect)
        screen.blit(restart_text,restart_rect)


    pygame.display.flip()

pygame.quit()

