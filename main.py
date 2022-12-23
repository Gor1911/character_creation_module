from random import randint

# Вот она — новая глобальная константа.
DEFAULT_ATTACK = 5
# Новая константа — стандартное значение защиты.
DEFAULT_DEFENCE = 10 
DEFAULT_STAMINA = 80 

class Character:
    # Константа для диапазона очков урона.
    RANGE_VALUE_ATTACK = (1, 3)    
    RANGE_VALUE__DEFENCE = (1, 5)
    # Вот они — две новые константы.
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15

    # Объявляем конструктор класса.
    def __init__(self, name):
        self.name = name
    
   # Объявляем метод атаки
    def attack(self):
        # Вместо диапазона записана переменная класса.
        # Оператор * распаковывает передаваемый кортеж.
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')
  
    # Объявляем метод защиты.
    def defence(self):
        # Вычисляем значение защиты в переменной value_defence.
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')
    
    # Объявляем метод специального умения.
    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}"')
    
    # Новый метод базового класса.
    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.' 

class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'

class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'

class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита' 
    
warrior = Warrior('Кодослав')
print(warrior)
print(warrior.attack())
