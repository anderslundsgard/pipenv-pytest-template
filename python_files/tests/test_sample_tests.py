import os
import pytest
from pkg.main import main, raises_exception


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_test_resource(file_name):
    return os.path.join(__location__, 'test_resources', file_name)


@pytest.fixture
def reuse_me():
    arr = []
    return arr


def test__reuse_arr(reuse_me):
    # Arrange
    reuse_me.append('dummy')

    # Assert
    assert len(reuse_me) == 1


def test__sample_test():
    # Arrange
    test_file = os.path.join(__location__, 'test_data', 'sample_lambda_event.txt')

    with open(test_file, 'r') as file:
        notification = file.read()

    event = eval(notification)

    # Act
    # handler(event, None)

    # Assert
    assert event is not None


def test__main():
    # Arrange

    # Act
    main()

    # Assert


def test_pytest_exception():
    # Arrange

    # Act, Assert
    with pytest.raises(Exception):
        raises_exception()
