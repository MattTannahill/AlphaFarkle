from main import throw, score
from unittest import main, TestCase
from unittest.mock import patch


class TestThrow(TestCase):

    def test_invalid_number_of_dice(self):
        for dice in [0, 7]:
            with self.assertRaises(Exception) as cm:
                throw(dice)

            self.assertEqual((f'the number of dice thrown is not between 1 and 6: {dice}',), cm.exception.args)

    @patch('main.sample')
    def test_sample_returned(self, mock_sample):
        for dice in [1, 5]:
            mock_sample.return_value = [6, 1, 1, 1, 1, 1]
            self.assertEqual(sorted(mock_sample.return_value), throw(dice))
            mock_sample.assert_called_with(range(1, 7), dice)


class TestScore(TestCase):

    def test_invalid_number_of_dice(self):
        for dice in [
            [],
            [1, 1, 1, 1, 1, 1, 1]
        ]:
            with self.assertRaises(Exception) as cm:
                score(dice)

            self.assertEqual((f'the number of dice kept is not between 1 and 6: {len(dice)}',), cm.exception.args)

    def test_invalid_die_values(self):
        for die in [0, 7, 1.5, 'not a number']:
            with self.assertRaises(Exception) as cm:
                score([die])

            self.assertEqual((f'die value is not in integer between range [1, 6]: {die}',), cm.exception.args)

    def test_six_of_a_kind(self):
        for die in [1, 5]:
            self.assertEqual(3000, score([die, die, die, die, die, die]))

    def test_five_of_a_kind(self):
        for die in [1, 5]:
            self.assertEqual(2000, score([die, die, die, die, die]))

    def test_two_triplets(self):
        self.assertEqual(2500, score([1, 1, 1, 2, 2, 2]))

    def test_straight(self):
        self.assertEqual(1500, score(range(1, 7)))

    def test_three_pairs(self):
        self.assertEqual(1500, score([1, 1, 2, 2, 3, 3]))

    def test_four_of_a_kind(self):
        for die in [3, 5]:
            self.assertEqual(1000, score([die, die, die, die]))

    def test_triplet(self):
        for die in range(1, 7):
            self.assertEqual(1000 if die == 1 else die * 100, score([die, die, die]))

    def test_ones(self):
        self.assertEqual(100, score([1]))
        self.assertEqual(100 * 2, score([1, 1]))

    def test_fives(self):
        self.assertEqual(50, score([5]))
        self.assertEqual(50 * 2, score([5, 5]))

    def test_combinations(self):
        self.assertEqual(750, score([1, 5, 6, 6, 6]))
        self.assertEqual(1150, score([1, 5, 6, 6, 6, 6]))
        self.assertEqual(1100, score([1, 1, 1, 1]))  # a triplet of 1s + one 1 is worth more than the four-of-a-kind
        self.assertEqual(1150, score([1, 1, 1, 1, 5]))
        self.assertEqual(2050, score([1, 1, 1, 1, 1, 5]))

    def test_farkle(self):
        self.assertEqual(0, score([2]))


if __name__ == '__main__':
    main()
