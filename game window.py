import pygame
import random


pygame.init()


# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hole em ALL")

title_font = pygame.font.SysFont('arial',72,bold=True)
score_font = pygame.font.SysFont('arial',36)
info_font = pygame.font.SysFont('arial',24)

COLORS={
    'background' : (34,139,34),
    'dark_bg' : (20,80,20),
    'fruit' : (255,69,0),
    'hole' : (20,20,20),
    'text' : (255,255,255),
    'score_panel' : (0,0,0,128),
    'win_text' : (50,205,50),
    'lose_text' : (178,34,34)
}

def draw_gradient_background(surface,color1,color2):
    height=surface.get_height()
    for i in range(height):
        factor = i/height
        r=color1[0]*(1-factor)+color2[0]*factor
        g=color1[1]*(1-factor)+color2[1]*factor
        b=color1[2]*(1-factor)+color2[2]*factor
        pygame.draw.line(surface, (r,g,b) , (0,i) , (surface.get_width(),i))
    
def draw_score_panel(surface , score , time):
    panel = pygame.Surface((200,90),pygame.SRCALPHA)
    pygame.draw.rect(panel, COLORS['score_panel'],(0,0,200,90), border_radius=10)
    score_text=score_font.render(f"Score: {score}", True, COLORS['text'])
    time_text = score_font.render(f"Time: {time}", True, COLORS['text']) 
    panel.blit(score_text,(20,10))
    panel.blit(time_text,(20,45))

    surface.blit(panel,(10,10))
    

PLAYING = "playing"
GAME_OVER = "game_over"
WIN = "win"


def reset_game():
    global score , start_ticks, hole_radius, fruit_positions, game_state, display_time
    score =0
    start_ticks = pygame.time.get_ticks()
    hole_radius = 30
    game_state=PLAYING
    display_time = time_limit

    fruit_positions =[]
    for _ in range(30):
        x=random.randint(50,750)
        y=random.randint(50,550)
        fruit_positions.append([x,y])

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
    for event in pygame.event.get():
        print(event) 
    # screen.fill((50,200,50))  #green background
    draw_gradient_background(screen,COLORS['background'],COLORS['dark_bg'])
    
    if game_state == PLAYING:
        seconds_passed = (pygame.time.get_ticks()-start_ticks)//1000

        display_time = max(0,time_limit-seconds_passed)
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
            pygame.draw.circle(screen,(*COLORS['fruit'],128),pos,15) 
            pygame.draw.circle(screen,COLORS['fruit'],pos,10)
        pygame.draw.circle(screen , COLORS['hole'],(mouse_x , mouse_y),hole_radius) #draws a circle at the mouse position

        if len(fruit_positions)==0:
            game_state = WIN
            
        elif display_time<=55:
            game_state= GAME_OVER
            display_time=55


    # score_text = font.render(f"Score: {score}", True,(255,255,255))
    # screen.blit(score_text,(10,10))

    # timer_text = font.render(f"Time: {display_time}",True , (255,255,255))
    # screen.blit(timer_text,(10,50))

    draw_score_panel(screen,score,display_time)
    
    if game_state!=PLAYING:
        overlay = pygame.Surface((800,600),pygame.SRCALPHA)
        # overlay.fill((0,0,0))
        # overlay.set_alpha(128)
        # screen.blit(overlay,(0,0))
        for i in range(60):
            pygame.draw.rect(overlay,(0,0,0,min(128,i*2)),(0,i*10,800,10))
        screen.blit(overlay,(0,0))

        if game_state == WIN:
            main_text_str = "YOU WIN!"
            main_text = title_font.render(main_text_str, True, COLORS['win_text'])
            status_text = score_font.render(f"Time remaining: {display_time}", True, COLORS['text'])
        else:
            main_text_str = "GAME OVER!"
            main_text = title_font.render(main_text_str, True, COLORS['lose_text'])
            status_text = score_font.render(f"Score: {score}", True, COLORS['text'])

        shadow_offset = 3
        shadow_text = title_font.render(main_text_str, True, (0, 0, 0))

        main_rect= main_text.get_rect(center=(400,250))
        shadow_rect= shadow_text.get_rect(center=(403,253))

        screen.blit(shadow_text,shadow_rect)
        screen.blit(main_text,main_rect)

        status_rect = status_text.get_rect(center=(400,350))
        screen.blit(status_text,status_rect)

        pulse= (pygame.time.get_ticks() % 1000)/1000
        alpha = int(128+127 * abs(pulse-0.5)*2)

        restart_text=info_font.render("Press SPACE to play again", True , COLORS['text'])
        restart_text.set_alpha(alpha)
        restart_rect=restart_text.get_rect(center=(400,420))


        # main_rect= main_text.get_rect(center=(400,250))
        # status_rect = status_text.get_rect(center=(400,350))


        # screen.blit(main_text, main_rect)
        # screen.blit(status_text, status_rect)
        screen.blit(restart_text,restart_rect)


    pygame.display.flip()

pygame.quit()

