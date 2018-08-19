import unittest
from subwords import random_sized_chunks, random_sized_subwords, generate_word_subwords


class RandomChunksTestCase(unittest.TestCase):

    def test_chunks_for_four(self):
        for x in range(10):
            chunks = random_sized_chunks(4, 10)
            self.assertEqual(len(chunks), 4)
            self.assertEqual(chunks[-1], 10)
            # No duplicates
            self.assertTrue(len(set(chunks)) == len(chunks))


class RandomSubwordsTestCase(unittest.TestCase):
    def test_random_subs(self):
        word = 'football'
        for x in range(5):
            subs = list(random_sized_subwords(4, word))
            print(subs)
        self.assertTrue(True)

class WordSubwordsTestCase(unittest.TestCase):

    word_list = ['footbal', 'table', 'tabletennis']

    def test_word_list(self):
        for word in self.word_list:
            subs = generate_word_subwords(word)
            print(subs)
            print(10 * '*')



if __name__ == '__main__':
    unittest.main()
