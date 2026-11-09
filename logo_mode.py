import game_framework
from pico2d import *

image = None
logo_start_time = 0.0


def init():
    global image, logo_start_time

    image = load_image('tuk_credit.png')
    logo_start_time = get_time()


def finish():
    global image
    del image


def update():
    global logo_start_time

    if get_time() - logo_start_time >= 2.0:
        logo_start_time = get_time()
        game_framework.quit()


def render():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    # 이벤트 큐를 비워서 창이 응답 없음 상태가 되지 않게 함
    events = get_events()
