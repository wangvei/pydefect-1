# -*- coding: utf-8 -*-
#  Copyright (c) 2020. Distributed under the terms of the MIT License.


class PydefectError(Exception):
    pass


class NoSupercellError(PydefectError):
    pass


class NotPrimitiveError(PydefectError):
    pass