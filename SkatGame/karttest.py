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

# Spieler-Kartenlisten
player1_card = []
player2_card = []
player3_card = []




class Card:
    def __init__(self, image, pos, value):
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.value = value

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def can_be_placed_on(self, other_card):
        return self.value[0] == other_card.value[0] or self.value[1] == other_card.value[1]


def sort_cards(player_cards):
    # Karten sortieren anhand ihrer definierten Reihenfolge
    return sorted(player_cards, key=lambda a_card: cards.card_order[a_card.image])


def deal_cards():
    # Eine zufällige Karte austeilen und aus dem Deck entfernen
    a_card = random.choice(cards.cards)
    if a_card in cards.cards:
        cards.cards.remove(a_card)
    return a_card


# Mischen der cards
random.shuffle(cards.cards)

# cards an die Spieler austeilen
for i in range(10):
    # Zuteilen der Karten an Spieler 1
    card1 = deal_cards()
    player1_card.append(Card(card1, (450 + i * 80, 820), cards.card_order[card1]))

    # Zuteilen der Karten an Spieler 2
    card2 = deal_cards()
    player2_card.append(Card(card2, (-120, 200 + i * 50), cards.card_order[card2]))

    # Zuteilen der Karten an Spieler 3
    card3 = deal_cards()
    player3_card.append(Card(card3, (1670, 200 + i * 50), cards.card_order[card3]))

# Die restlichen Karten im Skat
skat = [Card(card, (800 + i * 50, 350), cards.card_order[card]) for i, card in enumerate(cards.cards)]

# Hauptspielschleife
running = True
selected_card = None

while running:
    SCREEN.fill(COLOR)

    # Ereignisse abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for card in player1_card:
                if card.is_clicked(mouse_pos):
                    if selected_card:
                        # Logik zur Überprüfung, ob die Karte gelegt werden kann
                        if selected_card.can_be_placed_on(card):
                            print(f"Karte {selected_card.value} kann auf {card.value} gelegt werden.")
                        selected_card = None
                    else:
                        selected_card = card

    # Karten für jeden Spieler zeichnen
    for card in player1_card:
        card.draw(SCREEN)
    for card in player2_card:
        card.draw(SCREEN)
    for card in player3_card:
        card.draw(SCREEN)
    for card in skat:
        card.draw(SCREEN)

    # Bildschirm aktualisieren
    pygame.display.flip()
    clock.tick(20)

pygame.quit()