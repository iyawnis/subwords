import unittest
from subwords import random_sized_chunks, random_sized_subwords, generate_word_subwords, two_letter_subwords


class RandomChunksTestCase(unittest.TestCase):

    def test_chunks_for_four(self):
        for x in range(10):
            chunks = random_sized_chunks(4, 10)
            self.assertEqual(len(chunks), 4)
            self.assertEqual(chunks[-1], 10)
            # No duplicates
            self.assertTrue(len(set(chunks)) == len(chunks))


class RandomSubwordsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('')
        print('RandomSubwordsTestCase')
        print('')

    def test_random_subs(self):
        word = 'football'
        for x in range(5):
            subs = list(random_sized_subwords(4, word))
            print(subs)
        self.assertTrue(True)

class WordSubwordsTestCase(unittest.TestCase):

    word_list = ['football', 'table', 'tabletennis']

    @classmethod
    def setUpClass(cls):
        print('')
        print('WordSubwordsTestCase')
        print('')

    def test_word_list(self):
        for word in self.word_list:
            subs = generate_word_subwords(word)
            print(subs)
            print(10 * '*')

    def test_two_letter_subs(self):
        word = 'football'
        expected = ['fo', 'ot', 'ba', 'll']
        self.assertEqual(list(two_letter_subwords(word)), expected)

    def test_football_out(self):
        word = 'football'
        expected = [['foot', 'ball'], ['fo', 'ot', 'ball']]
        subs = generate_word_subwords(word)
        # Third set of subwords is random, exclude from test for now.
        # Can add all possible combinations for smaller words in future
        self.assertEqual(expected, subs[:2])


if __name__ == '__main__':
    unittest.main()
