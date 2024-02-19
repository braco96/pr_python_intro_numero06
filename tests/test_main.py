import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


def test_tomar():
    assert mod.tomar(1,2,3, n=2) == [1,2]
    assert mod.tomar("a","b") == ["a"]
