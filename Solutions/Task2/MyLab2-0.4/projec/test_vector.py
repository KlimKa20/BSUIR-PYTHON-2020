import pytest
from projec.Vector import Vector

class TestVector:
    def test_type_error(self):
        with pytest.raises(RuntimeError):
            Vector('ololo')

    def test_zero(self):
        assert(str(Vector([0]))=="0")

    def test_the_comparison_signs(self):
        assert (Vector([4, 3, 4]) < Vector([2, 3, 2])) == False
        assert (Vector([4, 3, 4]) > Vector([2, 3, 2])) == True
        assert (Vector([4, 3, 4]) <= Vector([2, 3, 2])) == False
        assert (Vector([4, 3, 4]) >= Vector([2, 3, 2])) == True
        assert (Vector([4, 3, 4]) == Vector([4, 3, 4])) == True
        assert (Vector([4, 3, 4]) != Vector([2, 3, 2])) == True

    def test_the_operations(self):
        assert (Vector([4, 3, 4]) - Vector([2, 3, 2])) == Vector([2, 0, 2])
        assert (Vector([4, 3, 4]) - 2) == None
        assert (Vector([4, 3, 4]) + 2) == None
        assert (Vector([4, 3, 4]) * "ad") == None
        assert ("sd" * Vector([4, 3, 4])) == None
        assert (Vector([4, 3, 4]) + Vector([2, 3, 2])) == Vector([6, 6, 6])
        assert (Vector([4, 3, 4]) * Vector([2, 3, 2])) == Vector([8, 9, 8])
        assert (Vector([4, 3, 4]) * 2) == Vector([8, 6, 8])
        assert (2 * Vector([4, 3, 4])) == Vector([8, 6, 8])

    def test_len(self):
        assert Vector([2, 2, 2, 2]).len() == 4

    def test_getitem(self):
        assert Vector([2, 2, 3, 2])[2] == 3