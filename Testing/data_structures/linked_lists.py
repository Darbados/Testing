class LinkedDevsList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node)
            current_node = current_node.next

    def append_dev(self, name, sector, **kwargs):
        dev = Dev(name, sector, **kwargs)
        if self.head is None:
            self.head = dev
            return

        current_dev = self.head
        while current_dev.next:
            current_dev = current_dev.next
        current_dev.next = dev

    def push_dev(self, name, sector, **kwargs):
        dev = Dev(name, sector, **kwargs)

        current_head = self.head
        self.head = dev
        self.head.next = current_head


class Dev:
    def __init__(self, name, sector, **kwargs):
        self.name = name
        self.sector = sector
        self.level = kwargs.get('level')
        self.next = None

    def __str__(self):
        return f'{self.name} - {self.sector} - {self.level}'


linked_devs = LinkedDevsList()
linked_devs.append_dev('Angel', 'Frontend', level='Lead')
linked_devs.append_dev('George', 'Frontend', level='Junior')
linked_devs.append_dev('Vlado', 'Backend', level='Regular')
linked_devs.append_dev('Misho', 'Backend', level='Mid - Reg')
linked_devs.append_dev('Kaloyan', 'Backend', level='Junior')
linked_devs.append_dev('Pesho', 'Backend', level='Manager, Lead')

linked_devs.print_list()
linked_devs.push_dev('Ivailo', 'Technology', level='CTO')
