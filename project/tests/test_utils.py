import pytest
from utils.calcoli import sottrazione, moltiplicazione, divisione


def test_sottrazione():
    assert sottrazione(5, 5) == 0


def test_moltiplicazione():
    assert moltiplicazione(10, 2) == 20


def test_divisione():
    assert divisione(100, 5) == 20
