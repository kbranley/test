from project import add


def test_add_edge_cases():
    # large numbers
    assert add(10**9, 10**9) == 2 * 10**9

    # zero
    assert add(0, 0) == 0

    # type hints: mypy will ensure correct usage; runtime remains simple
