import pytest

@pytest.mark.parametrize("input,expected", [
    ("input1", "expected1"),  # ID: test_feature_1
    ("input2", "expected2"),  # ID: test_feature_2
])
def test_sample(input, expected):
    assert True
