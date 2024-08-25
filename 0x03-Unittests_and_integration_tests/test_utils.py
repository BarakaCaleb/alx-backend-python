#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map

"""
This is the test case for the function access_nested_map
Implement the TestAccessNestedMap.test_access_nested_map method to test that the method returns what it is supposed to."""

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({'a': 1}, ['a'], 1),
        ({'a': {'b': 2}}, ['a', 'b'], 2),
        ({'a': {'b': 2}}, ['a'], {'b': 2}),
        ({'a': {'b': 2}}, ['c'], None),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)


class TestAccessNestedMap.test_access_nested_map_exception(unittest.TestCase):
    @parameterized.expand([
        ({'a': 1}, ['a', 'b']),
        ({'a': {'b': 2}}, ['a', 'c']),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
