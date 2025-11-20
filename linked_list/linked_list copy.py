class Node(): 
    def __init__(self, data = None, next = None, prev = None): 
        self.data = data 
        self.next = next 
        self.prev = prev 
 
    def get_data(self): 
        return self.data 
    
    def prev(self):
        return self.prev
 
    def get_next(self): 
        return self.next 
 
    def set_data(self, data): 
        self.data = data 
     
    def set_next(self, next): 
        self.next = next 
     
class LinkedList(): 
    def __init__(self): 
        self.head = None 
 
    def append(self, data): 
        new_node = Node(data) 
        cur_node = self.head 
        if cur_node == None: 
            self.head = new_node 
            return 
        while cur_node.get_next() != None: 
            cur_node = cur_node.get_next() 
        cur_node.set_next(new_node) 
         
    def add_to_end(self, data): 
        cur_node = self.head 
        new_node = Node(data) 
        while cur_node.get_next() != None: 
            cur_node = cur_node.get_next() 
        cur_node.set_next(new_node) 
 
 
    def display(self): 
        cur_node = self.head 
        output = "" 
        while cur_node != None: 
            output += str(cur_node.get_data()) + " -> " 
            cur_node = cur_node.get_next() 
        print(output) 
 
    def push_front(self, data): 
        new_node = Node(data) 
        cur_node = self.head 
        new_node.set_next(cur_node) 
        self.head = new_node 
 
    def value_at(self, index): 
        cur_node = self.head 
        count = 0 
        while cur_node != None: 
            if count + 1 == index: 
                return cur_node.get_data() 
            count += 1 
            cur_node = cur_node.get_next() 
        print("Index is out of range")
        
    def get_prev_element(self, index):
        cur_node = self.head
        count = 1   
        while cur_node is not None:
            if count == index - 1:
                return cur_node
            cur_node = cur_node.get_next()
            count += 1
        return None
 
    def insert(self, index, data): 
        if index == 0: 
                self.push_front(data) 
                return 
        new_node = Node(data) 
        cur_node = self.head 
        count = 0 
        while cur_node.get_next() != None: 
            if count + 1 == index: 
                the_node_after_cur = cur_node.get_next() 
                cur_node.set_next(new_node) 
                new_node.set_next(the_node_after_cur) 
                return 
            count += 1 
            cur_node = cur_node.get_next() 
        print("Index is out of range") 
         
    def find(self, data): 
        curr_node = self.head 
        index = 0 
        while curr_node is not None: 
            if curr_node.get_data() == data: 
                return index 
            curr_node = curr_node.get_next() 
            index += 1 
        return None 
 
    def remove_by_value(self, data): 
        cur_node = self.head 
        if self.head is None: 
            return 
        if self.head.get_data() == data: 
            self.head = self.head.get_next() 
            return 
        while cur_node.get_next() is not None: 
            if cur_node.get_next().get_data() == data: 
                node_to_remove = cur_node.get_next() 
                cur_node.set_next(node_to_remove.get_next()) 
                return 
            cur_node = cur_node.get_next() 
             
        print(f"Елемент зі значенням {data} не знайдено у списку.") 
 
 
my_list = LinkedList() 
 
my_list.append(2) 
my_list.append(4) 
my_list.append(8) 
my_list.append(16) 
my_list.append(45) 
 
print("Виведення списка: ") 
my_list.display() 
 
print("Вставка елемента на початок списку") 
my_list.push_front(int(input("Введіть значення елемента: "))) 
my_list.display() 
 
print("Вставка елемента в кінець списку") 
my_list.add_to_end(int(input("Введіть значення елемента: "))) 
my_list.display() 
 
my_list.remove_by_value(int(input("Видалення елемента: "))) 
my_list.display()

my_list.get_prev_element(int(input("Введіть індекс елемента: ")))

 
print("Вставка елементу в лист: ") 
my_list.insert(int(input("Введіть місце в списку: ")), int(input("Введіть елемент: "))) 
my_list.display() 
 
print("Вибірка елементу зі списка: ") 
print(my_list.value_at(int(input("Введіть значення: ")))) 
 
index = my_list.find(int(input("Введіть елемент для отримання його індекса: "))) 
print(index + 1)