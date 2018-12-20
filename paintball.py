from asset.annex import *
import cv2
import pygame
from pygame.locals import *
import sys
from random import randint

pygame.init()
cap = cv2.VideoCapture(0)
surf = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Hit Yourself')
soundEffect = pygame.mixer.Sound('asset/soundeffect.wav')
soundEffect.set_volume(1)
pygame.mouse.set_cursor(*pygame.cursors.diamond)
clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT,3000)
imgList =[]
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imwrite('asset/image.png', frame)
    img = pygame.image.load('asset/image.png')
    surf.blit(img,(0,0))
    for i in imgList :
        showImage2(surf,i[0],i[1],i[2])
    for event in pygame.event.get():
        if event.type == QUIT :
            cap.release()
            cv2.destroyAllWindows()
            pygame.quit()
            sys.exit()
        if event.type == USEREVENT :
            if imgList != [] :
                imgList.remove(imgList[0])
        if event.type == MOUSEBUTTONDOWN :
            soundEffect.play()
            imgSrc = 'asset/paint'+str(randint(0,6))+'.png'
            x,y = event.pos
            angle = randint(0,360)
            imgList.append([imgSrc,(x,y),angle])
    pygame.display.flip()
    clock.tick(60)        
    pygame.display.update()
    



