import pygame
import pyelement
import random
from math import floor
import json

#---------Initialise Pygame---------#
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Mushie Mushie')
pygame.font.init()
font = pygame.font.Font('resource/ShortStack-Regular.ttf', 38)
font_big = pygame.font.Font('resource/ShortStack-Regular.ttf', 48)
font_small = pygame.font.Font('resource/ShortStack-Regular.ttf', 30)
clock = pygame.time.Clock()
currency_list = ["K","M","B","T","aa","ab","ac","ad","ae","af","ag","ah","ai","aj","ak","al","am","an","ao","ap","aq","ar","as","at","au","av","aw","ax","ay","az","ba","bb","bc","bd","be","bf","bg","bh","bi","bj","bk","bl","bm","bn","bo","bp","bq","br","bs","bt","bu","bv","bw","bx","by","bz"]

#------------Custom Function-----------------#
class DropAnimation():
    def __init__(self, x, y,text):
        self.x = x
        self.y = y
        self.text = text
        
    def animate(self, list_of_mushroom):
        self.y -= 10
        if self.y < 50:
            list_of_mushroom.remove(self)

    def draw(self,surface):
        surface.blit(self.text, (self.x, self.y))

def format_number(n):
    if n >= 1000:
        currency = floor((len(str(n))-1)/3)
        i = currency*3
        if (n / 10**i) % 1 == 0:
            n = '{:.0f}'.format(n/10**i)
            n+=currency_list[currency-1]
        else:
            n = '{:.2f}'.format(n/10**i)
            n+=currency_list[currency-1]
    return n

#-------ImageLoad Area-------#
monster_sprite1_img = pygame.image.load('images/monster_sprite1.png').convert_alpha()
monster_sprite2_img = pygame.image.load('images/monster_sprite2.png').convert_alpha()
button_img = pygame.image.load('images/cubebutton.png').convert_alpha()
upgrade_button_img = pygame.image.load('images/upgrade_button.png').convert_alpha()
upgrade_button_no_img = pygame.image.load('images/upgrade_button_no.png').convert_alpha()
upgrade_button_max_img = pygame.image.load('images/upgrade_button_max.png').convert_alpha()
boost_img = pygame.image.load('images/boost.png').convert_alpha()
background_img = pygame.image.load('images/background.png').convert_alpha()
mushroom1_img = pygame.image.load('images/mushroom1.png').convert_alpha()
mushroom2_img = pygame.image.load('images/mushroom2.png').convert_alpha()
mushroom3_img = pygame.image.load('images/mushroom3.png').convert_alpha()
mushroom4_img = pygame.image.load('images/mushroom4.png').convert_alpha()
score_board_img = pygame.image.load('images/score_board.png').convert_alpha()
side_bar_img = pygame.image.load('images/side_bar.png').convert_alpha()
poop_img = pygame.image.load('images/poop.png').convert_alpha()
menu_background_img = pygame.image.load('images/menu_background.png').convert_alpha()
menu_monster_sprite_img = pygame.image.load('images/menu_monster_sprite.png').convert_alpha()
game_title_img = pygame.image.load('images/game_title.png').convert_alpha()
loading_sprite_img = pygame.image.load('images/loading_sprite.png').convert_alpha()
credit_img = pygame.image.load('images/credit.png').convert_alpha()
credit_x_img = pygame.image.load('images/credit_x.png').convert_alpha()
credit_button_img = pygame.image.load('images/credit_button.png').convert_alpha()
quit_button_img = pygame.image.load('images/quit.png').convert_alpha()
sleep_dragon_img = pygame.image.load('images/sleep_dragon.png').convert_alpha()
thanksforplaying_img = pygame.image.load('images/thanksforplaying.png').convert_alpha()
continue_img = pygame.image.load('images/continue.png').convert_alpha()
newgames_img = pygame.image.load('images/newgames.png').convert_alpha()

#------Pyelement Area--------#
monster_sprite1 = pyelement.SpriteSheet(monster_sprite1_img)
monster_sprite2 = pyelement.SpriteSheet(monster_sprite2_img)
menu_monster_sprite = pyelement.SpriteSheet(menu_monster_sprite_img)
loading_sprite = pyelement.SpriteSheet(loading_sprite_img)
sleep_dragon_sprite = pyelement.SpriteSheet(sleep_dragon_img)
thanksforplaying = pyelement.SpriteSheet(thanksforplaying_img)
button = pyelement.Button(270,220,button_img,25/48)
upgrade_button1 = pyelement.Button(575,120,upgrade_button_img,0.65)
upgrade_button2 = pyelement.Button(575,230,upgrade_button_img,0.65)
upgrade_button3 = pyelement.Button(575,340,upgrade_button_img,0.65)
upgrade_button4 = pyelement.Button(575,450,upgrade_button_img,0.65)
upgrade_button_no_1 = pyelement.Button(575,120,upgrade_button_no_img,0.65)
upgrade_button_no_2 = pyelement.Button(575,230,upgrade_button_no_img,0.65)
upgrade_button_no_3 = pyelement.Button(575,340,upgrade_button_no_img,0.65)
upgrade_button_no_4 = pyelement.Button(575,450,upgrade_button_no_img,0.65)
upgrade_button_max_1 = pyelement.Button(575,120,upgrade_button_max_img,0.65)
upgrade_button_max_2 = pyelement.Button(575,230,upgrade_button_max_img,0.65)
upgrade_button_max_3 = pyelement.Button(575,340,upgrade_button_max_img,0.65)
upgrade_button_max_4 = pyelement.Button(575,450,upgrade_button_max_img,0.65)
boost_button = pyelement.Button(10,400,boost_img,0.6)
credit_button = pyelement.Button(20,520,credit_button_img,0.2)
credit_x = pyelement.Button(175,155,credit_x_img,0.6)
quit_button = pyelement.Button(660,520,quit_button_img,0.35)
continue_button = pyelement.Button(270,520,continue_img,1)
newgames_button = pyelement.Button(270,520,newgames_img,1)
background = pyelement.ImageDraw(0,0,background_img,1)
mushroom1 = pyelement.ImageDraw(594,142,mushroom1_img,0.47)
mushroom2 = pyelement.ImageDraw(595,252,mushroom2_img,0.47)
mushroom3 = pyelement.ImageDraw(595,362,mushroom3_img,0.5)
mushroom4 = pyelement.ImageDraw(595,472,mushroom4_img,0.5)
score_board = pyelement.ImageDraw(203,10,score_board_img,0.4)
side_bar1 = pyelement.ImageDraw(740,110,side_bar_img,1)
side_bar2 = pyelement.ImageDraw(-125,110,side_bar_img,1)
menu_background = pyelement.ImageDraw(0,0,menu_background_img,1)
game_title = pyelement.ImageDraw(90,30,game_title_img,0.75)
credit = pyelement.ImageDraw(-45,145,credit_img,0.65)

#------Music Area-------#
#songlist = ['resource/onesummerday.mp3','resource/merrygoround.mp3','resource/atownwithoceanview.mp3']
#pygame.mixer.init()
#pygame.mixer.music.load(songlist[random.randint(0,1)])
#pygame.mixer.music.play(0)
#nyah = pygame.mixer.Sound('resource/nyah.ogg')
#upgrade_sound = pygame.mixer.Sound('resource/Ka-ching.ogg')
#roar = pygame.mixer.Sound('resource/roar.mp3')
#paper = pygame.mixer.Sound('resource/paper.mp3')

data = {
    'magic_faeces_value' : 0,
    'upgrade1_lvl_value' : 1,
    'upgrade1_price_value' : 1000,
    'upgrade2_lvl_value' : 1,
    'upgrade2_price_value' : 100000,
    'upgrade3_lvl_value' : 1,
    'upgrade3_price_value' : 10000000,
    'upgrade4_lvl_value' : 1,
    'upgrade4_price_value' : 1000000000,
    'faeces_per_click' : 200,
    'increase_rate' : 10,
    'booster_count' : 10
}

try:
    with open('save.txt') as save_file:
        data = json.load(save_file)
except:
    print("No file created")


#------Variable Area------#
animation_cooldown = 10
animation_timer = 0
ending_timer = 0
frame = 0
loading_frame = 0
ending_frame = 0
list_of_falling_number=[]
increase_timer = 0
upgrade1_max = False
upgrade2_max = False
upgrade3_max = False
upgrade4_max = False
boost_mode = False
booster_timer = 0
game_state = 'menu'
credit_state = False
input_box1 = pygame.Rect(250, 140, 270, 45)
input_box2 = pygame.Rect(250, 200, 270, 45)
name = ""
password = ""
active1 = False
active2 = False
nametext = ""

#--------Pygame Start-------#
run = True
while run:
    if game_state == 'menu':
        menu_background.draw(screen)
        animation_list = []
        for x in range(4):
            animation_list.append(menu_monster_sprite.get_frame(x,480,480,1,(0,0,0)))
        animation_timer += 1
        if animation_timer >= animation_cooldown:
            frame += 1
            animation_timer = 0
        if frame >= len(animation_list):
            frame = 0
        animation_list[frame]= pygame.transform.scale(animation_list[frame],(400,420)).convert_alpha()
        screen.blit(animation_list[frame], (200,240))
        game_title.draw(screen)
        if button.draw(screen):
            if name != "" and password != "":
                game_state = "loading"
        if credit_state == False:
            if credit_button.draw(screen):
                #paper.play()
                credit_state = True
        else:
            credit.draw(screen)
            if credit_x.draw(screen):
                credit_state = False
        if quit_button.draw(screen):
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box1.collidepoint(event.pos):
                    active1 = True
                else:
                    active1 = False
                if input_box2.collidepoint(event.pos):
                    active2 = True
                else:
                    active2 = False

            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_RETURN:
                        pass
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode
                    nametext = name
            
                if active2:
                    if event.key == pygame.K_RETURN:
                        pass
                    elif event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode
                    passtext = password


            if name == "":
                nametext = "Username..."
                text_surface1 = font_small.render(nametext, True, (200,200,200))
            else:
                text_surface1 = font_small.render(nametext, True, (0,0,0))
            if password == "":
                passtext = "Password..."
                text_surface2 = font_small.render(passtext, True, (200,200,200))
            else:
                text_surface2 = font_small.render(passtext, True, (0,0,0))
            if event.type == pygame.QUIT:
                run = False
        
        pygame.draw.rect(screen, (250,250,250), input_box1, 0)
        pygame.draw.rect(screen, (200,200,200), input_box1, 4)
        pygame.draw.rect(screen, (250,250,250), input_box2, 0)
        pygame.draw.rect(screen, (200,200,200), input_box2, 4)
        screen.blit(text_surface1, (input_box1.x + 5, input_box1.y + 10))
        screen.blit(text_surface2, (input_box2.x + 5, input_box2.y + 10))
        
    elif game_state == "loading":
        animation_list = []
        for z in range(10):
            animation_list.append(loading_sprite.get_frame(z,800,600,1,(0,0,0)))
        animation_timer += 1
        if animation_timer >= 9:
            loading_frame += 1
            animation_timer = 0
        if loading_frame >= len(animation_list):
            loading_frame = 0
            game_state = "game"
        animation_list[loading_frame]= pygame.transform.scale(animation_list[loading_frame],(800,600)).convert_alpha()
        screen.blit(animation_list[loading_frame], (0,0))

    elif game_state == "game":
        animation_list = []
        screen.fill((255,255,255))
        background.draw(screen)
        monster_select = 1
        if boost_mode == True:
            monster_select = 2

        #-------Sprite Select-------#
        if monster_select == 1:
            for y in range(4):
                animation_list.append(monster_sprite1.get_frame(y,480,480,1,(0,0,0)))
        elif monster_select == 2:
            for z in range(5):
                animation_list.append(monster_sprite2.get_frame(z,480,480,1,(0,0,0)))

        #-------Sprite Area---------#
        animation_timer += 1
        if animation_timer >= animation_cooldown:
            frame += 1
            animation_timer = 0
        if frame >= len(animation_list):
            frame = 0
        if monster_select == 1:
            animation_list[frame]= pygame.transform.scale(animation_list[frame],(250,250)).convert_alpha()
            screen.blit(animation_list[frame], (270,250))
        elif monster_select == 2:
            animation_list[frame]= pygame.transform.scale(animation_list[frame],(330,330)).convert_alpha()
            screen.blit(animation_list[frame], (230,220))

        #-------Textbox Area-------#
        score_text = format_number(data['magic_faeces_value'])
        score = font_big.render(f'{score_text}', True, (0,0,0))
        upgrade1_price_value_text = format_number(data['upgrade1_price_value'])
        upgrade2_price_value_text = format_number(data['upgrade2_price_value'])
        upgrade3_price_value_text = format_number(data['upgrade3_price_value'])
        upgrade4_price_value_text = format_number(data['upgrade4_price_value'])

        #--------Upgrade MAX--------#
        if data['upgrade1_lvl_value'] == 100 or data['upgrade1_lvl_value'] == "Max":
            data['upgrade1_lvl_value'] = "Max"
            upgrade1_price_value_text = "Max"
        if data['upgrade2_lvl_value'] == 100 or data['upgrade2_lvl_value'] == "Max":
            data['upgrade2_lvl_value'] = "Max"
            upgrade2_price_value_text = "Max"
        if data['upgrade3_lvl_value'] == 100 or data['upgrade3_lvl_value'] == "Max":
            data['upgrade3_lvl_value'] = "Max"
            upgrade3_price_value_text = "Max"
        if data['upgrade4_lvl_value'] == 100 or data['upgrade4_lvl_value'] == "Max":
            data['upgrade4_lvl_value'] = "Max"
            upgrade4_price_value_text = "Max"

        upgrade1_lvl = font_small.render('lvl'+str(data['upgrade1_lvl_value']), True, (0,0,0))
        upgrade1_price = font_small.render(f'{upgrade1_price_value_text}', True, (0,0,0))
        upgrade2_lvl = font_small.render('lvl'+str(data['upgrade2_lvl_value']), True, (0,0,0))
        upgrade2_price = font_small.render(f'{upgrade2_price_value_text}', True, (0,0,0))
        upgrade3_lvl = font_small.render('lvl'+str(data['upgrade3_lvl_value']), True, (0,0,0))
        upgrade3_price = font_small.render(f'{upgrade3_price_value_text}', True, (0,0,0))
        upgrade4_lvl = font_small.render('lvl'+str(data['upgrade4_lvl_value']), True, (0,0,0))
        upgrade4_price = font_small.render(f'{upgrade4_price_value_text}', True, (0,0,0))
        booster_counter = font_small.render(''+str(data['booster_count'])+'', True, (0,0,0))

        #-------Upgrade Area--------#
        side_bar1.draw(screen)
        side_bar2.draw(screen)
        #Upgrade1
        if data['upgrade1_lvl_value'] != "Max":
            if data['upgrade1_lvl_value'] < 100:
                if data['magic_faeces_value'] >= data['upgrade1_price_value']:
                    if upgrade_button1.draw(screen):
                        #upgrade_sound.play()
                        data['magic_faeces_value'] -= data['upgrade1_price_value']
                        data['upgrade1_lvl_value'] += 1
                        data['upgrade1_price_value']=int(data['upgrade1_price_value']*1.3)
                        data['increase_rate']=int(data['increase_rate']*1.3)
                        data['faeces_per_click']=int(data['faeces_per_click']*1.2)
                        if data['upgrade1_lvl_value'] % 10 == 0:
                            data['booster_count'] += 1
                else:
                    upgrade_button_no_1.draw(screen)
        else:
            upgrade_button_max_1.draw(screen)
            upgrade1_max = True

        #Upgrade2
        if data['upgrade2_lvl_value'] != "Max":
            if data['upgrade2_lvl_value'] < 100:
                if data['magic_faeces_value'] >= data['upgrade2_price_value']:
                    if upgrade_button2.draw(screen):
                        #upgrade_sound.play()
                        data['magic_faeces_value'] -= data['upgrade2_price_value']
                        data['upgrade2_lvl_value'] += 1
                        data['upgrade2_price_value']=int(data['upgrade2_price_value']*1.3)
                        data['increase_rate']=int(data['increase_rate']*1.3)
                        data['faeces_per_click']=int(data['faeces_per_click']*1.2)
                        if data['upgrade2_lvl_value'] % 10 == 0:
                            data['booster_count'] += 1
                else:
                    upgrade_button_no_2.draw(screen)
        else:
            upgrade_button_max_2.draw(screen)
            upgrade2_max = True

        #Upgrade3
        if data['upgrade3_lvl_value'] != "Max":
            if data['upgrade3_lvl_value'] < 100:
                if data['magic_faeces_value'] >= data['upgrade3_price_value']:
                    if upgrade_button3.draw(screen):
                        #upgrade_sound.play()
                        data['magic_faeces_value'] -= data['upgrade3_price_value']
                        data['upgrade3_lvl_value'] += 1
                        data['upgrade3_price_value']=int(data['upgrade3_price_value']*1.3)
                        data['increase_rate']=int(data['increase_rate']*1.3)
                        data['faeces_per_click']=int(data['faeces_per_click']*1.2)
                        if data['upgrade3_lvl_value'] % 10 == 0:
                            data['booster_count'] += 1
                else:
                    upgrade_button_no_3.draw(screen)
        else:
            upgrade_button_max_3.draw(screen)    
            upgrade3_max = True

        #Upgrade4
        if data['upgrade4_lvl_value'] != "Max":
            if data['upgrade4_lvl_value'] < 100:
                if data['magic_faeces_value'] >= data['upgrade4_price_value']:
                    if upgrade_button4.draw(screen):
                        #upgrade_sound.play()
                        data['magic_faeces_value'] -= data['upgrade4_price_value']
                        data['upgrade4_lvl_value'] += 1
                        data['upgrade4_price_value']=int(data['upgrade4_price_value']*1.3)
                        data['increase_rate']=int(data['increase_rate']*1.3)
                        data['faeces_per_click']=int(data['faeces_per_click']*1.2)
                        if data['upgrade4_lvl_value'] % 10 == 0:
                            data['booster_count'] += 1
                else:
                    upgrade_button_no_4.draw(screen)
        else:
            upgrade_button_max_4.draw(screen)     
            upgrade4_max = True
        
        #-------Main Button Area--------#
        if button.draw(screen):
            #nyah.play()
            faeces_per_click_text = format_number(data['faeces_per_click'])
            list_of_falling_number.append(DropAnimation(random.randint(300,430), 240,(font.render(f'{faeces_per_click_text}', True, (0,0,0)))))
            data['magic_faeces_value'] += data['faeces_per_click']

        increase_timer += 1
        if increase_timer >= 60:
            increase_rate_text = format_number(data['increase_rate'])
            list_of_falling_number.append(DropAnimation(random.randint(300,430), 240,(font_small.render(f'{increase_rate_text}', True, (0,0,0)))))
            data['magic_faeces_value'] += data['increase_rate']
            increase_timer = 0

        if len(list_of_falling_number) > 0:
            for falling_number in list_of_falling_number:
                falling_number.draw(screen)
                falling_number.animate(list_of_falling_number)
        
        #------BoostMode-------#
        screen.blit(booster_counter,((12,515)))
        if boost_mode == False :
            if data['booster_count'] > 0:
                if boost_button.draw(screen):
                    #roar.play()
                    boost_mode = True
                    data['booster_count'] -= 1

        elif booster_timer < 250:
            if booster_timer % 4 == 0:
                faeces_per_click_text = format_number(data['faeces_per_click'])
                list_of_falling_number.append(DropAnimation(random.randint(300,430), 240,(font.render(f'{faeces_per_click_text}', True, (0,0,0)))))
                data['magic_faeces_value'] += data['faeces_per_click']
            booster_timer+=1
        else:
            boost_mode=False
            booster_timer = 0

        #----------Render Area----------#
        mushroom1.draw(screen)
        mushroom2.draw(screen)
        mushroom3.draw(screen)
        mushroom4.draw(screen)
        score_board.draw(screen)
        screen.blit(score, (300, 30))
        screen.blit(upgrade1_lvl, (680, 135))
        screen.blit(upgrade1_price, (680, 170))
        screen.blit(upgrade2_lvl, (680, 245))
        screen.blit(upgrade2_price, (680, 280))
        screen.blit(upgrade3_lvl, (680, 355))
        screen.blit(upgrade3_price, (680, 390))
        screen.blit(upgrade4_lvl, (680, 465))
        screen.blit(upgrade4_price, (680, 500))

        if upgrade1_max == True and upgrade2_max == True and upgrade3_max == True and upgrade4_max == True:
            if continue_button.draw(screen):
                game_state = 'ending'

    if game_state == "ending":
        screen.fill((250, 236, 228))
        animation_list = []
        for x in range(15):
            animation_list.append(sleep_dragon_sprite.get_frame(x,480,480,1,(0,0,0)))
        animation_timer += 1
        if animation_timer >= 5:
            ending_frame += 1
            animation_timer = 0
        if ending_frame >= len(animation_list):
            ending_frame = 0
        animation_list[ending_frame]= pygame.transform.scale(animation_list[ending_frame],(300,300)).convert_alpha()
        screen.blit(animation_list[ending_frame], (250,200))

        animation_list = []
        for x in range(3):
            animation_list.append(thanksforplaying.get_frame(x,480,421,1,(0,0,0)))
        ending_timer += 1
        if ending_timer >= 10:
            frame += 1
            ending_timer = 0
        if frame >= len(animation_list):
            frame = 0
        animation_list[frame]= pygame.transform.scale(animation_list[frame],(250,220)).convert_alpha()
        screen.blit(animation_list[frame], (260,30))

        if newgames_button.draw(screen):
            data['magic_faeces_value'] = 0
            data['upgrade1_lvl_value'] = 1
            data['upgrade1_price_value'] = 1000
            data['upgrade2_lvl_value'] = 1
            data['upgrade2_price_value'] = 100000
            data['upgrade3_lvl_value'] = 1
            data['upgrade3_price_value'] = 10000000
            data['upgrade4_lvl_value'] = 1
            data['upgrade4_price_value'] = 1000000000
            data['faeces_per_click'] = 200
            data['increase_rate'] = 10
            data['booster_count'] = 10
            game_state = 'menu'
            upgrade1_max = False
            upgrade2_max = False
            upgrade3_max = False
            upgrade4_max = False
            name = ""
            password = ""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('save.txt','w') as save_file:
                json.dump(data,save_file)
            run = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()