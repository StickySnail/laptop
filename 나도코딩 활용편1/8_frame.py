import pygame

###############################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("게임이름")

# FPS
clock = pygame.time.Clock()
###############################################################
# 1. 사용자 게임 초기화 ( 배경화면, 게임 이미지, 좌표, 속도, 폰트 등 )

running = True  # 게임이 진행 중인가?
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update()  # 게임화면을 다시 그리기! // 파이게임에서는 계속 배경을 불러와주어야 함

# 잠시 대기
pygame.time.delay(2000)  # 2 초 정도 대기

# pygame 종료
pygame.quit()
