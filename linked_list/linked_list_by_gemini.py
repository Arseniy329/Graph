class Node():
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev # Тепер цей вказівник буде використовуватись

    # Getters/Setters залишаються без змін
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
        
    def get_prev(self): # Додамо getter для prev
        return self.prev

    def set_data(self, data):
        self.data = data
    
    def set_next(self, next):
        self.next = next
        
    def set_prev(self, prev): # Додамо setter для prev
        self.prev = prev

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None # Для двозв'язного списку зручно мати вказівник на хвіст

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        # Додаємо вузол в кінець
        self.tail.set_next(new_node)
        new_node.set_prev(self.tail)
        self.tail = new_node

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
            
        # Додаємо вузол на початок
        self.head.set_prev(new_node)
        new_node.set_next(self.head)
        self.head = new_node

    # Функція виправлена, тепер працює коректно
    def remove_back(self):
        if self.head is None:
            print("Список порожній.")
            return

        if self.head == self.tail: # Якщо у списку один елемент
            self.head = None
            self.tail = None
            return
            
        # Видаляємо останній елемент
        self.tail = self.tail.get_prev()
        self.tail.set_next(None)

    def remove_front(self):
        if self.head is None:
            print("Список порожній.")
            return
        
        if self.head == self.tail: # Якщо у списку один елемент
            self.head = None
            self.tail = None
            return
            
        # Видаляємо перший елемент
        self.head = self.head.get_next()
        self.head.set_prev(None)
        
    # Функція виправлена для коректної роботи
    def insert(self, index, data):
        if index == 0:
            self.push_front(data)
            return

        curr_node = self.head
        count = 0
        while curr_node is not None:
            if count + 1 == index:
                if curr_node == self.tail: # Вставка в кінець
                    self.append(data)
                else: # Вставка в середину
                    new_node = Node(data)
                    next_node = curr_node.get_next()
                    
                    curr_node.set_next(new_node)
                    new_node.set_prev(curr_node)
                    new_node.set_next(next_node)
                    next_node.set_prev(new_node)
                return
            curr_node = curr_node.get_next()
            count += 1
            
        print("Індекс за межами списку.")

    # --- Нові функції, яких бракувало ---

    def find(self, data):
        """Локалізація елемента: повертає індекс першого знайденого елемента або None."""
        curr_node = self.head
        index = 0
        while curr_node is not None:
            if curr_node.get_data() == data:
                return index
            curr_node = curr_node.get_next()
            index += 1
        return None

    def get_node_at(self, index):
        """Вибір елемента: повертає вузол (Node) за індексом."""
        curr_node = self.head
        count = 0
        while curr_node is not None:
            if count == index:
                return curr_node
            count += 1
            curr_node = curr_node.get_next()
        return None # Якщо індекс не знайдено

    def merge(self, other_list):
        """Об'єднання двох списків: додає інший список в кінець поточного."""
        if not isinstance(other_list, LinkedList):
            print("Можна об'єднувати лише з іншим LinkedList.")
            return
            
        if other_list.head is None: # Якщо другий список порожній
            return

        if self.head is None:
            self.head = other_list.head
            self.tail = other_list.tail
        else:
            self.tail.set_next(other_list.head)
            other_list.head.set_prev(self.tail)
            self.tail = other_list.tail

    def show(self):
        curr_node = self.head
        output = ""
        while curr_node is not None:
            output += str(curr_node.get_data()) + " <-> "
            curr_node = curr_node.get_next()
        print(output + "None")
        
    def length(self):
        curr_node = self.head
        count = 0
        while curr_node is not None:
            count += 1
            curr_node = curr_node.get_next()
        return count
# --- Демонстрація роботи ---

# Створюємо перший список
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.push_front(5)
print("Початковий список:")
my_list.show() # Очікуємо: 5 <-> 10 <-> 20 <-> None

# 1. Вставка елемента
print("\n--- 1. Демонстрація вставки ---")
my_list.insert(2, 15) # Вставляємо 15 між 10 і 20
print("Після вставки '15' за індексом 2:")
my_list.show() # Очікуємо: 5 <-> 10 <-> 15 <-> 20 <-> None

# 2. Локалізація елемента
print("\n--- 2. Демонстрація локалізації ---")
index = my_list.find(10)
print(f"Елемент '10' знаходиться за індексом: {index}") # Очікуємо: 1
index_not_found = my_list.find(99)
print(f"Результат пошуку елемента '99': {index_not_found}") # Очікуємо: None

# 3. Вибір елемента, попереднього і наступного
print("\n--- 3. Демонстрація вибору елементів ---")
node = my_list.get_node_at(2) # Отримуємо вузол з даними '15'
if node:
    print(f"Вибраний елемент за індексом 2: {node.get_data()}")
    
    # Вибірка наступного
    next_node = node.get_next()
    if next_node:
        print(f"Наступний елемент: {next_node.get_data()}") # Очікуємо: 20
        
    # Вибірка попереднього (тепер це можливо!)
    prev_node = node.get_prev()
    if prev_node:
        print(f"Попередній елемент: {prev_node.get_data()}") # Очікуємо: 10

# 4. Вилучення елемента
print("\n--- 4. Демонстрація вилучення ---")
my_list.remove_back()
print("Після вилучення з кінця:")
my_list.show() # Очікуємо: 5 <-> 10 <-> 15 <-> None

my_list.remove_front()
print("Після вилучення з початку:")
my_list.show() # Очікуємо: 10 <-> 15 <-> None

# 5. Об'єднання двох списків
print("\n--- 5. Демонстрація об'єднання ---")
list2 = LinkedList()
list2.append(100)
list2.append(200)
print("Другий список:")
list2.show()

my_list.merge(list2)
print("Перший список після об'єднання з другим:")
my_list.show() # Очікуємо: 10 <-> 15 <-> 100 <-> 200 <-> None
print(f"Нова довжина списку: {my_list.length()}")