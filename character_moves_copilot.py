from pico2d import *
import math

open_canvas()
character = load_image('character.png')
grass = load_image('grass.png')

def draw_character(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

def move_rectangle():
    # move right
    for x in range(400, 750, 10):
        draw_character(x, 90)

    # move up
    for y in range(90, 550, 10):
        draw_character(750, y)

    # move left
    for x in range(750, 50, -10):
        draw_character(x, 550)

    # move down (왼쪽 끝으로 내려옴)
    for y in range(550, 90, -10):
        draw_character(50, y)

    # y=90에서 x좌표를 가운데로 이동
    for x in range(50, 400, 10):
        draw_character(x, 90)

# 삼각운동 함수 추가

def move_triangle():
    # 삼각형 꼭짓점 좌표
    points = [(400, 90), (750, 550), (50, 550)]
    # 1번 꼭짓점 -> 2번 꼭짓점
    for t in range(0, 101):
        x = points[0][0] + (points[1][0] - points[0][0]) * t / 100
        y = points[0][1] + (points[1][1] - points[0][1]) * t / 100
        draw_character(x, y)
    # 2번 꼭짓점 -> 3번 꼭짓점
    for t in range(0, 101):
        x = points[1][0] + (points[2][0] - points[1][0]) * t / 100
        y = points[1][1] + (points[2][1] - points[1][1]) * t / 100
        draw_character(x, y)
    # 3번 꼭짓점 -> 1번 꼭짓점
    for t in range(0, 101):
        x = points[2][0] + (points[0][0] - points[2][0]) * t / 100
        y = points[2][1] + (points[0][1] - points[2][1]) * t / 100
        draw_character(x, y)

def move_circle():
    # 바닥에서 시작해서 바닥으로 끝나는 원운동
    r = 210  # 반지름 (원 크기 조절)
    cx, cy = 400, 90 + r  # 중심점 (바닥에서 r만큼 위)
    # 270도(아래)에서 시작해서 한 바퀴(360도) 돌고 다시 바닥으로
    for deg in range(270, 630, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        draw_character(x, y)

def main():
    while True:
        move_rectangle()  # 사각 운동
        move_triangle()   # 삼각 운동
        move_circle()     # 원 운동

main()
close_canvas()
