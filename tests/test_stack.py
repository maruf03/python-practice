import pytest
from stack import Stack

@pytest.fixture
def empty_stack():
    return Stack()


def test_push_and_pop(empty_stack):
    empty_stack.push(1)
    empty_stack.push(2)

    assert empty_stack.pop() == 2
    assert empty_stack.pop() == 1
