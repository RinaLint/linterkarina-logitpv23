import pygame
pygame.init() #Pygame´i tööle rakendamiseks
ekraani_pind=pygame.display.set_mode((640,480)) #akna pind, 640 on akna laius, 480-kõrgus
ekraani_pind.fill((0,0,255)) #värvime tekitatud pinna siniseks
pygame.display.set_caption("Minu esimine aken")

ristkylik1=pygame.Rect(0,380,640,480) #Argumentid: x koordinat, y koordinat, laius, kõrgus.
pygame.draw.rect(ekraani_pind,(0,255,0),ristkylik1) #surface, color, Rect

center_cordinates=(60,60)
radius=40
pygame.draw.circle(ekraani_pind, (255,255,0), center_cordinates, radius )

pilt1=pygame.image.load("sipsik.xcf")
pilt1=pygame.transform.scale(pilt1,(170,160))
ekraani_pind.blit(pilt1, (200,100)) #pilt1 (x,y)

tekst="Tere, Pygame!"
meie_font=pygame.font.SysFont("Verdana",36)
teksti_pilt=meie_font.render(tekst, False, (250,250,100))
ekraani_pind.blit(teksti_pilt,(300,30))

pygame.display.flip() #soovime pilt kasutajale näidata
while True:
    event=pygame.event.poll() #lõpmatu tsükel, mis igas sammus loeb kasutajalt sisendeid muutujasse event ning kontollib seejärel, kas kasutaja soovib programmi sulgeda
    if event.type==pygame.QUIT:
        break
pygame.quit() #Pygame välja lülitamine


#joon (line): pygame.draw.line(aken, värv, algus_pos, lõpp_pos, paksus)
#ristkülik (rect): pygame.draw.rect(screen, värv, [x, y, w, h], joone_paksus)

#hulknurk (polygon): pygame.draw.polygon(screen, värv, koordinaatide_loend, joone_paksus)
#ovaal (ellipse): pygame.draw.ellipse(screen, värv, [x, y, r1, r2], joone_paksus)
#kaar (arc): pygame.draw.arc(screen, värv, ristküliku_koordinaadid, start_nurk, lõpp_nurk, joone_paksus)