import game_framework
import ball
import game_world
import play_mode
from pico2d import *

image = None

# 숫자 줄과 숫자 패드의 0, 1, 2 키를 각각 공 없음, 작은 공, 큰 공에 대응
ITEM_KEYS = {
    SDLK_0: None, SDLK_KP_0: None,
    SDLK_1: ball.SMALL, SDLK_KP_1: ball.SMALL,
    SDLK_2: ball.BIG, SDLK_KP_2: ball.BIG,
}


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def update():
    # 선택 창이 떠 있는 동안에도 게임 월드는 계속 움직임
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key in (SDLK_ESCAPE, SDLK_i):
            # ESC나 선택 창을 연 i 키를 다시 누르면 고르지 않고 닫음
            game_framework.pop_mode()
            return  # 남은 이벤트로 한 번 더 pop 되지 않게 바로 나감
        elif event.type == SDL_KEYDOWN and event.key in ITEM_KEYS:
            play_mode.boy.item = ITEM_KEYS[event.key]
            game_framework.pop_mode()
            return


def pause():
    pass


def resume():
    pass
