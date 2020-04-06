from unittest import TestCase
from Chapter3.Problem6.animal_shelter import *

class TestAnimalShelter(TestCase):
    def test_animal_shelter(self):
        shelter = AnimalShelter()
        shelter.enqueue(Animal("Dog"))
        shelter.enqueue(Animal("Cat"))
        shelter.enqueue(Animal("Dog"))
        shelter.enqueue(Animal("Dog"))
        shelter.enqueue(Animal("Dog"))
        shelter.enqueue(Animal("Cat"))
        self.assertEqual(shelter.dequeue_cat().time, 1)
        self.assertEqual(shelter.dequeue_any().time, 0)
        self.assertEqual(shelter.dequeue_any().time, 2)
        self.assertEqual(shelter.dequeue_any().time, 3)
        self.assertEqual(shelter.dequeue_cat().time, 5)
