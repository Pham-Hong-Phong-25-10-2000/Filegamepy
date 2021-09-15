import pygame,sys
#hàm chạy sàn
def draw_floor():
    screen.blit(floor,(floor_x_pos,600))
    screen.blit(floor,(floor_x_pos+432,600))
def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop = (216,384))
    return new_pipe
def move_pipe(pipes):
    for pipe in pipes :
        pipe.centerx -=5
    return pipes 
def draw_pipe(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface,pipe)
pygame.init()
screen=pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
#tạo biến cho trò chơi
gravity = 0.25
bird_movement = 0
#chèn background
bg = pygame.image.load('assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)
#chèn sàn
floor = pygame.image.load('assets/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
#tạo chim 
bird = pygame.image.load('assets/yellowbird-midflap.png').convert()
brid = pygame.transform.scale2x(bird)
brid_rect = bird.get_rect(center = (100,384))
#tạo ống 
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
#tạo timer 
spawnpine = pygame.USEREVENT
pygame.time.set_timer(spawnpine,1200)
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE :
                bird_movement = -11
        if event.type == spawnpine:
            pipe_list.append(create_pipe())
            
    screen.blit(bg,(0,0))
    #chim
    bird_movement += gravity
    brid_rect.centery += bird_movement
    screen.blit(bird,brid_rect)
    #ống 
    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)
    #sàn 
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos<= -432:
        floor_x_pos=0
    pygame.display.update()
    clock.tick(120)       