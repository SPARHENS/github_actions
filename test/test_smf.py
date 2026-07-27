import pytest
import json
import pathlib

from src import add, sub


second_parent_path = pathlib.Path(__file__).resolve().parents[0]
with open(f"{second_parent_path}/data/test_add.json", "r") as f:
    add_data = json.load(f)

with open(f"{second_parent_path}/data/test_sub.json", "r") as f:
    sub_data = json.load(f)

add_data = [{k: int(v) for k, v in item.items()} for item in add_data]
sub_data = [{k: int(v) for k, v in item.items()} for item in sub_data]

@pytest.mark.parametrize("for_add", add_data)

def test_add(for_add):
    a = int(for_add["a"])
    b = int(for_add["b"])
    expected_result = int(for_add["add"])

    result = add(a, b)

    assert result == expected_result

@pytest.mark.parametrize("for_sub", sub_data)

def test_sub(for_sub):
    a = int(for_sub["a"])
    b = int(for_sub["b"])
    expected_result = int(for_sub["sub"])

    result = sub(a, b)

    assert result == expected_result
