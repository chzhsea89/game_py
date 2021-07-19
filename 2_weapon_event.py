import os
import pygame
##################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init() #초기화 (반드시필요)

#화면크기설정
screen_width = 640 # 가로크기
screen_height = 480 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Rabit pang")#게임 이름

#FPS
clock = pygame.time.Clock()
##################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치를 반환
image_path= os.path.join(current_path, "images") # images 폴터 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path,"bg.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_height = character_size[0]
character_width = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

#캐릭터 이동방향
character_to_x = 0

#캐릭터 이동속도
character_speed = 5

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0] #width 만 필요한 이유 캐릭터의 위치 기준에서 중앙에서 발사되야되는것이기 때문

#무기는 한번에 여러발 발사가능
weapons = []

#무기 이동속도
weapon_speed = 10




running = True 
while running:
    dt = clock.tick(60) 

# 2.이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running =False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 왼쪽 이동
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 오른쪽 이동
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: #무기발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:    
                character_to_x = 0

    # 3.게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    weapons = [[w[0], w[1]- weapon_speed] for w in weapons] #무기 위치를 위로

    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0 ]


    # 4.충돌 처리

    # 5. 화면에 그리기

    screen.blit(background,(0,0))
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos,weapon_y_pos))

    screen.blit(stage,(0,screen_height - stage_height))
    screen.blit(character,(character_x_pos, character_y_pos))



    pygame.display.update() # 게임화면을 다시 그리기

pygame.time.delay(1000) # 1초 정도 대기 (ms)

pygame.quit()
