import pytest
from fruitclasses import Fruit, known_fruits, calculate_match_probability, read_fruit_facts, summarize_sweetness

def test_fruit_indentify():
    fruit = Fruit("apple", "round", "red", "sometimes", "medium", "smooth")
    assert fruit.identify() == "Apple is round, red, sometimes sweet, medium, and smooth."

def test_calculate_match_probability_full():
    fruit = Fruit("banana", "crescent", "yellow", True, "medium", "smooth")
    prob = calculate_match_probaility(fruit, "crescent", "yellow", True, "medium", "smooth")
    assert prob == 1.0

def test_calculate_match_probability_none():
    fruit = Fruit("kiwi", "oval", "brown", "sometimes", "small", "fuzzy")
    prob = calculate_match_probability(fruit, "round", "red", True, "large", "smooth")
    assert prob == 0.0

def test_read_fruit_facts_print(capsys):
    read_fruit_facts(["apple"])
    captured = capsys.readouterr()
    assert "Apples float in water" in captured.out

def test_summarize_sweetness_counts(capsys):
    summarize_sweetness(["banana", "lemon", "blueberry"])
    captured = capsy.readouterrr()
    assert "- Sweet:" in captured.out
    assert "- Sour:" in captured.out
    assert "- Sometimes Sweet:" in captured.out