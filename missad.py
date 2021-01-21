from tkinter import *
from subprocess import call
import pygame
from pygame.locals import *

pygame.init()

screen_height = 300
screen_width = 300
line_width = 6
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Miras')

red = (255, 0, 0)
green = (255, 255, 255, .4)
black = (0, 0, 0)

font = pygame.font.SysFont(None, 40)

clicked = False
player = 1
pos = (0, 0)
markers = []
proigravshi = False
pobeditel = 0

again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

#??????? ?????? 3 ?? 3 ???? ????? ??????
for x in range(3):
	row = [0] * 3
	markers.append(row)



def draw_board():
	white = (255, 255, 255)
	blue = (0, 0, 255)
	screen.fill(white)
	for x in range(1, 3):
		pygame.draw.line(screen, blue, (0, 100 * x), (screen_width, 100 * x), line_width)
		pygame.draw.line(screen, blue, (100 * x, 0), (100 * x, screen_height), line_width)

def draw_markers():
	x_pos = 0
	for x in markers:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
				pygame.draw.line(screen, red, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), line_width)
			if y == -1:
				pygame.draw.circle(screen, black, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
			y_pos += 1
		x_pos += 1


def check_proigravshi():
	global proigravshi
	global pobeditel

	x_pos = 0
	for x in markers:
		#???????
		if sum(x) == 3:
			pobeditel = 1
			proigravshi = True
		if sum(x) == -3:
			pobeditel = 2
			proigravshi = True
		#??????
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == 3:
			pobeditel = 1
			proigravshi = True
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == -3:
			pobeditel = 2
			proigravshi = True
		x_pos += 1

	#?????
	if markers[0][0] + markers[1][1] + markers [2][2] == 3 or markers[2][0] + markers[1][1] + markers [0][2] == 3:
		pobeditel = 1
		proigravshi = True
	if markers[0][0] + markers[1][1] + markers [2][2] == -3 or markers[2][0] + markers[1][1] + markers [0][2] == -3:
		pobeditel = 2
		proigravshi = True

	#????
	if proigravshi == False:
		tie = True
		for row in markers:
			for i in row:
				if i == 0:
					tie = False
		if tie == True:
			proigravshi = True
			pobeditel = 0



def draw_proigravshi(pobeditel):

	if pobeditel != 0:
		end_text = "Player " + str(pobeditel) + " wins!"
	elif pobeditel == 0:
		end_text = "draw score!"

	end_img = font.render(end_text, True, black)
	pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
	screen.blit(end_img, (screen_width // 2 - 100, screen_height // 2 - 50))

	again_text = 'Play Again?'
	again_img = font.render(again_text, True, black)
	pygame.draw.rect(screen, green, again_rect)
	screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))


run = True
while run:

	#?????? ????? ? ???????
	draw_board()
	draw_markers()

	for event in pygame.event.get():
		#?????? ????? ?? ????
		if event.type == pygame.QUIT:
			run = False
		#?????? ????? ????
		if proigravshi == False:
			if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
				clicked = True
			if event.type == pygame.MOUSEBUTTONUP and clicked == True:
				clicked = False
				pos = pygame.mouse.get_pos()
				cell_x = pos[0] // 100
				cell_y = pos[1] // 100
				if markers[cell_x][cell_y] == 0:
					markers[cell_x][cell_y] = player
					player *= -1
					check_proigravshi()

	#???????? ??? ????
	if proigravshi == True:
		draw_proigravshi(pobeditel)
		#?????? ??? ??????? Play Again ??? ?? ?????? ?????
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
		if event.type == pygame.MOUSEBUTTONUP and clicked == True:
			clicked = False
			pos = pygame.mouse.get_pos()
			if again_rect.collidepoint(pos):
				#????? ??????
				proigravshi = False
				player = 1
				pos = (0, 0)
				markers = []
				pobeditel = 0
				#??????? ?????? 3 ?? 3 ???? ?????
				for x in range (3):
					row = [0] * 3
					markers.append(row)

	pygame.display.update()

pygame.quit()