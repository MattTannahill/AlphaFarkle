import main
import unittest.mock


class TestThrow(unittest.TestCase):

    def test_invalid_number_of_dice(self):
        for dice in [0, 7]:
            with self.assertRaises(Exception) as cm:
                main.throw(dice)

            self.assertEqual((f'the number of dice thrown is not between 1 and 6: {dice}',), cm.exception.args)

    @unittest.mock.patch('main.random.choices')
    def test_sample_returned(self, mock_choices):
        for dice in [1, 5]:
            mock_choices.return_value = [6, 1, 1, 1, 1, 1]
            self.assertEqual(sorted(mock_choices.return_value), main.throw(dice))
            mock_choices.assert_called_with(range(1, 7), k=dice)


class TestScore(unittest.TestCase):

    def test_invalid_number_of_dice(self):
        for dice in [
            [],
            [1, 1, 1, 1, 1, 1, 1]
        ]:
            with self.assertRaises(Exception) as cm:
                main.score(dice, 0)

            self.assertEqual((f'the number of dice kept is not between 1 and 6: {len(dice)}',), cm.exception.args)

    def test_invalid_die_values(self):
        for die in [0, 7, 1.5, 'not a number']:
            with self.assertRaises(Exception) as cm:
                main.score([die], 0)

            self.assertEqual((f'die value is not an integer in range [1, 6]: {die}',), cm.exception.args)

    def test_six_of_a_kind(self):
        for die in [1, 5]:
            self.assertEqual(3000, main.score([die, die, die, die, die, die], 0))

    def test_five_of_a_kind(self):
        for die in [1, 5]:
            self.assertEqual(2000, main.score([die, die, die, die, die], 0))

    def test_two_triplets(self):
        self.assertEqual(2500, main.score([1, 1, 1, 2, 2, 2], 0))

    def test_straight(self):
        self.assertEqual(1500, main.score(range(1, 7), 0))

    def test_three_pairs(self):
        self.assertEqual(1500, main.score([1, 1, 2, 2, 3, 3], 0))

    def test_four_of_a_kind(self):
        for die in [3, 5]:
            self.assertEqual(1000, main.score([die, die, die, die], 0))

    def test_triplet(self):
        for die in range(1, 7):
            self.assertEqual(1000 if die == 1 else die * 100, main.score([die, die, die], 0))

    def test_ones(self):
        self.assertEqual(100, main.score([1], 0))
        self.assertEqual(100 * 2, main.score([1, 1], 0))

    def test_fives(self):
        self.assertEqual(50, main.score([5], 0))
        self.assertEqual(50 * 2, main.score([5, 5], 0))

    def test_combinations(self):
        self.assertEqual(750, main.score([1, 5, 6, 6, 6], 0))
        self.assertEqual(1150, main.score([1, 5, 6, 6, 6, 6], 0))
        self.assertEqual(1100, main.score([1, 1, 1, 1], 0))  # triple + single
        self.assertEqual(1150, main.score([1, 1, 1, 1, 5], 0))
        self.assertEqual(2050, main.score([1, 1, 1, 1, 1, 5], 0))

    def test_farkle(self):
        self.assertEqual(0, main.score([2], 0))
        self.assertEqual(0, main.score([2], 1))
        self.assertEqual(-1000, main.score([2], 2))


if __name__ == '__main__':
    unittest.main()
