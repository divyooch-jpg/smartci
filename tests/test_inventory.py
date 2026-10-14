import pytest
from src.inventory import Inventory

def test_add_stock():
    i = Inventory()
    i.add_stock('pen', 5)
    assert i.stock['pen'] == 5

def test_remove_stock():
    i = Inventory()
    i.add_stock('pen', 5)
    i.remove_stock('pen', 2)
    assert i.stock['pen'] == 3

def test_remove_too_much():
    i = Inventory()
    i.add_stock('pen', 1)
    with pytest.raises(ValueError):
        i.remove_stock('pen', 2)