import random
import pygame
import cards

pygame.init()
X = 1800
Y = 1000
SCREEN = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Kartenspiel by Zunovic")
COLOR = (0, 70, 50)
pygame.display.set_icon(cards.KREUZ)
pygame.Surface.fill(SCREEN, COLOR)
clock = pygame.time.Clock()
player1_card = []
player2_card = []
player3_card = []


def sort_cards(player_cards):
    return sorted(player_cards, key=lambda a_card: cards.card_order[a_card])


def deal_cards():
    a_card = random.choice(cards.cards)
    if a_card in cards.cards:
        cards.cards.remove(a_card)
    return a_card


random.shuffle(cards.cards)

for i in range(10):
    player1_card.append(deal_cards())
    player2_card.append(deal_cards())
    player3_card.append(deal_cards())

skat = cards.cards
player1_card = sort_cards(player1_card)
player2_card = sort_cards(player2_card)
player3_card = sort_cards(player3_card)
skat = sort_cards(skat)


for index, card in enumerate(player1_card):
    SCREEN.blit(card, (450 + index * 80, 820))

for index, card in enumerate(player2_card):
    rotate = pygame.transform.rotate(cards.BACK, 90)
    card = pygame.transform.rotate(card, 90)
    SCREEN.blit(rotate, (-120, 200 + index * 50))

for index, card in enumerate(player3_card):
    rotate = pygame.transform.rotate(cards.BACK, 90)
    card = pygame.transform.rotate(card, 90)
    SCREEN.blit(rotate, (1670, 200 + index * 50))

for index, card in enumerate(skat):
    SCREEN.blit(cards.BACK, (800 + index * 50, 350))

a = True
while a:
    pygame.display.flip()
    #  Karten in Variable werden enumeriert und nebeneinander platziert
    # Userinput
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)

pygame.quit()
