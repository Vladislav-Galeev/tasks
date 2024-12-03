# Ниже приведены две реализации циклического буфера FIFO: через обычный список и связанный список
# Связанный список займет больше места из-за хранения ссылок на следующие элементы
# Операции вставки и удаления занимат одинаковое время О(1)
# Операции доступа к элементам занимают разное время: О(1) у обычных списков, О(n) у связанного списка
# Расширение буфера занимает меньше времени у связанного списка 


# Первая реализация циклического буфера FIFO. Здесь используется список.
class CircularBufferV1:
    def __init__(self, size=1):
        self.size = max(1, size)
        self.array = [None] * self.size
        self.head = 0
        self.tail = 0
    
    def put(self, value):
        self.array[self.head] = value
        if self.head == self.tail and self.array[(self.head + 1) % self.size] != None:
            self.tail = (self.tail + 1) % self.size

        self.head = (self.head + 1) % self.size

    def pull(self):
        if self.array[self.tail] != None:
            self.array[self.tail] = None
            self.tail = (self.tail + 1) % self.size

    def getHead(self):
        print(self.array[self.head - 1])

    def getTail(self):
        print(self.array[(self.tail) % self.size])
    
    def getArray(self):
        print(*self.array)


# Вторая реализация циклического буфера FIFO. Здесь используется связанный список.
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class CircularBufferV2:
    def __init__(self, size=1):
        self.size = max(1, size)
        self.head = None
        self.tail = None
        self.current_size = 0
    
    def put(self, value):
        self.current_size += 1
        if self.current_size == 1:
            self.head = self.tail = Node(value)

        elif self.current_size == self.size:
            self.head.next = Node(value)
            self.head = self.head.next
            self.head.next = self.tail

        elif self.current_size > self.size:
            self.head, self.tail = self.tail, self.tail.next
            self.head.value = value
            self.current_size -= 1

        else:
            self.head.next = Node(value)
            self.head = self.head.next

    def pull(self):
        if self.tail != None:
            if self.current_size == self.size:
                self.tail = self.tail.next
                self.head.next = None

            else:
                if self.current_size == 1:
                    self.head = None
                    self.tail = None

                else:
                    self.tail = self.tail.next

            self.current_size -= 1

    def getHead(self):
        if self.current_size == 0:
            return None
        else:
            return self.head.value
    
    def getTail(self):
        if self.current_size == 0:
            return None
        else:
            return self.tail.value