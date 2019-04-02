def adv_print(*args, **kwargs):
    start = kwargs.pop('start', '')
    max_line = int(kwargs.pop('max_line', 0))
    in_file = kwargs.pop('in_file', False)
    separator = str(kwargs.pop('sep', ''))

    args = list(args)
    args_for_text = []
    for arg in args:
        args_for_text.append(str(arg) + separator)
    args_for_text[-1] = args_for_text[-1][0:-1]
    text = ''.join(args_for_text)

    text = str(start) +separator + str(text)

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

    print(text, **kwargs)


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


def test():
    arr = ['str', 2, False]
    a = 4
    b = 'dwa'
    adv_print(1, b, 'tri', a, arr, sep='+', end='endoftext', start='startoftext', max_line='8', in_file=True)
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    jhon2 = Contact('Jhon2', 'Smith2', '+2', telegram='@2', email='jhony2@smith.com')
    phone_book = PhoneBook('Книга')
    phone_book.add_contact(jhon)
    phone_book.add_contact(jhon2)
    phone_book.print_contacts()
    phone_book.delete_contact('+2')
    phone_book.print_contacts()

if __name__ == '__main__':
    test()
