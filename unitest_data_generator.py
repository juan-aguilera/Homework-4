import unittest
import data_generator
import constants


class DataGeneratorTest(unittest.TestCase):
    def test_data_generator_with_empty_array(self):
        N = 0
        random_array = data_generator.random_list(N)
        self.assertTrue(N == len(random_array))
        pass

    def test_data_generator_with_1(self):
        N = 1
        random_array = data_generator.random_list(N)
        self.assertTrue(N == len(random_array))
        pass

    def test_data_generator_with_2(self):
        N = 2
        random_array = data_generator.random_list(N)
        self.assertTrue(N == len(random_array))
        pass

    def test_data_generator_with_1000(self):
        N = 1000
        random_array= data_generator.random_list(N)
        self.assertTrue(N == len(random_array))
        for number in random_array:
            self.assertTrue(number <= constants.MAX_VALUE)
            self.assertTrue(number >= 0)
        pass
    #def test_target_generator(self):
        #N = 1000
        #random_array= data_generator.random_list(N)
        #random_target = data_generator.gen_target(random_array)
        #self.assertTrue(random_target in random_array)


if __name__ == "__main__":
    unittest.main()