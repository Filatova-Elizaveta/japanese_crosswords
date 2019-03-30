# coding: utf-8

# In[2]:


import pygame 

class Board():
    def __init__(self, width, height, tl):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.type = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.f1 = pygame.font.Font(None, 36)
        self.tl = tl
        
    def drawlevel(self,q) :
        if (30 < q[0] < 670) and (50 < q[1] < 150):
            self.tl = 1
        elif (30 < q[0] < 670) and (250 < q[1] < 350):
            self.tl = 2
        elif (30 < q[0] < 670) and (450 < q[1] <550):
            self.tl = 3
        print(self.tl)
        return self.tl    

      
    def drawlevel1(self) :
        text1 = self.f1.render('1 уровень', 1, (0, 0, 0))
        text2 = self.f1.render('2 уровень', 1, (0, 0, 0))
        text3 = self.f1.render('3 уровень', 1, (0, 0, 0))
        pygame.draw.rect(screen, (255,255,0), [30,50,640,100])
        pygame.draw.rect(screen, (255,255,0), [30,250,640,100])
        pygame.draw.rect(screen, (255,255,0), [30,450,640,100])
        screen.blit(text1, (350,75))
        screen.blit(text2, (350,275))
        screen.blit(text3, (350,475))

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
      
    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.type[j][i] % 3 == 0:
                    self.board[j][i] = 0
                    pygame.draw.rect(screen, (255, 255, 255), [self.left+i*self.cell_size, self.top+j*self.cell_size, self.cell_size, self.cell_size])
                
                elif self.type[j][i] % 3 == 1:
                    self.board[j][i] = 1
                    pygame.draw.rect(screen, (0, 0, 0), [self.left+i*self.cell_size, self.top+j*self.cell_size, self.cell_size, self.cell_size])
                    
                elif self.type[j][i] % 3 == 2:
                    self.board[j][i] = 0
                    pygame.draw.rect(screen, (255, 255, 255), [self.left+i*self.cell_size, self.top+j*self.cell_size, self.cell_size, self.cell_size])
#                    pygame.draw.rect(screen, (255, 0, 0), [self.left+i*self.cell_size, self.top+j*self.cell_size, self.cell_size, self.cell_size])
                    pygame.draw.line(screen, (0, 0, 0), [self.left+i*self.cell_size, self.top+j*self.cell_size], [self.left+(i+1)*self.cell_size, self.top+(j+1)*self.cell_size], 5)
                    pygame.draw.line(screen, (0, 0, 0), [self.left+(i+1)*self.cell_size, self.top+j*self.cell_size], [self.left+i*self.cell_size, self.top+(j+1)*self.cell_size], 5)
                    
                pygame.draw.rect(screen, (0, 0, 0), [self.left+i*self.cell_size, self.top+j*self.cell_size, self.cell_size, self.cell_size], 1)
            pygame.draw.rect(screen, (153,255,255), [self.left+(-2*self.cell_size), self.top+(-2*self.cell_size), 2*self.cell_size, 2*self.cell_size])


        if self.tl == 1:
            pygame.draw.rect(screen, (0,128,128), [self.left, self.top+(-2*self.cell_size), 8*self.cell_size, 2*self.cell_size])
            pygame.draw.rect(screen, (0,128,128), [self.left+(-2*self.cell_size), self.top, 2*self.cell_size, 8*self.cell_size])                
            text1 = self.f1.render('2', 1, (0, 0, 0))
            text2 = self.f1.render('8', 1, (0, 0, 0))
            
            screen.blit(text1, (self.left, self.top+(-1*self.cell_size)))
            screen.blit(text1, (self.left, self.top+(-2*self.cell_size)))
            screen.blit(text2, (self.left+self.cell_size, self.top+(-1*self.cell_size)))
            screen.blit(text2, (self.left+self.cell_size+self.cell_size, self.top+(-1*self.cell_size)))
            screen.blit(text1, (self.left+3*self.cell_size, self.top+(-1*self.cell_size)))
            screen.blit(text1, (self.left+3*self.cell_size, self.top+(-2*self.cell_size)))
            screen.blit(text1, (self.left+4*self.cell_size, self.top+(-1*self.cell_size)))
            screen.blit(text1, (self.left+4*self.cell_size, self.top+(-2*self.cell_size)))
            screen.blit(text2, (self.left+5*self.cell_size, self.top+(-1*self.cell_size)))
            screen.blit(text2, (self.left+6*self.cell_size, self.top+(-1*self.cell_size)))
            screen.blit(text1, (self.left+7*self.cell_size, self.top+(-1*self.cell_size)))
            screen.blit(text1, (self.left+7*self.cell_size, self.top+(-2*self.cell_size)))
            screen.blit(text1, (self.left+(-2*self.cell_size), self.top))
            screen.blit(text1, (self.left+(-1*self.cell_size), self.top))
            screen.blit(text2, (self.left+(-1*self.cell_size), self.top+self.cell_size))
            screen.blit(text2, (self.left+(-1*self.cell_size), self.top+2*self.cell_size))
            screen.blit(text1, (self.left+(-2*self.cell_size), self.top+3*self.cell_size))
            screen.blit(text1, (self.left+(-1*self.cell_size), self.top+3*self.cell_size))
            screen.blit(text1, (self.left+(-2*self.cell_size), self.top+4*self.cell_size))
            screen.blit(text1, (self.left+(-1*self.cell_size), self.top+4*self.cell_size))
            screen.blit(text2, (self.left+(-1*self.cell_size), self.top+5*self.cell_size))
            screen.blit(text2, (self.left+(-1*self.cell_size), self.top+6*self.cell_size))
            screen.blit(text1, (self.left+(-2*self.cell_size), self.top+7*self.cell_size))
            screen.blit(text1, (self.left+(-1*self.cell_size), self.top+7*self.cell_size))
            self.check_1()
        elif self.tl == 2:
            vert = [['','','','5',''],
                    ['','','1','1',''],
                    ['3','5','8','1','3']]
            pygame.draw.rect(screen, (0,128,128), [self.left, self.top+(-3*self.cell_size), 5*self.cell_size, 3*self.cell_size])
            pygame.draw.rect(screen, (0,128,128), [self.left+(-2*self.cell_size), self.top, 2*self.cell_size, 10*self.cell_size])
            
            for i in range(3):
                for j in range(5):
                    screen.blit(self.f1.render(vert[i][j], 1, (0, 0, 0)), (self.left+j*self.cell_size, self.top+(-(3-i)*self.cell_size)) )
            
            hor = [['','3'],['2','2'],['','5'],['','5'],['','3'],['','1'],['','1'],['','2'],['','1'],['','2']]
            self.check_2()
            for i in range(10):
                for j in range(2):
                    screen.blit(self.f1.render(hor[i][j], 1, (0, 0, 0)), (self.left-(2-j)*self.cell_size, self.top+i*self.cell_size))
        elif self.tl == 3:
            self.check_3()
            pygame.draw.rect(screen, (0,128,128), [self.left, self.top+(-5*self.cell_size), 13*self.cell_size, 5*self.cell_size])
            pygame.draw.rect(screen, (0,128,128), [self.left+(-5*self.cell_size), self.top, 5*self.cell_size, 14*self.cell_size]) 
            v = [['', '', '', '1', '', '', '', '', '', '1','','',''],
                 ['', '1', '', '1', '', '', '', '1', '', '2','3','',''],
                 ['3', '2', '', '3', '', '', '', '1', '1', '1','1','',''],
                 ['1', '1', '1', '2', '', '5', '', '3', '4', '1','1','',''],
                 ['1', '1', '4', '1', '12', '6', '12', '4', '2', '1','2','2','3']]
            for i in range(5):
                for j in range(13):
                    screen.blit(self.f1.render(v[i][j], 1, (0, 0, 0)), (self.left+j*self.cell_size, self.top+(-(5-i)*self.cell_size)) )
            gg = [['','','','2','2'],['','1','1','1',''],['','','1','5','1'],['','','1','3','1'],['','','1','5','1'],['1','1','3','1','1'],['','','','','9'],['','1','3','3','1'],['','','','','9'],['','','','3','1'],['','','','5','1'],['','','','5','2'],['','','','5','2'],['','','','','8']]
            for i in range(14):
                for j in range(5):
                    screen.blit(self.f1.render(gg[i][j], 1, (0, 0, 0)), (self.left-(5-j)*self.cell_size, self.top+i*self.cell_size))
#            screen.blit(text1, (self.left, self.top+(-1*self.cell_size)))
#            screen.blit(text1, (self.left, self.top+(-2*self.cell_size)))
#            screen.blit(text2, (self.left+self.cell_size, self.top+(-1*self.cell_size)))
#            screen.blit(text2, (self.left+self.cell_size+self.cell_size, self.top+(-1*self.cell_size)))
#            screen.blit(text1, (self.left+3*self.cell_size, self.top+(-1*self.cell_size)))
#            screen.blit(text1, (self.left+3*self.cell_size, self.top+(-2*self.cell_size)))              
            self.check_2()
            

            
        elif self.tl == 3:
            self.check_3()
        
    def get_cell(self, mouse_pos):
            if (self.left <= mouse_pos[0] <= self.left+self.cell_size*self.width) and (self.top <= mouse_pos[1] <= self.top+self.cell_size*self.height):
                return mouse_pos
            else:
                return None     

    def on_click(self, cell_coords):
        if cell_coords != None:
            q = ((cell_coords[0] - self.left)//self.cell_size, (cell_coords[1] - self.top)//self.cell_size)
            #print(q)
            self.type[q[1]][q[0]] += 1
        else:
            print(cell_coords)
    

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
        
        
    def check_1(self):
        massiv = [[0,1,1,0,0,1,1,0],
                  [1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1],
                  [0,1,1,0,0,1,1,0],
                  [0,1,1,0,0,1,1,0],
                  [1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1],
                  [0,1,1,0,0,1,1,0]]
                  
        for i in range(8):
            if self.board[i] == massiv[i]:
                pygame.draw.rect(screen, (0, 255, 0), [self.left+8*self.cell_size, self.top+(i*self.cell_size), self.cell_size, self.cell_size])
        for i in range(8):
            self.board = list(map(list,zip(*self.board[::-1])))
            if self.board[i] == massiv[i]:
                pygame.draw.rect(screen, (0, 255, 0), [self.left+(i*self.cell_size), self.top+(8*self.cell_size), self.cell_size, self.cell_size])
            self.board = list(map(list,zip(*self.board[::-1])))
            self.board = list(map(list,zip(*self.board[::-1])))
            self.board = list(map(list,zip(*self.board[::-1])))
    
    def check_2(self):
        massiv = [[0,1,1,1,0],
                   [1,1,0,1,1],
                   [1,1,1,1,1],
                   [1,1,1,1,1],
                   [0,1,1,1,0],
                   [0,0,1,0,0],
                   [0,0,1,0,0],
                   [0,0,1,1,0],
                   [0,0,1,0,0],
                   [0,0,1,1,0]]
        for i in range(10):
            if self.board[i] == massiv[i]:
                pygame.draw.rect(screen, (0, 255, 0), [self.left+5*self.cell_size, self.top+(i*self.cell_size), self.cell_size, self.cell_size])
        for i in range(5):
            self.board = list(map(list,zip(*self.board[::-1])))
            massiv = list(map(list,zip(*massiv[::-1])))
            
            if self.board[i]== massiv[i]:
                pygame.draw.rect(screen, (0, 255, 0), [self.left+i*self.cell_size, self.top+(10*self.cell_size), self.cell_size, self.cell_size])
            self.board = list(map(list,zip(*self.board[::-1])))
            self.board = list(map(list,zip(*self.board[::-1])))
            self.board = list(map(list,zip(*self.board[::-1])))
            
            massiv = list(map(list,zip(*massiv[::-1])))
            massiv = list(map(list,zip(*massiv[::-1])))
            massiv = list(map(list,zip(*massiv[::-1]))) 
            
            
            
            
    def check_3(self):
        massiv = [[1,1,0,0,0,0,0,0,0,1,1,0,0],
                   [1,0,1,0,0,0,0,0,1,0,1,0,0],
                   [1,0,0,1,1,1,1,1,0,0,1,0,0],
                   [0,1,0,0,1,1,1,0,0,1,0,0,0],
                   [0,1,0,1,1,1,1,1,0,1,0,0,0],
                   [1,0,1,0,1,1,1,0,1,0,1,0,0],
                   [0,1,1,1,1,1,1,1,1,1,0,0,0],
                   [1,0,1,1,1,0,1,1,1,0,1,0,0],
                   [0,1,1,1,1,1,1,1,1,1,0,0,0],
                   [0,0,0,0,1,1,1,0,0,0,0,0,1],
                   [0,0,0,1,1,1,1,1,0,0,0,0,1],
                   [0,0,0,1,1,1,1,1,0,0,0,1,1],
                   [0,0,0,0,1,1,1,1,1,0,1,1,0],
                   [0,0,0,1,1,1,1,1,1,1,1,0,0]]
        
        
        
        for i in range(14):
            if self.board[i] == massiv[i]:
                pygame.draw.rect(screen, (0, 255, 0), [self.left+13*self.cell_size, self.top+(i*self.cell_size), self.cell_size, self.cell_size])
        for i in range(13):
            self.board = list(map(list,zip(*self.board[::-1])))
            massiv = list(map(list,zip(*massiv[::-1])))
            
            if self.board[i]== massiv[i]:
                pygame.draw.rect(screen, (0, 255, 0), [self.left+i*self.cell_size, self.top+(14*self.cell_size), self.cell_size, self.cell_size])
            self.board = list(map(list,zip(*self.board[::-1])))
            self.board = list(map(list,zip(*self.board[::-1])))
            self.board = list(map(list,zip(*self.board[::-1])))
            massiv = list(map(list,zip(*massiv[::-1])))
            massiv = list(map(list,zip(*massiv[::-1])))
            massiv = list(map(list,zip(*massiv[::-1]))) 


pygame.init()
tl = 0
cho = 0 
board = Board(8, 8, tl)
board.set_view(100, 100, 50)
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.flip()
running = True
f = 0 
while running:
    if not f:
        board.drawlevel1()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if tl == 0:
                 tl = board.drawlevel(event.pos)
                # tl = 0/1/2
            else:
                board.get_click(event.pos)
    
    
    screen.fill((153,255,255))   
    
    if tl == 0:
        board.drawlevel1()
    elif (tl==1) & (cho == 0) :
        board = Board(8,8, 1)
        board.set_view(100, 100, 50)
        cho = 1
        size = (700, 700)
        screen = pygame.display.set_mode(size)
    elif (tl==2) & (cho == 0):
        board = Board(5, 10, 2)
        board.set_view(150, 150, 50)
        cho = 1
        size = (500, 700)
        screen = pygame.display.set_mode(size)
    elif (tl==3) & (cho == 0):
        board = Board(13,14,3)
        board.set_view(200, 200, 30)
        size = (1000, 1000)
        screen = pygame.display.set_mode(size)
        cho = 1
        
    
    if cho == 1: 
        board.render()
        
    pygame.display.flip()
    
pygame.quit()
   