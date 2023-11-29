from src.utils import generate_random


def test_generate_random():
    start = 1
    end = 10
    rand = generate_random(start, end)

    assert start <= rand <= end
