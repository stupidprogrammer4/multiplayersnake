import consts


class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x
    
    def __is_dead(self, cell):
        return cell.color != consts.fruit_color and cell.color != consts.back_color 

    def __is_eat(self, cell):
        return cell.color == consts.fruit_color

    def __move(self, posx, posy):
        posx = self.val(posx)
        posy = self.val(posy)
        next = self.game.get_cell((posx, posy))
        if self.__is_eat(next):
            self.cells.append((posx, posy))
        elif self.__is_dead(next):
            self.game.kill(self)
            return
        tail = self.game.get_cell((self.cells[0][0], self.cells[0][1]))
        tail.set_color(consts.back_color)
        self.cells.pop(0)
        next.set_color(self.color)
        self.cells.append((posx, posy))

    def next_move(self):
        head = self.get_head()
        if self.direction == 'LEFT':
            self.__move(head[0]-1, head[1])
        elif self.direction == 'RIGHT':
            self.__move(head[0]+1, head[1])
        elif self.direction == 'UP':
            self.__move(head[0], head[1]-1)
        elif self.direction == 'DOWN':
            self.__move(head[0], head[1]+1)

    def handle(self, keys):
        for key in keys:
            d = self.keys.get(key)
            if key in self.keys and d != self.direction:
                self.set_direction(d)
                break
        self.next_move()

    def set_direction(self, d):
        if d == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif d == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        elif d == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif d == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

