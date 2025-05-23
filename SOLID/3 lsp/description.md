# Принцип подстановки Барборы Лисков (Liskov Substitution Principle, LSP)

Принцип подстановки Барборы Лисков звучит как: **функции, которые используют базовый тип, должны иметь возможность использовать подтипы базового типа, не зная об этом.**

## По человечески

**Для любого класса клиент должен иметь возможность использовать любой подкласс базового класса, не замечая разницы между ними**, и следовательно, без каких-либо изменений поведения программы при выполнении.

## Как это реализовано в коде

### Класс `Position`

Класс `Position` отвечает исключительно за представление координат на плоскости. Его задачи включают:

- Хранение координат `x` и `y`.
- Предоставление строкового представления координат.

#### Методы класса `Position`:
- `__init__(x, y)`: Инициализирует координаты `x` и `y`. По умолчанию координаты равны `(0, 0)`.
- `__str__()`: Возвращает строковое представление координат в формате `(x, y)`.

Этот класс не содержит дополнительной логики, связанной с персонажами или их действиями, что соответствует принципу SRP.

---

### Класс `Character`

Класс `Character` является суперклассом, который определяет базовую логику для всех персонажей. Его задачи включают:

- Инициализацию имени и начальной позиции персонажа.
- Определение базового метода перемещения.

#### Методы класса `Character`:
- `__init__(name)`: Инициализирует имя персонажа и его начальную позицию (по умолчанию `(0, 0)`).
- `move(destination)`: Перемещает персонажа на новую позицию, выводя соответствующее сообщение.

Этот класс предоставляет общий интерфейс для всех дочерних классов, таких как `Human` и `Dragon`.

---

### Классы `Human` и `Dragon`

Классы `Human` и `Dragon` являются дочерними классами `Character`. Они расширяют логику родительского класса, добавляя специфические действия для каждого типа персонажа. При этом они соблюдают принцип полиморфизма, переопределяя метод `move` для своей уникальной логики.

#### Класс `Human`
- Переопределяет метод `move`, чтобы описать движение человека как "идёт".
- Добавляет метод `buy`, который реализует уникальное действие для человека — покупку предметов.

#### Класс `Dragon`
- Переопределяет метод `move`, чтобы описать движение дракона как "летит".
- Добавляет метод `attack`, который реализует уникальное действие для дракона — атаку пламенем.

---

### Функция `move`

Функция `move` демонстрирует использование полиморфизма. Она принимает объект типа `Character` (или его потомков) и вызывает метод `move`, не зная конкретного типа объекта. Это позволяет ей работать с любым персонажем, будь то `Character`, `Human` или `Dragon`.

#### Параметры функции `move`:
- `character`: Объект типа `Character` или его потомков.
- `destination`: Целевая позиция, куда должен переместиться персонаж.

---

## Преимущества

1. **Четкое разделение обязанностей**:  
   - Класс `Position` отвечает только за хранение и представление координат.
   - Класс `Character` определяет базовую логику для всех персонажей.
   - Классы `Human` и `Dragon` добавляют уникальные действия, не затрагивая базовую логику.

2. **Полиморфизм**:  
   - Функция `move` работает с любым объектом, который реализует метод `move`, независимо от его конкретного типа.

3. **Расширяемость**:  
   - Легко добавить новые типы персонажей (например, `Elf` или `Wizard`) без изменения существующего кода.

4. **Тестируемость**:  
   - Каждый класс можно тестировать независимо от других.

5. **Читаемость**:  
   - Код легко понять благодаря четкому разделению обязанностей и использованию полиморфизма.

---