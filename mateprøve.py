import pygame

pygame.init()

# Font som brukes for å style teksten
font20 = pygame.font.Font('freesansbold.ttf', 20)

# RGB verdier for standart farger
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Størrelse på vindu
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

#Hvor fort ballen går
clock = pygame.time.Clock()
FPS = 50

#Rekkerten
class Rekkert:
    # Første posisjon, dimensjon, fart og farge til objektet
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        # Rect som brukes for å kontrollere posisjonen og kollisjonen til objektet, pygame bruker rect for å lagre rektangulære kordinater
        self.playerRect = pygame.Rect(posx, posy, width, height)
        # Objektet som blir bygget på skjermen
        self.player = pygame.draw.rect(screen, self.color, self.playerRect)

    # Brukt for å vise objektet på skjermen
    def display(self):
        self.player = pygame.draw.rect(screen, self.color, self.playerRect)

    def update(self, yFac):
        self.posy = self.posy + self.speed*yFac

        # Stopper objektet fra å være under bunnen på skjermen
        if self.posy <= 0:
            self.posy = 0
        # Stopper objektet fra å være over toppen av skjermen
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT-self.height

        # Oppdaterer rect med nye verdier
        self.playerRect = (self.posx, self.posy, self.width, self.height)

    def displayScore(self, text, score, x, y, color):
        text = font20.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)

        screen.blit(text, textRect)

    def getRect(self):
        return self.playerRect

# Ballen
class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1

    def display(self):
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)

    def update(self):
        self.posx += self.speed*self.xFac
        self.posy += self.speed*self.yFac

        # Hvis ballen treffer toppen eller bunnen,
        # endres yFac og
        # det resulterer i at ballen spretter tilbake
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1

        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0

    def reset(self):
        self.posx = WIDTH//2
        self.posy = HEIGHT//2
        self.xFac *= -1
        self.firstTime = 1

    # Brukt til å reflektere ballen på X-aksen
    def hit(self):
        self.xFac *= -1

    def getRect(self):
        return self.ball

#Start meny
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
game_state = "start_menu"

def draw_start_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('My Game', True, (255, 255, 255))
    start_button = font.render('[space] to start', True, (255, 255, 255))
    screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2))
    screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2))
    pygame.display.update()

def draw_game_over_screen():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Game Over', True, (255, 255, 255))
    restart_button = font.render('R - Restart', True, (255, 255, 255))
    quit_button = font.render('Q - Quit', True, (255, 255, 255))
    screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))
    screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/1.9 + restart_button.get_height()))
    screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if game_state == "start_menu":
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player_x = 200
            player_y = 400
            game_state = "game"
            game_over = False
    elif game_state == "game_over":
        draw_game_over_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_state = "start_menu"
        if keys[pygame.K_q]:
            pygame.quit()
            quit()
    elif game_state == "game":
       
        # Game Manager
        def main():
            running = True

            # Defining the objects
            player1 = Rekkert(20, 0, 10, 100, 10, WHITE)
            player2 = Rekkert(WIDTH-30, 0, 10, 100, 10, WHITE)
            ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)

            listOfPlayers = [player1, player2]

            # Initial parameters of the players
            player1Score, player2Score = 0, 0
            player1YFac, player2YFac = 0, 0

            while running:
                screen.fill(BLACK)

                # Event handling
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            player2YFac = -1
                        if event.key == pygame.K_DOWN:
                            player2YFac = 1
                        if event.key == pygame.K_w:
                            player1YFac = -1
                        if event.key == pygame.K_s:
                            player1YFac = 1
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            player2YFac = 0
                        if event.key == pygame.K_w or event.key == pygame.K_s:
                            player1YFac = 0

                # Oppdager kollisjoner
                for player in listOfPlayers:
                    if pygame.Rect.colliderect(ball.getRect(), player.getRect()):
                        ball.hit()

                # Oppdaterer objektene
                player1.update(player1YFac)
                player2.update(player2YFac)
                point = ball.update()

                #Legg til poeng
                if point == -1:
                    player1Score += 1
                elif point == 1:
                    player2Score += 1

                # Flytter ballen tilbake når noen har fått et poeng
                if point:
                    ball.reset()

                # Viser objektene på skjermen
                player1.display()
                player2.display()
                ball.display()

                # Viser stillingen på skjermen
                player1.displayScore("User 1 : ",
                                player1Score, 100, 20, WHITE)
                player2.displayScore("User 2 : ",
                                player2Score, WIDTH-100, 20, WHITE)

                pygame.display.update()
                clock.tick(FPS)  
           
               

        if __name__ == "__main__":
            main()
            pygame.quit()


