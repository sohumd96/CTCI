from Chapter2.linked_list import LinkedList


class Animal:

    def __init__(self, animal):
        self.animal = animal
        self.time = 0

    def set_order(self, time):
        self.time = time


class AnimalShelter:

    def __init__(self):
        self.dog_head = self.dog_tail = None
        self.cat_head = self.cat_tail = None
        self.order = 0

    def enqueue(self, animal):

        animal.set_order(self.order)
        self.order += 1
        node = LinkedList(animal)

        if animal.animal == "Dog":
            if self.dog_head is None:
                self.dog_head = self.dog_tail = node
            else:
                self.dog_tail.next = node
                self.dog_tail = node
        else:
            if self.cat_head is None:
                self.cat_head = self.cat_tail = node
            else:
                self.cat_tail.next = node
                self.cat_tail = node

    def dequeue_dog(self):
        if self.dog_head is None:
            return None
        temp = self.dog_head
        self.dog_head = temp.next

        if self.dog_head is None:
            self.dog_tail = None
        return temp.data

    def dequeue_cat(self):
        if self.cat_head is None:
            return None
        temp = self.cat_head
        self.cat_head = temp.next

        if self.cat_head is None:
            self.cat_tail = None
        return temp.data

    def dequeue_any(self):
        if self.dog_head is None:
            if self.cat_head is None:
                return None
            return self.dequeue_cat()
        elif self.cat_head is None:
            return self.dequeue_dog()
        else:
            return self.dequeue_dog() if self.dog_head.data.time < self.cat_head.data.time else self.dequeue_cat()



