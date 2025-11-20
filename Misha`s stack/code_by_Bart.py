# Функції для роботи зі стеком
def create_stack():
    """Створює та повертає порожній стек (список)."""
    return []

def is_full(stack, capacity):
    """Перевіряє, чи стек заповнений."""
    return len(stack) >= capacity
    
def is_empty(stack):
    """Перевіряє, чи стек порожній."""
    return len(stack) == 0

def add_item(stack, item, capacity):
    """Додає елемент до стека, якщо він не повний. Не повертає значення."""
    if not is_full(stack, capacity):
        stack.append(item)
    else:
        # Повідомляємо користувача, якщо стек повний
        print("Помилка: Стек повний. Неможливо додати елемент.")

def remove_item(stack):
    """Видаляє елемент зі стека, якщо він не порожній. Не повертає значення."""
    if not is_empty(stack):
        stack.pop()
    else:
        # Повідомляємо, якщо стек вже порожній
        print("Помилка: Стек порожній. Неможливо видалити елемент.")

# --- Основна частина програми ---

# 1. Ініціалізація стека
try:
    capacity = int(input("Введіть ємність стека: "))
except ValueError:
    print("Некоректне значення. Будь ласка, введіть ціле число.")
    exit() # Завершуємо програму, якщо введено не число

main_stack = create_stack()

# 2. Заповнення стека
print(f"Введіть {capacity} елементів для стека:")
for _ in range(capacity): # Використовуємо _, бо сама змінна циклу нам не потрібна
    try:
        item = int(input("Введіть елемент: "))
        add_item(main_stack, item, capacity)
    except ValueError:
        print("Будь ласка, вводьте тільки цілі числа.")
        # Можна додати логіку, щоб повторити спробу вводу

print(f"\nВаш початковий стек: {main_stack}")

# 3. Розділення елементів на парні та непарні
stack_even = create_stack()
stack_odd = create_stack()

for item in main_stack:
    if item % 2 == 0:
        # Ємність для нових стеків може бути такою ж, як і для основного
        add_item(stack_even, item, capacity)
    else:
        add_item(stack_odd, item, capacity)

print(f"Стек з парними числами: {stack_even}")
print(f"Стек з непарними числами: {stack_odd}")

# 4. Демонстрація видалення (якщо потрібно)
print("\nДемонстрація видалення останнього елемента з основного стека:")
remove_item(main_stack)
print(f"Основний стек після видалення: {main_stack}")