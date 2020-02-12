import unittest
from parameterized import parameterized

from file_reader.base import read_file, parse_line


class TestBase(unittest.TestCase):

    def _select_attr(self, list_, attr):
        return [getattr(element, attr, None) for element in list_]

    @parameterized.expand([
        ('integer', '-98', -98.),
        ('float', '1.98', 1.98),
        ('string', 'this is a string', 'this is a string'),
        ('none', None, None)
    ])
    def test__parse_line(self, name, input, expected):
        self.assertEqual(parse_line(input), expected)

    def test__read(self):
        files = {}
        read_file('tests/data/file_a.txt', files)
        self.assertListEqual(
            list(files.keys()),
            ['tests/data/file_a.txt',
             'tests/data/file_b.txt',
             'tests/data/file_c.txt'])
        self.assertEqual(self._select_attr(files.values(), 'sum_numbers'),
                         [11., -24., 100000.5])
