import pytest
from projec.Vector import Vector

class TestVector:
    def test_type_error(self):
        with pytest.raises(ValueError):
            Vector('ololo')
        with pytest.raises(ValueError):
            Vector([23,"fsad"])


    def test_zero(self):
        assert(str(Vector([0]))=="0")

    def test_the_comparison_signs(self):
        assert (Vector([4, 3, 4]) < Vector([2, 3, 2])) == False
        assert (Vector([4, 3, 4]) > Vector([2, 3, 2])) == True
        assert (Vector([4, 3, 4]) <= Vector([2, 3, 2])) == False
        assert (Vector([4, 3, 4]) >= Vector([2, 3, 2])) == True
        assert (Vector([4, 3, 4]) == Vector([4, 3, 4])) == True
        assert (Vector([4, 3, 4]) != Vector([2, 3, 2])) == True
        with pytest.raises(ValueError):
            Vector([4, 3, 4]) < "s"
        with pytest.raises(ValueError):
            Vector([4, 3, 4]) > "s"
        with pytest.raises(ValueError):
            Vector([4, 3, 4]) <= "s"
        with pytest.raises(ValueError):
            Vector([4, 3, 4]) >= "s"
        with pytest.raises(ValueError):
            Vector([4, 3, 4]) == "s"
        with pytest.raises(ValueError):
            Vector([4, 3, 4]) != "s"

    def test_the_operations(self):
        assert (Vector([4, 3, 4]) - Vector([2, 3, 2])) == Vector([2, 0, 2])
        with pytest.raises(ValueError):
            Vector([4, 3, 4]) - 2
        with pytest.raises(ValueError):
            Vector([4, 3, 4]) + 2
        with pytest.raises(ValueError):
            Vector([4, 3, 4]) * "ad"
        with pytest.raises(ValueError):
            "sd" * Vector([4, 3, 4])
        assert (Vector([4, 3, 4]) + Vector([2, 3, 2])) == Vector([6, 6, 6])
        assert (Vector([4, 3, 4]) * Vector([2, 3, 2])) == Vector([8, 9, 8])
        assert (Vector([4, 3, 4]) * 2) == Vector([8, 6, 8])
        assert (2 * Vector([4, 3, 4])) == Vector([8, 6, 8])

    def test_len(self):
        assert Vector([2, 2, 2, 2]).len() == 4

    def test_getitem(self):
        assert Vector([2, 2, 3, 2])[2] == 3
        with pytest.raises(ValueError):
            Vector([2, 2, 3, 2])["dsf"]