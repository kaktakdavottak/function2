from utils.mydecorator import log_writer_with_path


class Contact:

    @log_writer_with_path('C:\\Users\\semen\\Documents\\GitHub\\function2\\')
    def __init__(self, name, surname, number, favorites=False, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        self.add_info = kwargs
        if favorites:
            self.favorites = 'Да'
        else:
            self.favorites = 'Нет'

    def __str__(self):
        contact_data = 'Имя: {}\nФамилия: {}\nТелефон: {}\n' \
                       'В избранных: {}\nДополнительная информация:\n'.format(self.name, self.surname,
                                                                              self.number, self.favorites)
        for adv_info_key, adv_info_value in self.add_info.items():
            contact_data += '\t {}: {} \n'.format(adv_info_key, adv_info_value)
        return contact_data


class PhoneBook:

    def __init__(self, phonebook_name):
        self.name = phonebook_name
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def print_all_contacts(self):
        for contact in self.contacts:
            print(contact)

    def del_contact_by_number(self, number):
        for contact in self.contacts[:]:
            if contact.number == number:
                self.contacts.remove(contact)

    def print_favorites_contacts(self):
        for contact in self.contacts:
            if contact.favorites == 'Да':
                print(contact)

    def search_by_name(self, name, surname=''):
        for contact in self.contacts:
            if name == contact.name:
                print(contact)
            elif surname == contact.surname:
                print(contact)


if __name__ == "__main__":
    # Создание книги
    pb1 = PhoneBook('Телефонная книга')

    # Добавление контактов
    pb1.add_contact(Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com'))
    pb1.add_contact(Contact('Sem', 'Smith', '+73535353454', favorites=True, telegram='@sem', email='sem@smith.com'))
    pb1.add_contact(Contact('Den', 'Adams', '+1'))

    # Вывод всех контактов
    pb1.print_all_contacts()

    # Удаление контакта по номеру
    pb1.del_contact_by_number('+1')

    # Вывод всех избранных
    pb1.print_favorites_contacts()

    # Поиск и вывод по имени и фамилии
    pb1.search_by_name('Sem', 'Adams')


