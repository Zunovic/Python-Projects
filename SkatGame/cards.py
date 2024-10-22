import pygame

KREUZBUBE = pygame.image.load('G4/1_1.gif')
PIKBUBE = pygame.image.load('G4/1_2.gif')
HERZBUBE = pygame.image.load('G4/1_3.gif')
KAROBUBE = pygame.image.load('G4/1_4.gif')
KREUZASS = pygame.image.load('G4/2_1.gif')
PIKASS = pygame.image.load('G4/2_2.gif')
HERZASS = pygame.image.load('G4/2_3.gif')
KAROASS = pygame.image.load('G4/2_4.gif')
KREUZ10 = pygame.image.load('G4/3_1.gif')
PIK10 = pygame.image.load('G4/3_2.gif')
HERZ10 = pygame.image.load('G4/3_3.gif')
KARO10 = pygame.image.load('G4/3_4.gif')
KREUZKNG = pygame.image.load('G4/4_1.gif')
PIKKNG = pygame.image.load('G4/4_2.gif')
HERZKNG = pygame.image.load('G4/4_3.gif')
KAROKNG = pygame.image.load('G4/4_4.gif')
KREUZDAME = pygame.image.load('G4/5_1.gif')
PIKDAME = pygame.image.load('G4/5_2.gif')
HERZDAME = pygame.image.load('G4/5_3.gif')
KARODAME = pygame.image.load('G4/5_4.gif')
KREUZ9 = pygame.image.load('G4/6_1.gif')
PIK9 = pygame.image.load('G4/6_2.gif')
HERZ9 = pygame.image.load('G4/6_3.gif')
KARO9 = pygame.image.load('G4/6_4.gif')
KREUZ8 = pygame.image.load('G4/7_1.gif')
PIK8 = pygame.image.load('G4/7_2.gif')
HERZ8 = pygame.image.load('G4/7_3.gif')
KARO8 = pygame.image.load('G4/7_4.gif')
KREUZ7 = pygame.image.load('G4/8_1.gif')
PIK7 = pygame.image.load('G4/8_2.gif')
HERZ7 = pygame.image.load('G4/8_3.gif')
KARO7 = pygame.image.load('G4/8_4.gif')
BACK = pygame.image.load('G4/back.gif')
KREUZ = pygame.image.load('G4/clubs.gif')
PIK = pygame.image.load('G4/spades.gif')
HERZ = pygame.image.load('G4/hearts.gif')
KARO = pygame.image.load('G4/diamonds.gif')

sort_order = {
    'BUBE': 1,
    'KREUZ': 2,
    'PIK': 3,
    'HERZ': 4,
    'KARO': 5,
}

card_order = {
    KREUZBUBE: (sort_order['BUBE'], 1),
    PIKBUBE: (sort_order['BUBE'], 2),
    HERZBUBE: (sort_order['BUBE'], 3),
    KAROBUBE: (sort_order['BUBE'], 4),
    KREUZASS: (sort_order['KREUZ'], 1),
    PIKASS: (sort_order['PIK'], 1),
    HERZASS: (sort_order['HERZ'], 1),
    KAROASS: (sort_order['KARO'], 1),
    KREUZ10: (sort_order['KREUZ'], 2),
    PIK10: (sort_order['PIK'], 2),
    HERZ10: (sort_order['HERZ'], 2),
    KARO10: (sort_order['KARO'], 2),
    KREUZKNG: (sort_order['KREUZ'], 3),
    PIKKNG: (sort_order['PIK'], 3),
    HERZKNG: (sort_order['HERZ'], 3),
    KAROKNG: (sort_order['KARO'], 3),
    KREUZDAME: (sort_order['KREUZ'], 4),
    PIKDAME: (sort_order['PIK'], 4),
    HERZDAME: (sort_order['HERZ'], 4),
    KARODAME: (sort_order['KARO'], 4),
    KREUZ9: (sort_order['KREUZ'], 5),
    PIK9: (sort_order['PIK'], 5),
    HERZ9: (sort_order['HERZ'], 5),
    KARO9: (sort_order['KARO'], 5),
    KREUZ8: (sort_order['KREUZ'], 6),
    PIK8: (sort_order['PIK'], 6),
    HERZ8: (sort_order['HERZ'], 6),
    KARO8: (sort_order['KARO'], 6),
    KREUZ7: (sort_order['KREUZ'], 7),
    PIK7: (sort_order['PIK'], 7),
    HERZ7: (sort_order['HERZ'], 7),
    KARO7: (sort_order['KARO'], 7)
}

cards = [
    KREUZBUBE, PIKBUBE, HERZBUBE,
    KAROBUBE, KREUZASS, PIKASS,
    HERZASS, KAROASS, KREUZ10,
    PIK10, HERZ10, KARO10,
    KREUZKNG, PIKKNG, HERZKNG,
    KAROKNG, KREUZDAME, PIKDAME,
    HERZDAME, KARODAME, KREUZ9,
    PIK9, HERZ9, KARO9, KREUZ8,
    PIK8, HERZ8, KARO8, KREUZ7,
    PIK7, HERZ7, KARO7
]
