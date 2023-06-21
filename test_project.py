from project import helper, open_file, input_word, input_errors
# from pytest import monkeypatch
import pytest

open_file()

def test_input_word(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "adieu")
    assert(input_word()) == ["a", "d", "i", "e", "u"]


def test_input_errors(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "22222")
    assert(input_errors()) == ["2", "2", "2", "2", "2"]


def test_helper():
    assert helper(["a", "d", "i", "e", "u"], ["2", "2", "2", "2", "2"]) == ['adieu\n']

