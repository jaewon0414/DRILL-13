from pico2d import *
import game_framework
import game_world
import item_mode
import pause_mode
import title_mode
from boy import Boy
from grass import Grass

boy = None


def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.push_mode(item_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
        else:
            boy.handle_event(event)


def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    # 다시 들어왔을 때 객체가 겹치지 않도록 월드를 비움
    game_world.clear()


def pause():
    # 아이템 모드가 키 입력을 받는 동안 방향키를 떼도 소년이 계속 달리지 않게 함
    boy.release_keys()


def resume():
    pass
