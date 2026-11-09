from pico2d import *
import game_framework
import logo_mode

open_canvas()
# 한글 입력 모드에서는 입력기가 i 같은 영문자 키를 가져가 키 이벤트가 오지 않으므로 끔
SDL_StopTextInput()
game_framework.run(logo_mode)
close_canvas()
