import pygame
def renderImage(surface,imgSrc,pos,angle = 0):
    image = pygame.image.load(imgSrc)
    image = pygame.transform.rotate(image,angle)
    imageRect = image.get_rect()
    imageRect.center = pos
    surface.blit(image, imageRect)
    return([imageRect.topleft,imageRect.bottomright])

def showImage(surface,imgSrc,pos,angle = 0,brightness = 255):
    image = pygame.image.load(imgSrc).convert()
    image = pygame.transform.rotate(image,angle)
    image.set_alpha(brightness)
    image.set_colorkey((0,0,0))
    imageRect = image.get_rect()
    imageRect.center = pos
    surface.blit(image, imageRect)
def showImage2(surface,imgSrc,pos,angle = 0):
    image = pygame.image.load(imgSrc)
    image = pygame.transform.rotate(image,angle)
    imageRect = image.get_rect()
    imageRect.center = pos
    surface.blit(image, imageRect)
