import pytest


def test_stack():
    stack = []
    stack.extend([1, 'two', {3}])
    assert stack.pop() == {3}
    assert stack.pop() == 'two'
    assert stack.pop() == 1


def test_emptiness():
    stack = []
    assert not stack
    stack.append(1)
    assert bool(stack)
    stack.pop()
    assert not stack


import pytest


def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()

