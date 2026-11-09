import os

from pico2d import *
import game_framework
import game_world
import play_mode

font = None


def init():
    global font
    # pico2d에 기본으로 들어있는 폰트 사용
    font = load_font(os.getenv('PICO2D_DATA_PATH') + '/ConsolaMalgun.ttf', 40)


def finish():
    global font
    del font


def update():
    # 정지 중에는 아무것도 갱신하지 않음
    pass


def render():
    clear_canvas()
    game_world.render()  # 플레이 화면을 멈춘 상태 그대로 그림
    draw_rectangle(280, 260, 520, 340, 0, 0, 0, filled=True)
    draw_rectangle(280, 260, 520, 340, 255, 255, 255)
    font.draw(334, 300, 'PAUSED', (255, 255, 255))
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
        elif event.type == SDL_KEYUP:
            # 정지 중에 뗀 방향키를 소년에게 전달해서, 재개 후 혼자 계속 달리지 않게 함
            play_mode.boy.handle_event(event)


def pause():
    pass


def resume():
    pass
