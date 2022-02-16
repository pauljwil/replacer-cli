import unittest
import re
import sys

sys.path.insert(0, '/Users/pwilliams/Documents/github/replacer-cli/replacer')

import replacer

class TestReplacer(unittest.TestCase):
    """Test the find replace functions."""

    def test_find(self):
        """Test the find() function."""
        found = replacer.find('../example/example1.rst', 'Hello')
        self.assertEqual(found, 3)

    def test_find_iterator(self):
        """Test the find_iterator() function."""
        found = replacer.find_iterator('../example', 'Hello')
        self.assertEqual(found, 9)

    def test_replace_1(self):
        """Test the replace() function."""
        with open('../example/example1.rst', 'r') as f:
            text = f.read()
            old = len(re.findall('Paul', text))
        replacer.replace('../example/example1.rst', 'Paul', 'Mr. Williams')
        with open('../example/example1.rst', 'r') as f:
            text = f.read()
            new = len(re.findall('Mr. Williams', text))
        self.assertEqual(old, new)

    def test_replace_2(self):
        """Test replacing the original text with the replace() function."""
        with open('../example/example1.rst', 'r') as f:
            text = f.read()
            new = len(re.findall('Mr. Williams', text))
        replacer.replace('../example/example1.rst', 'Mr. Williams', 'Paul')
        with open('../example/example1.rst', 'r') as f:
            text = f.read()
            old = len(re.findall('Paul', text))
        self.assertEqual(new, old)

    def test_replace_iterator_1(self):
        """Test the replace_iterator() function."""
        with open('../example/example1.rst', 'r') as f:
            text = f.read()
            ex1 = len(re.findall('Paul', text))
        with open('../example/example2.rst', 'r') as f:
            text = f.read()
            ex2 = len(re.findall('Paul', text))
        with open('../example/example3.rst', 'r') as f:
            text = f.read()
            ex3 = len(re.findall('Paul', text))
        old = ex1 + ex2 + ex3
        replacer.replace_iterator('../example', 'Paul', 'Mr. Williams')
        with open('../example/example1.rst', 'r') as f:
            text = f.read()
            ex1 = len(re.findall('Mr. Williams', text))
        with open('../example/example2.rst', 'r') as f:
            text = f.read()
            ex2 = len(re.findall('Mr. Williams', text))
        with open('../example/example3.rst', 'r') as f:
            text = f.read()
            ex3 = len(re.findall('Mr. Williams', text))
        new = ex1 + ex2 + ex3
        self.assertEqual(old, new)

    def test_replace_iterator_2(self):
        """Test replacing the original text with the replace_iterator() function."""
        with open('../example/example1.rst', 'r') as f:
            text = f.read()
            ex1 = len(re.findall('Mr. Williams', text))
        with open('../example/example2.rst', 'r') as f:
            text = f.read()
            ex2 = len(re.findall('Mr. Williams', text))
        with open('../example/example3.rst', 'r') as f:
            text = f.read()
            ex3 = len(re.findall('Mr. Williams', text))
        new = ex1 + ex2 + ex3
        replacer.replace_iterator('../example', 'Mr. Williams', 'Paul')
        with open('../example/example1.rst', 'r') as f:
            text = f.read()
            ex1 = len(re.findall('Paul', text))
        with open('../example/example2.rst', 'r') as f:
            text = f.read()
            ex2 = len(re.findall('Paul', text))
        with open('../example/example3.rst', 'r') as f:
            text = f.read()
            ex3 = len(re.findall('Paul', text))
        old = ex1 + ex2 + ex3
        self.assertEqual(new, old)

if __name__ == '__main__':
    unittest.main()
