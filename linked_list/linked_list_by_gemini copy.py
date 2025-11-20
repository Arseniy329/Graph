class Node():
    # Прибираємо 'prev', оскільки це реалізація однозв'язного списку
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        """Додає елемент в кінець списку."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        # Починаємо з голови і йдемо до останнього вузла
        last_node = self.head
        while last_node.get_next() is not None:
            last_node = last_node.get_next()
        
        # Встановлюємо новий вузол як наступний для останнього
        last_node.set_next(new_node)

    def display(self):
        """Виводить вміст списку."""
        cur_node = self.head
        output = ""
        while cur_node is not None:
            output += str(cur_node.get_data()) + " -> "
            cur_node = cur_node.get_next()
        print(output + "None") # Додаємо "None" в кінці для наочності

    def push_front(self, data):
        """Додає елемент на початок списку."""
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def value_at(self, index):
        """Повертає значення за індексом (починаючи з 0)."""
        cur_node = self.head
        count = 0
        while cur_node is not None:
            if count == index:
                return cur_node.get_data()
            count += 1
            cur_node = cur_node.get_next()
        # Якщо індекс за межами списку, повертаємо None
        return None

    def get_next_element(self, data):
        """Знаходить елемент і повертає значення наступного за ним елемента."""
        cur_node = self.head
        while cur_node is not None and cur_node.get_next() is not None:
            if cur_node.get_data() == data:
                return cur_node.get_next().get_data()
            cur_node = cur_node.get_next()
        return None # Повертає None, якщо елемент не знайдено або він останній

    def insert(self, index, data):
        """Вставляє елемент за вказаним індексом (починаючи з 0)."""
        if index < 0:
            print("Помилка: індекс не може бути від'ємним.")
            return

        if index == 0:
            self.push_front(data)
            return

        new_node = Node(data)
        cur_node = self.head
        count = 0
        
        # Шукаємо вузол, що стоїть ПЕРЕД потрібною позицією
        while count < index - 1 and cur_node is not None:
            cur_node = cur_node.get_next()
            count += 1
        
        # Якщо індекс більший за довжину списку або список порожній
        if cur_node is None:
            print("Індекс за межами списку.")
            return

        # Вставляємо новий вузол
        new_node.set_next(cur_node.get_next())
        cur_node.set_next(new_node)
        
    def find(self, data):
        """Повертає індекс першого входження елемента (починаючи з 0)."""
        cur_node = self.head
        index = 0
        while cur_node is not None:
            if cur_node.get_data() == data:
                return index
            cur_node = cur_node.get_next()
            index += 1
        return None

    def remove_by_value(self, data):
        """Видаляє перше входження елемента за його значенням."""
        if self.head is None:
            print(f"Список порожній. Неможливо видалити {data}.")
            return

        # Якщо елемент для видалення - голова списку
        if self.head.get_data() == data:
            self.head = self.head.get_next()
            return
        
        # Шукаємо вузол, що стоїть ПЕРЕД тим, який треба видалити
        prev_node = self.head
        while prev_node.get_next() is not None:
            if prev_node.get_next().get_data() == data:
                node_to_remove = prev_node.get_next()
                prev_node.set_next(node_to_remove.get_next())
                return
            prev_node = prev_node.get_next()

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

print("Вставка елементу в лист: ") 
my_list.get_prev_element(int(input("Введіть елемент: "))) 
my_list.display()
 
print("Вставка елементу в лист: ") 
my_list.insert(int(input("Введіть місце в списку: ")), int(input("Введіть елемент: "))) 
my_list.display() 
 
print("Вибірка елементу зі списка: ") 
print(my_list.value_at(int(input("Введіть значення: ")))) 
 
index = my_list.find(int(input("Введіть елемент для отримання його індекса: "))) 
print(index + 1)



print("\nПошук елемента, наступного за 4:")
next_val = my_list.get_next_element(4)
if next_val is not None:
    print(f"За елементом 4 йде: {next_val}")
else:
    print("Елемент 4 не знайдено або він останній.")