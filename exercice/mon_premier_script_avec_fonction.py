import unittest


MINIMUM_NAME_LENGTH = 7


def count_names_longer_than(names: list[str], minimum_length: int) -> int:
    """Count names with more than `minimum_length` letters."""
    return sum(1 for name in names if len(name) > minimum_length)


class TestCountNamesLongerThan(unittest.TestCase):

    def setUp(self):
        self.first_names = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]

    def test_returns_correct_count_when_multiple_names_exceed_minimum_length(self):
        result = count_names_longer_than(names=self.first_names, minimum_length=MINIMUM_NAME_LENGTH)
        self.assertEqual(result, 4)

    def test_returns_zero_when_no_name_exceeds_minimum_length(self):
        result = count_names_longer_than(names=["Ali", "Bob", "Eva"], minimum_length=MINIMUM_NAME_LENGTH)
        self.assertEqual(result, 0)

    def test_returns_total_count_when_all_names_exceed_minimum_length(self):
        result = count_names_longer_than(names=["Guillaume", "Cassandre"], minimum_length=MINIMUM_NAME_LENGTH)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()