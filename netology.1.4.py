def print(text, start = '', max_line = 0, in_file = False):
    text = str(start) + str(text)

    if max_line > 0 and len(text) // max_line > 1:
        text = list(text)
        line = 0
        while line < len(text) // max_line:
            text.insert((line + 1) * max_line + line, '\n')
            line += 1
        if text[len(text) - 1] == '\n':
            text.pop()
        text = ''.join(text)

    if in_file:
        with open('print.txt', 'w', encoding='utf8') as file:
            file.write(text)

    return __builtins__.print(text)


class Contact():
    def __init__(self, name, surname, number, fav_number = False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        self.other = kwargs

        if fav_number == False:
            self.fav_number = 'нет'
        else:
            self.fav_number = fav_number

    def __str__(self):
        self.other_for_join = []
        for info in self.other:
            self.other_for_join.append('\t\t{} : {}\n'.format(info, self.other[info]))
        self.other_for_join = ''.join(self.other_for_join)
        return 'Имя: {}\nФамилия: {}\nТелефон: {}\nВ избранных: {}\nДополнительная информация:\n{}'.format(self.name, self.surname, self.number, self.fav_number, self.other_for_join)


class PhoneBook():
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def print_contacts(self):
        for contact in self.contacts:
            print(contact)

    def add_contact(self, contact):
        self.contacts.append(contact)
        print('Контакт добавлен')

    def delete_contact(self, number):
        for contact in self.contacts:
            if contact.number == number:
                self.contacts.remove(contact)
                print('Контакт удален')

    def find_fav(self):
        all_fav = []
        for contact in self.contacts:
            if contact.fav_number != 'нет':
                all_fav.append(contact.fav_number)
        return all_fav

    def find_by_name(self, name, surname):
        for contact in self.contacts:
            if contact.name == name and contact.surname == surname:
                return contact
