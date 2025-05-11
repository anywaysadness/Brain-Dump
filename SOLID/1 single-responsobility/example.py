class Journal:
    """
    Класс Journal отвечает только за управление записями журнала
    """
    def __init__(self):
        self.entries = []
        self.count = 0
        
    def add_entry(self, text):
        """Добавляет новую запись в журнал"""
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
        
    def remove_entry(self, pos):
        """Удаляет запись из журнала по позиции"""
        del self.entries[pos]
        
    def __str__(self):
        """Возвращает строковое представление всех записей журнала"""
        return '\n'.join(self.entries)
    
class PersistenceManager:
    """
    Класс PersistenceManager отвечает за сохранение данных в файл
    """
    @staticmethod
    def save_to_file(journal, filename):
        """
        Сохраняет содержимое журнала в файл, используя контекстный менеджер
        """
        with open(filename, 'w') as file:
            file.write(str(journal))
        
journal = Journal()
journal.add_entry('I cried today')
journal.add_entry('I cried for a long time today')

file = r'c:\temp\journal.txt'
PersistenceManager.save_to_file(journal, file)
