# -*- coding: utf-8 -*-
#  Copyright (c) 2020. Distributed under the terms of the MIT License.

import pytest


from pydefect.input_maker.defect import Defect, SimpleDefect
from pydefect.tests.helpers.assertion import assert_msonable


def test_defect_msonable():
    defect = Defect("Va_O1", (1, 2))
    assert_msonable(defect)


def test_simple_defect_msonable():
    defect = SimpleDefect("Va", "O1", [1, 2])
    assert_msonable(defect)


def test_defect_hashable():
    defect = Defect("Va_O1", (1, 2))
    d = {defect: 1}


def test_simple_defect_hashable():
    defect = SimpleDefect(None, "O1", (1, 2))
    d = {defect: 1}


def test_defect_name_and_charges():
    defect = Defect("Va_O1", (1, 2))
    assert defect.str_list == ["Va_O1_1", "Va_O1_2"]


def test_simple_defect():
    defect = SimpleDefect(None, "O1", [1, 2])
    expected = Defect("Va_O1", (1, 2))
    assert defect.name == expected.name
    assert defect.charge_list == expected.charge_list
    assert defect.in_atom is None


"""
TODO
- DefectCharge
- Defect
- SimpleDefect

DONE
"""