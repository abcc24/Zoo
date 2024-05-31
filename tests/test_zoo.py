import unittest
from unittest import TestCase
from src.Zoo import Zoo, Fence, ZooKeeper, Animal

class TestZoo(TestCase):
    def setUp(self) -> None:
        self.zookeper1: ZooKeeper = ZooKeeper ("Rocco", "Balocco", "1g")
        self.fence1: Fence = Fence (100, 25.6, "Foresta")
        self.animal1: Animal = Animal("Fenrir", "lupo", 5,1,4, "Foresta")
        self.zoo1: Zoo = Zoo(self.fence1, self.zookeper1)

    def test_1(self):

        self.zookeper1.add_animal(self.animal1, self.fence1)
        result: int = len(self.fence1.animal)
        message: str = "Error: the function add animal should not add animal into fence1"
        self.assertEqual(result, 0, message)
    
    #def test_2(self):



if __name__ == "__main__":
    unittest.main()