import pygame, sys, random
from game import Game
from Story import Story
from spaceship import Spaceship

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)

font = pygame.font.Font("Fonts/Manrope/Manrope-SemiBold.ttf", 20)
alt_font = pygame.font.Font("Fonts/Short_Stack/ShortStack-Regular.ttf", 20)
fin_font = pygame.font.Font("Fonts/English_Vivace_BT/english111_vivace_BT.ttf", 60)

level_surface = font.render("Move with <- and -> ; space to shoot", True, WHITE)
game_over_surface = font.render("Game Over. Press ENTER to retry", True, RED)
relive_surface = font.render("Game Over. Press ENTER to Relive", True, RED)

level_rect = level_surface.get_rect()
level_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Unbound")

background_image = pygame.image.load("Graphics/space-stars-texture.webp")
scaled_image = pygame.transform.scale(background_image, (750, 700))

base_lives = pygame.image.load("Graphics/charge.png")
scaled_lives = pygame.transform.scale(base_lives, (32, 32))

arrow_image = pygame.image.load("Graphics/arrow.png")

clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)

shoot_laser = pygame.USEREVENT
big_alien_shoot_laser = pygame.USEREVENT + 1
mystery_ship = pygame.USEREVENT + 2
boss_shoot_laser = pygame.USEREVENT + 3

pygame.time.set_timer(big_alien_shoot_laser, 275)
pygame.time.set_timer(mystery_ship, random.randint(6000, 8000))
pygame.time.set_timer(boss_shoot_laser, 250)

story_text_1 = [
    ("...starting android\n...memory restored\n...vitals OK\nstatus: Online\n\n\n\n\n\n\n\n\n\n\n                                                                                          (Enter)", alt_font),
    ("Eren: Uh... my head. Where am I? What's going on? It's all a blur.", font),
    ("*access memory*\n...fetching data...\n...found 1 item\nGoal: Rescue Leia from Casper, currently on planet 9.", alt_font),
    ("Eren: Leia! I remember now. Our home, the attack... he took her and dumped\nme here. My spaceship... there it is! Huh, I remember it getting damaged,\nbut it's good as new. All the better! Let's get out of here.\nHold on Leia, *set destination: planet 9... set!* *activate shields... activated!*\n I'm on my way.", font)
]

story_text_2 = [
    ("*Eren ploughs through several waves of Casper's minions until\nhe gets to the tower where Leia is held captive*", alt_font),
    ("Eren: Almost there. It's strange though. I feel like I'm being controlled\nby someone else. But that is not important right now.\nHere I come Casper, you'll pay for what you've done!", font),
    ("*As Eren approaches the planet surface near the tower,\nhe is suddenly ambushed by a fleet, led by Casper.*", alt_font),
    ("Casper: ...You made it till here again. You're getting used to\nthis. Perhaps I'll increase our damage output next time...", alt_font),
    ("Casper:Oh, let's skip my monologue (I've done it far too many times).\nYou're here to fight aren't you? Kill me, Rescue Leia?\nI've got to admit, this part never gets old! Let's Fight!", font)
]

story_text_3 = [
    ("*Eren rushes inside the tower where he sees Leia*", alt_font),
    ("Eren: Leia!", font),
    ("*They run towards each other and embrace. Eren is relieved\nas he hugs her tightly. But he notices Leia crying.*", alt_font),
    ("Eren: Hey, what's wrong? I'm here, we can go home now. Casper's dead.", font),
    ("Leia: We can't. This is his game. What you killed outside was\n merely his projection. We can't beat him.", font),
    ("Erne: What?!", font),
    ("Leia: It's all a cruel joke. You wake up, remember me, fight your way here,\ndie, resurrect and repeat.", font),
    ("Eren: What do you mean?", font),
    ("Leia: Your code was altered by Casper on the day of the attack. You are\nprogrammed to kill yourself every time you meet me. And all I can do\nis watch. I can't even step out of this tower. My program won't let me.\nThat is my punishment for rejecting his proposal.To watch my love die for an\neternity. And everytime you die, he resurrects you with the memory\nof the attack, an intact spaceship and a singular goal: to rescue me.\nAnd thus the cycle repeats.", font),
    ("*Eren hugs Leia again as she starts sobbing*", alt_font),
    ("Eren: No, we'll get out of this. I promise.", font),
    ("*Leia hugs him back*", alt_font),
    ("Leia: It's no use Eren. You won't remember this when you wake up again.\nYou'll only see your goal and remember me. And he watches your\n futile attempts with pleasure. That is all this is to him. A show.", font),
    ("*There is silence for a moment*", alt_font),
    ("Eren: No. It's different this time. I've been feeling it since I woke up.\nMy actions... they're not entirely my own. It's like someone... or\nsomething, is controlling me. A higher power. Maybe it can help us.", font),
    ("Leia: I lost all hope of escaping this torment long ago. But seeing the sparkle\nin your eyes.... if what you're saying is true, then please, whoever you are\nout there, help us. Casper's only weakness is his ego. He is a cunning\ngenius and will never face Eren head on, as long as he obeys his command.\nKilling the droids, facing his projection, rescuing me and dying - Eren is\nprogrammed to repeat these tasks. Force Casper to face Eren by\nbreaking this loop. Please. You are our only hope.", font),
    ("*Suddenly, it's as though Erens sentience is taken from him.\nHe stares off into space for a while, takes out his sword,\nand plunges it through his chest, breaking the core chip\ninto pieces. With the voice of a woman crying in the\nbackground, his vision fades*\n\n\n\n\n\n\n\nPress ENTER to Relive", alt_font),
]

story_text_4 = [
    ("*A deep rumbling sound emanates from a distance, getting\nlouder by the second until a huge battleship comes into view.*", alt_font),
    ("Casper: Well well well, isn't this a surprise. What's wrong little one?\nForgot how to fire bullets? Must be a bug in your code.\nHand it over, your core chip. Let me fix it.", font),
    ("*Casper enters some command into a terminal on his\nship and looks at you expectantly*", alt_font),
    ("Eren: Casper! Release Leia or get ready to die!", font),
    ("*Casper is visibly surprised as he sees Eren ready his\nbattleship weapon.*", alt_font),
    ("Casper: Why you little... how dare you disobey me! Wait, how can you\ndisobey me? And you know how to use the guns too. Then why didn't you...?\nNo, it's not possible. ", font),
    ("*He seems lost in though for a moment, like he's trying to\nrationalize the situation in his mind*", alt_font),
    ("Casper: Ah, it must be quite a major bug. No matter. I'll fix it once I get\nhold of it... and as a bonus, I'll add some new features that'll make your\njourney a little more painful next time. It's getting a bit stale watching\nyour same pathetic attempt every time, heh heh heh. But for\nall that, I'll need your core chip, which means I have to kill you!", font)
]

story_text_5 = [
    ("*Having beaten Casper, Eren rushes to the battleships terminal,\ndisabling the droids and recompiling the default code for himself\nand Leia.He then gets on his ship and rushes to planet 9.*", alt_font),
    ("*Arriving there, he sees Leia on the surface, already outside\nthe tower and waiting for him.*", alt_font),
    ("Eren: Leia!\nLeia: Eren!", font),
    ("*They heartily embrace each other.*", alt_font),
    ("Eren: We're finally free! We can go home now.", font),
    ("Leia: Yes, you did it Eren! I'm so glad.", font),
    ("*After celebrating for some more time, they walk towards\nEren's battleship to get back home*", alt_font),
    ("*As they walk, Leia looks towards the sky, whispering to herself*", alt_font),
    ("Leia: Thank you kindly, whoever you are.\n This wouldn't have been possible without you.", alt_font),
    ("\n\n\n\n\n\n\nFin", fin_font)
]

story = Story(screen, story_text_1, arrow_image)
display_story = True

fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
fade_surface.fill((15, 15, 15))

def display_level_story(level_text):
    global display_story, story
    story = Story(screen, level_text, arrow_image)
    display_story = True
    while display_story:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if story.is_last_text():
                        if level_text == story_text_5:
                            pygame.quit()
                            print("Intentional exit. Game complete.")
                            sys.exit()
                        display_story = False
                        game.run = True
                        if level_text == story_text_1:
                            spaceship.start_timer()
                            print("Timer started")
                        pygame.time.set_timer(shoot_laser, 300)
                    else:
                        story.next_text()
        story.draw()
        pygame.display.update()
        clock.tick(60)

def fade_in(screen, fade_surface, fade_speed=8):
    fade_alpha = 255
    fade_surface.set_alpha(fade_alpha)
    while fade_alpha >= 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()

        fade_alpha -= fade_speed
        clock.tick(FPS)

fade_in(screen, fade_surface)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == shoot_laser and game.run:
            game.alien_shoot_laser()
        if event.type == big_alien_shoot_laser and game.run:
            game.big_alien_laser()
        if event.type == mystery_ship:
            game.create_mystery_ship()
            pygame.time.set_timer(mystery_ship, random.randint(6000, 8000))
        if event.type == boss_shoot_laser and game.run:
            game.boss_laser()

        if event.type == pygame.KEYDOWN:
            if display_story:
                if event.key == pygame.K_RETURN:
                    if story.is_last_text():
                        display_story = False
                        fade_in(screen, fade_surface)
                        game.run = True
                        spaceship.start_timer()
                        pygame.time.set_timer(shoot_laser, 300)
                    else:
                        story.next_text()
            else:
                key = pygame.key.get_pressed()
                if key[pygame.K_RETURN] and not game.run:
                    spaceship.timer_enabled = True
                    print("Timer enabled")
                    fade_in(screen, fade_surface)
                    display_level_story(story_text_1)
                    fade_in(screen, fade_surface)
                    game.reset()

    if spaceship.timer_expired:
        spaceship.reset_timer()
        spaceship.stop_timer()
        print("Timer expired")
        fade_in(screen, fade_surface)
        display_level_story(story_text_4)
        fade_in(screen, fade_surface)
        game.secret_level()

    if display_story:
        story.draw()
    else:
        if game.run:
            game.spaceship_group.update()
            game.move_aliens()
            game.alien_lasers_group.update()
            game.mystery_ship_group.update()
            game.check_for_collisions()
            spaceship.update()

        #screen.fill(GREY)
        screen.blit(scaled_image, (0, 0))

        if game.run:
            screen.blit(level_surface, level_rect)
        else:
            screen.blit(game_over_surface, level_rect)

        x = 10
        for life in range(game.lives):
            screen.blit(scaled_lives, (x, 10))
            x += 32

        game.spaceship_group.draw(screen)
        game.spaceship_group.sprite.lasers_group.draw(screen)
        for obstacle in game.obstacles:
            obstacle.blocks_group.draw(screen)
        game.aliens_group.draw(screen)
        game.alien_lasers_group.draw(screen)
        game.mystery_ship_group.draw(screen)

    pygame.display.update()
    clock.tick(60)

    if game.level_complete():
        if game.level == 1:
            fade_in(screen, fade_surface)
            display_level_story(story_text_2)
            fade_in(screen, fade_surface)
            game.next_level()
        elif game.level == 2:
            fade_in(screen, fade_surface)
            display_level_story(story_text_3)
            fade_in(screen, fade_surface)
            spaceship.timer_enabled = True
            print("Timer enabled")
            fade_in(screen, fade_surface)
            display_level_story(story_text_1)
            fade_in(screen, fade_surface)
            game.reset()
        elif game.level == 10:
            fade_in(screen, fade_surface)
            display_level_story(story_text_5)
            fade_in(screen, fade_surface)


