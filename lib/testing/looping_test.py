# looping_test.py

from looping import happy_new_year, square_integers, fizzbuzz
import io
import sys

def test_happy_new_year(capsys):
    happy_new_year()
    captured = capsys.readouterr()
    assert captured.out == "10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nHappy New Year!\n"

def test_square_integers():
    assert square_integers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]

def test_fizzbuzz(capsys):
    fizzbuzz()
    captured = capsys.readouterr()
    assert "Fizz" in captured.out
    assert "Buzz" in captured.out
    assert "FizzBuzz" in captured.out