import pygame
import math
from random import randint
from sklearn import cluster
from sklearn.cluster import KMeans

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))

pygame.init()

screen=pygame.display.set_mode((1200,700))

BACKGROUND=(214,214,214)
WHITE=(255,255,255)
BLACK=(0,0,0)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (147, 153, 35)
PURPLE = (255,0,255)
SKY = (0,255,255)
ORANGE = (255,125,25)
GRAPE = (100,25,125)
GRASS = (55,155,65)

colors=[RED,GREEN,BLUE,YELLOW,PURPLE,SKY,ORANGE,GRAPE,GRASS]

font=pygame.font.SysFont('sans',40)
text_plus=font.render('+',True,WHITE)
text_minus=font.render('-',True,WHITE)
text_run=font.render('Run',True,WHITE)
text_random=font.render('RanDom',True,WHITE)
text_algorithm=font.render('Algorithm',True,WHITE)
text_Reset=font.render('Reset',True,WHITE)

clock=pygame.time.Clock()

pygame.display.set_caption("GUI for Kmeans")

K=0
error=0
points=[]
labels=[]
clusters=[]

running=True
while running:
    clock.tick(60)
    mouse_x,mouse_y=pygame.mouse.get_pos()
    screen.fill(BACKGROUND)
    #draw panel
    pygame.draw.rect(screen,BLACK,(50,50,700,500))
    pygame.draw.rect(screen,WHITE,(55,55,690,490))

    #draw button +
    pygame.draw.rect(screen,BLACK,(850,50,50,50))
    screen.blit(text_plus,(865,50))
    #draw button -
    pygame.draw.rect(screen,BLACK,(950,50,50,50))
    screen.blit(text_minus,(970,50))
    #draw button K
    text_K=font.render('K = '+ str(K),True,BLACK)
    screen.blit(text_K,(1050,50))
    #draw button Run
    pygame.draw.rect(screen,BLACK,(850,150,150,50))
    screen.blit(text_run,(900,150))
    #draw button Random
    pygame.draw.rect(screen,BLACK,(850,250,150,50))
    screen.blit(text_random,(850,250))
    #draw button algorithm
    pygame.draw.rect(screen,BLACK,(850,450,150,50))
    screen.blit(text_algorithm,(850,450))
    #draw button reset
    pygame.draw.rect(screen,BLACK,(850,550,150,50))
    screen.blit(text_Reset,(850,550))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # panel
            if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                labels=[]
                points.append([mouse_x-50,mouse_y-50])
                
            # button +
            if 850 < mouse_x < 900 and 50 < mouse_y < 100:
                if K < 8:
                    K += 1
            # button -
            if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
                if K > 0:
                    K -= 1
            # change button Run
            if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
                labels=[]
                if clusters == []:
                    continue
                for p in points:
                    distance_to_clusters=[]
                    for c in clusters:
                        dis=distance(p,c)
                        distance_to_clusters.append(dis)
                    min_distance=min(distance_to_clusters)
                    label=distance_to_clusters.index(min_distance)
                    labels.append(label)
                    
                # fixed label , update cluster
                for i in range(K):
                    sum_x=0
                    sum_y=0
                    count=0
                    for j in range(len(points)):
                        if labels[j]==i:
                            sum_x += points[j][0]
                            sum_y += points[j][1]
                            count +=1
                    if count != 0:
                        new_cluster_x=sum_x/count
                        new_cluster_y=sum_y/count
                        clusters[i]=[new_cluster_x,new_cluster_y]

            # change button Random
            if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
                labels = []
                clusters=[]
                for i in range(K):
                    random_point=[randint(0,700),randint(0,500)]
                    clusters.append(random_point)
            # change button reset
            if 850< mouse_x < 1000 and 550 < mouse_y < 600:
                K = 0
                points = []
                labels = []
                clusters = []
                error = 0
            # change button algorithm
            if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
                try:
                    kmeans=KMeans(n_clusters=K).fit(points)
                    labels=kmeans.predict(points)
                    clusters=kmeans.cluster_centers_
                except:
                    print("Error")

    

    #draw clusters
    for i in range(len(clusters)):
        pygame.draw.circle(screen,colors[i],(int(clusters[i][0])+50,int(clusters[i][1])+50),10)    
    # draw points
    for i in range(len(points)):
        pygame.draw.circle(screen,BLACK,(points[i][0]+50,points[i][1]+50),6)
        if labels == []:
            pygame.draw.circle(screen,WHITE,(points[i][0]+50,points[i][1]+50),5)
        else:
            pygame.draw.circle(screen,colors[labels[i]],(points[i][0]+50,points[i][1]+50),6)
    #draw error
    error = 0
    if labels != [] and clusters != []:
        for i in range(len(points)):
            error += distance(points[i],clusters[labels[i]])

    text_error=font.render('Distance = ' + str(int(error)),True,BLACK)
    screen.blit(text_error,(850,350))     
    pygame.display.flip()
pygame.quit()
