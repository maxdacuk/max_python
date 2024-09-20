class SumOfNumbers:
    def __init__(self):
        self.count = 0
    
    def calculate(self):
        for a in range(1, 8):
            for b in range(a + 1, 9):
                for c in range(b + 1, 10):
                    self.count += 1
    
    def get_count(self):
        return self.count

# Створюємо об'єкт класу
numbers = SumOfNumbers()

# Викликаємо метод для підрахунку
numbers.calculate()

# Виводимо результат
print("Кількість трицифрових чисел зі строгим зростанням цифр:", numbers.get_count())