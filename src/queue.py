class Queue:
    def __init__(self, capacity=None):
        self.queue = []
        self.capacity = capacity

    def is_empty(self):
        if not self.queue:
            return True
        return False

    def put_element(self, el):
        if not self.full_capacity():
            self.queue.append(el)

    def get_element(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def size(self):
        if self.is_empty():
            return 0
        return len(self.queue)

    def show_top(self):
        if not self.is_empty():
            return self.queue[0]

    def full_capacity(self):
        if len(self.queue) == self.capacity:
            return True
        return False


queue1 = [1, 3, 5, 7, 9]
queue2 = [2, 4, 6, 8, 0]
first = Queue()
second = Queue()
for i in queue1:
    first.put_element(i)
for j in queue2:
    second.put_element(j)


class Game:
    def __init__(self, q1: Queue, q2: Queue):
        self.first = q1
        self.second = q2
        self.step = 0

    def play(self):
        if not self.first.is_empty() and not self.second.is_empty():
            card1 = self.first.get_element()
            card2 = self.second.get_element()
            self.step += 1
            if card1 == 9 and card2 == 0:
                self.second.put_element(card1)
                self.second.put_element(card2)
            elif card1 > card2:
                self.first.put_element(card1)
                self.first.put_element(card2)
            if card1 == 0 and card2 == 9:
                self.first.put_element(card1)
                self.first.put_element(card2)
            elif card2 > card1:
                self.second.put_element(card1)
                self.second.put_element(card2)

    def game(self):
        while not (self.first.is_empty() or self.second.is_empty()):
            self.play()
            if self.step == 1000000:
                print('botva')
                break
        if self.first.is_empty():
            print('2nd won')
        elif self.second.is_empty():
            print('1st won')
        print(f'number of steps: {self.step}')


drunk = Game(first, second)
drunk.game()
