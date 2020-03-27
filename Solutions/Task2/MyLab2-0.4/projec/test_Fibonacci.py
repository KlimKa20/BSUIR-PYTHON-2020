import pytest
from projec.Fibonacci import fib

class TestFib:

    def test_type_error(self):
        with pytest.raises(TypeError):
            fib('ololo')

    def test_negative(self):
        assert(fib(-1) == [])

    def test_zero(self):
        assert(fib(0) == 1)

    def test_one(self):
        assert(fib(1) == 1)

    def test_two(self):
        assert(fib(2) == 2)

    def test_three(self):
        assert(fib(3) == 3)

    def test_seven(self):
        assert([fib(n) for n in range(7)] == [1, 1, 2, 3, 5, 8, 13])
