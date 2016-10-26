#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python_sdk
----------------------------------

Tests for `python_sdk` module.
"""

import unittest

import tradenity


class TestPython_sdk(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(tradenity.__version__)

    def tearDown(self):
        pass
