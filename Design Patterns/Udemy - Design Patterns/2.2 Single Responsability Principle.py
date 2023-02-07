class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def __str__(self):
        return '\n'.join(self.entries)

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

'''
Так делать нельзя, так как в созданных объектах класса метод сохранения и загрузки может быть свой
и его необходимо менять. Нужно создать отдельный класс
'''
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def low_from_web(self, uri):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')

file = r'd:\temp\journal.txt'

PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())
