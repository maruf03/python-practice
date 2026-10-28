import pytest
from queue import Queue, Queue2

@pytest.fixture
def empty_queue():
    return Queue()

@pytest.fixture
def empty_queue2():
    return Queue2()


def test_enqueue_and_dequeue(empty_queue):
    empty_queue.enqueue(1)
    empty_queue.enqueue(2)

    assert empty_queue.dequeue() == 1
    assert empty_queue.dequeue() == 2


def test_queue2_enqueue_and_dequeue(empty_queue2):
    empty_queue2.enqueue(1)
    empty_queue2.enqueue(2)

    assert empty_queue2.dequeue() == 1
    assert empty_queue2.dequeue() == 2


def test_queue2_enqueue_and_dequeue_mixed(empty_queue2):
    empty_queue2.enqueue(1)
    empty_queue2.enqueue(2)

    assert empty_queue2.dequeue() == 1

    empty_queue2.enqueue(3)

    assert empty_queue2.dequeue() == 2

    assert empty_queue2.dequeue() == 3
