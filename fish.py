import pygame #on importe Pygame
pygame.init()#on initialise Pygame
ecran = pygame.display.set_mode((1360,720))#on crée une fenêtre avec le module display de Pygame, la fenêtre sera la taille de mon écran 
pygame.display.set_caption("Chassons-Poissons!")#on met le titre de notre fenetre grace au module display
image = pygame.image.load("bg2.png").convert_alpha() #on convertit notre image de type JPG en PNG
clock = pygame.time.Clock()
music=pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
#on fait convert et non convert.alpha car on a utiliser la fonsction img.set_alpha qui joue sur les pixels de la photo initiale

walkRight = [pygame.image.load("Fish/R1.png").convert(),
             pygame.image.load("Fish/R2.png").convert(),
             pygame.image.load("Fish/R3.png").convert(),
             pygame.image.load("Fish/R4.png").convert(),
             pygame.image.load("Fish/R5.png").convert(),
             pygame.image.load("Fish/R6.png").convert(),
             pygame.image.load("Fish/R7.png").convert(),
             pygame.image.load("Fish/R8.png").convert()]
walkLeft = [pygame.image.load("Fish/L1.png").convert(),
            pygame.image.load("Fish/L2.png").convert(),
            pygame.image.load("Fish/L3.png").convert(),
            pygame.image.load("Fish/L4.png").convert(),
            pygame.image.load("Fish/L5.png").convert(),
            pygame.image.load("Fish/L5.png").convert(),
            pygame.image.load("Fish/L7.png").convert(),
            pygame.image.load("Fish/L8.png").convert()]
char = pygame.image.load("Fish/R1.png")

class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5 #pq 5?
        self.left=False #tjrs la condition doit etre True pour entrer dans la boucle While doit etre True pour entrer dans la boucle
        self.right=False
        self.walkCount=0
        self.alpha = 255#comme on sait que les couleurs RVB vont de 0 a 255, alors on va jouer avec pour faire reapparaitre calmement le poisson
        self.vie=2
        self.walkRight=[pygame.image.load("Fish/R1.png"),
                        pygame.image.load("Fish/R2.png"),
                        pygame.image.load("Fish/R3.png"),
                        pygame.image.load("Fish/R4.png"),
                        pygame.image.load("Fish/R5.png"),
                        pygame.image.load("Fish/R6.png"),
                        pygame.image.load("Fish/R7.png"),
                        pygame.image.load("Fish/R8.png")]
        self.walkLeft=[pygame.image.load("Fish/L1.png"),
                       pygame.image.load("Fish/L2.png"),
                       pygame.image.load("Fish/L3.png"),
                       pygame.image.load("Fish/L4.png"),
                       pygame.image.load("Fish/L5.png"),
                       pygame.image.load("Fish/L5.png"),
                       pygame.image.load("Fish/L7.png"),
                       pygame.image.load("Fish/L8.png")]
                    
       
    #ici,on assume que le deplacement est vers la droite: alors on verifie si vel est une valeur positif d'apres def move puis si fish.x est <... :
    #on veut que fish.x soit en collision avec le shark(> car le vel de shark ou fish n'st pas fixe).
    #-3eme lgne est pour s'assurer qu'ils aient les memes coordonnes(pour collision)----
    #il y a 6 conditions(poisson droite et baleine droite...)
    #1ere(2):le requain=fish.x ou >:il l'a depasse    

    def perte (self,enemy):
        import random
        #avec and il faut que tout soit TRUE , alors si on a pas mis les parentheses,
        #il va pas fonctionner car les parentheses forcent le compilateur de les lire d'abord, comme en maths
        if self.width <= enemy.width or self.height <= enemy.height:
            
            if (enemy.vel > 0 and self.x < enemy.x + enemy.width and self.x>=enemy.x and ((self.y <= enemy.y + enemy.height and self.y >= enemy.y ) or (self.y+self.height>enemy.y and self.y<enemy.y))):
                self.vie-=1  
                self.x=random.randrange(90,1000)
                self.y=random.randrange(90,700)
            
            elif(enemy.vel < 0 and self.x+self.width > enemy.x and self.x<=enemy.x  and ((self.y <= enemy.y + enemy.height and self.y >= enemy.y ) or (self.y+self.height>enemy.y and self.y<enemy.y))):
                self.vie-=1
                self.x=random.randrange(90,1000)
                self.y=random.randrange(90,700)
            
            
            if self.vie ==0:
                print ("Game Over")

            elif(self.height> enemy.height and self.width>enemy.width):
                print ("Congratulation!")
        else:
            if (self.right and enemy.x < self.x + self.width and enemy.x>=self.x and ((enemy.y <= self.y + self.height and enemy.y >= self.y ) or (enemy.y+enemy.height>self.y and enemy.y<self.y))):
                enemy.vel=  0 #pour que le shark arrete de se deplacer
                enemy.x = -300
            
            elif(self.left and enemy.x+enemy.width > self.x and enemy.x<=self.x  and ((enemy.y <= self.y + self.height and enemy.y >= self.y ) or (enemy.y+enemy.height>self.y and enemy.y<self.y))):
                enemy.vel=  0
                enemy.x = -300
             
           
        
    def draw(self,ecran):
        
        if self.alpha < 255:
            self.alpha = self.alpha + 25            
        
        if self.walkcount+1>=24: #on va jamais utiliser cette boucle sans respecter la condition
           self.walkcount=0
           
        if self.left: #ici je verifie la variable
            img = walkLeft[self.walkcount//3]
            img.set_alpha(self.alpha)#fonction qui permet de changer alpha de cette photo et donc dans les couleurs (dans les pixels)
            ecran.blit(pygame.transform.scale(img, (self.width, self.height)),(self.x,self.y))  #En effet, j en tout 8 photos , et j choisi de faire 24 FPS alors je divise les 24/8=3: ansi chaque photo
                                                                                                        #apparaitra 3 fois. Le x et y sont les positions de la photo. 
                                                                                                        #Si je veux mettre 60FPS , je divisrai par 6.66 . De plus ,ex:1/3=0.3333
                                                                                                        #il prend juste la partie entiere (//)! et donc comme il s'agit d'un index il affichera la premiere photo
            self.walkcount+=1
        elif self.right:  #elle sera True selon la boucle while
            
            img = walkRight[self.walkcount//3]
            img.set_alpha(self.alpha)
            ecran.blit(pygame.transform.scale(img, (self.width,self.height)),(self.x,self.y))
            self.walkcount+=1
                  
        else: #c la 1ere chose qui va fonctionner car left et right sont False ! : le joueur sera en position standing
            img = walkRight[self.walkcount//3]
            img.set_alpha(self.alpha)
            ecran.blit(pygame.transform.scale(img, (self.width, self.height)),(self.x,self.y))
            self.walkcount=0
            

class enemy(object):
    walkLeft = [pygame.image.load('shark\R\R1.png'),pygame.image.load('shark\R\R2.png'),pygame.image.load('shark\R\R3.png'),
                pygame.image.load('shark\R\R4.png'),pygame.image.load('shark\R\R5.png'),pygame.image.load('shark\R\R6.png'),
                pygame.image.load('shark\R\R7.png'), pygame.image.load('shark\R\R8.png'),pygame.image.load('shark\R\R9.png'),
                pygame.image.load('shark\R\R10.png'), pygame.image.load('shark\R\R11.png'),pygame.image.load('shark\R\R12.png'),
                pygame.image.load('shark\R\R13.png'), pygame.image.load('shark\R\R14.png'), pygame.image.load('shark\R\R15.png'),
                pygame.image.load('shark\R\R16.png'),pygame.image.load('shark\R\R17.png'),pygame.image.load('shark\R\R18.png'),pygame.image.load('shark\R\R19.png')]
    walkRight = [pygame.image.load('shark\L\L1.png'), pygame.image.load('shark\L\L2.png'), pygame.image.load('shark\L\L3.png'),
                 pygame.image.load('shark\L\L4.png'), pygame.image.load('shark\L\L5.png'), pygame.image.load('shark\L\L6.png'),
                 pygame.image.load('shark\L\L7.png'), pygame.image.load('shark\L\L8.png'), pygame.image.load('shark\L\L9.png'),
                 pygame.image.load('shark\L\L10.png'), pygame.image.load('shark\L\L11.png'),pygame.image.load('shark\L\L12.png'),
                 pygame.image.load('shark\L\L13.png'),pygame.image.load('shark\L\L14.png'),pygame.image.load('shark\L\L15.png'),
                 pygame.image.load('shark\L\L16.png'),pygame.image.load('shark\L\L17.png'),pygame.image.load('shark\L\L18.png'),pygame.image.load('shark\L\L19.png')]
    
    def __init__(self, x, y, width, height, start, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.start = start 
        self.end = end
        self.walkCount = 0
        self.vel = 7

     

    def draw(self, win):
        self.move()#par exemple shark1.move()
        if self.walkCount + 1 >=57: #car ils sont en tout 19 photos (57/3=19)
            self.walkCount = 0
        
        if self.vel > 0:
            ecran.blit(pygame.transform.scale(self.walkRight[self.walkCount//3], (self.width, self.height)),(self.x,self.y))#il prend la partie entiere seulement
            self.walkCount += 1
        else:
            ecran.blit(pygame.transform.scale(self.walkLeft[self.walkCount//3], (self.width, self.height)),(self.x,self.y))
            self.walkCount += 1

      
        
    def move(self):
        if self.vel > 0:  #on assume qu'il se deplace vers la droite
            if self.x < self.end + self.vel:
                self.x += self.vel
            else:#sinon il se deplace vers la gauche c pq on multiplie par -1
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0 #on le remet a 0 pour initialiser les images
        else:#ici il se deplace vers la gauche(vel<0)
            if self.x > self.start + self.vel:#ceci montre quelle doit etre > starting
                self.x += self.vel
            else: #sinon il se deplace vers la droite c pq on multiplie par -1
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

class proies(object):
    walkLeft = [pygame.image.load('Fish_1\L\R1.png'),pygame.image.load('Fish_1\L\R2.png'),pygame.image.load('Fish_1\L\R3.png'),pygame.image.load('Fish_1\L\R4.png'),
                pygame.image.load('Fish_1\L\R5.png'),pygame.image.load('Fish_1\L\R6.png'),pygame.image.load('Fish_1\L\R7.png'),pygame.image.load('Fish_1\L\R8.png'),
                pygame.image.load('Fish_1\L\R9.png'),pygame.image.load('Fish_1\L\R10.png'),pygame.image.load('Fish_1\L\R11.png'),pygame.image.load('Fish_1\L\R12.png'),
                pygame.image.load('Fish_1\L\R13.png'),pygame.image.load('Fish_1\L\R14.png'),pygame.image.load('Fish_1\L\R15.png'),pygame.image.load('Fish_1\L\R16.png')]

    walkRight = [pygame.image.load('Fish_1\R\L1.png'),pygame.image.load('Fish_1\R\L2.png'),pygame.image.load("Fish_1\R\L3.png"),pygame.image.load('Fish_1\R\L4.png'),
                 pygame.image.load('Fish_1\R\L5.png'),pygame.image.load('Fish_1\R\L6.png'),pygame.image.load("Fish_1\R\L7.png"),pygame.image.load('Fish_1\R\L8.png'),
                 pygame.image.load('Fish_1\R\L9.png'),pygame.image.load('Fish_1\R\L10.png'),pygame.image.load("Fish_1\R\L11.png"),pygame.image.load('Fish_1\R\L12.png'),
                 pygame.image.load('Fish_1\R\L13.png'),pygame.image.load('Fish_1\R\L14.png'),pygame.image.load("Fish_1\R\L15.png"),pygame.image.load('Fish_1\R\L16.png')]
    
    def __init__(self, x, y, width, height, start, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.start = start 
        self.end = end
        self.walkCount = 0
        self.vel = 7
    

    def draw(self, win):
        self.move()#par exemple shark1.move()
        self.proies(fish)
        if self.walkCount + 1 >= 48: #car ils sont en tout 19 photos (57/3=19)
            self.walkCount = 0
        
        if self.vel > 0:
            ecran.blit(pygame.transform.scale(self.walkRight[self.walkCount//3], (self.width, self.height)),(self.x,self.y))#il prend la partie entiere seuleme
            self.walkCount += 1
        else:
            ecran.blit(pygame.transform.scale(self.walkLeft[self.walkCount//3], (self.width, self.height)),(self.x,self.y))
            self.walkCount += 1

      
        
    def move(self):
        if self.vel > 0:  #on assume qu'il se deplace vers la droite
            if self.x < self.end + self.vel:
                self.x += self.vel
            else:#sinon il se deplace vers la gauche c pq on multiplie par -1
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0 #on le remet a 0 pour initialiser les images
        else:#ici il se deplace vers la gauche(vel<0)
            if self.x > self.start + self.vel:#ceci montre quelle doit etre > starting
                self.x += self.vel
            else: #sinon il se deplace vers la droite c pq on multiplie par -1
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def proies (self,fish):
        import random
        #avec and il faut que tout soit TRUE , alors si on a pas mis les parentheses,
        #il va pas fonctionner car les parentheses forcent le compilateur de les lire d'abord, comme en maths
        if (fish.right and self.x < fish.x + fish.width and self.x>=fish.x and ((self.y <= fish.y + fish.height and self.y >= fish.y ) or (self.y+self.height> fish.y and self.y<fish.y))):
            self.x=random.randint(100,700)
            self.y=random.randint(90,1000)
            if (fish.width <=200 or fish.height<=80):
                fish.width = fish.width + 40
                fish.height = fish.height +20
           
        elif(fish.left and self.x+self.width > fish.x and self.x<=fish.x  and ((self.y <= fish.y + fish.height and self.y >= fish.y ) or (self.y+self.height>fish.y and self.y< fish.y))):
            self.x=random.randint(100, 700)
            self.y=random.randint(90, 1000)
            if (fish.width <=200 or fish.height<=80):
                fish.width = fish.width +40
                fish.height = fish.height+20
            
def redrawindow():#il supprime global!! car il n'y a pas de valeurs precises, chaque instance aura sa propre valeur 
    global fish #sert a connaitre la variable partout dans le programme et a ne pas creer une nouvelle fish par exemple
    ecran.blit(image,(0,0)) #ici c la position par laquelle la photo commence a s'afficher et a chaque fois qu'il y a un mouvement elle le cache
    fish.draw(ecran)
    shark.draw(ecran)
    shark1.draw(ecran)
    shark2.draw(ecran)
    fish.perte(shark)
    fish.perte(shark1)
    fish.perte(shark2)
    petit.draw(ecran)
    petit1.draw(ecran)
    petit2.draw(ecran)
       

    pygame.display.update()

fish=player(300,410,64,64)
shark= enemy(-389, 410, 170,71,-389, 1360) #(x, y, width, height, start, end)
shark1= enemy(900,180, 170,71 ,-120, 1360)#on initialise les caracteristiques de celui-ci -- on a mis position par rapport au starting
shark2= enemy(600,300, 170,71 ,-300, 1360)
petit=proies(90,600,44,38,-370,1360)
petit1=proies(200,250,44,38,-800,1360)
petit2=proies(600,100,44,38,-800,1360)

continuer = True
while continuer:
    clock.tick(24)   
    for event in pygame.event.get(): #dit moi tous les evenements faits par l'utilisateur 
        if event.type == pygame.QUIT:
            continuer=False
            
    keys=pygame.key.get_pressed()#dit moi les boutons dont j clique dessus - important dans la boucle while pas dehors!

#Last Keys pressed: la boucle while permet la repetition, alors event.get permet de verifier
#une nouvelle action par l'utilisateur , ex: une clique=1 nouvelle action .Donc si la boucle For n'a rien de nouveau et que "If keys" est dans cette boucle
#alors la boucle While va ignorer la boucle For (si c la meme action) et donc il faut la mettre ailleurs pour que ca soit une action permanente.

    if keys[pygame.K_LEFT]and fish.x>=fish.vel : #la condition ici de se deplacer : si x>=5 donc oui on peut se deplacer alors on arrivera a la fin a 0! 
        fish.x-=fish.vel
        fish.left=True #ici je change la variable 
        fish.right=False
    elif keys[pygame.K_RIGHT]and fish.x<= 1360-(fish.width+fish.vel): #on peut aussi mettre x<=1360-vel ou meme mettre x<= 1360-(width+5) ou 1360-(x+vel+width)!=0
        fish.x+=fish.vel   
        fish.right=True
        fish.left=False
    else:
        fish.right=False
        fish.left=False
        fish.walkcount=0
    if keys[pygame.K_UP]and fish.y>=fish.vel :
           fish.y-=fish.vel
    if keys[pygame.K_DOWN]and fish.y<= 720-(fish.height+fish.vel) :  #on peut aussi mettre y<=720-vel ou meme mettre y<= 720-(height+5)
           fish.y+=fish.vel
           

    redrawindow()
    
    
pygame.quit() #il faut quitter proprement Pygame


