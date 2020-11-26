import os
import pytest
from pkg import main


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
    main.main()

    # Assert


def test__pytest_exception():
    # Arrange

    # Act, Assert
    with pytest.raises(Exception):
        main.raises_exception()


def test__sample_mock(mocker):
    # Arrange
    mocker.patch('pkg.main.sleep_100', return_value='sleep_100 mocked!')

    # Act
    response = main.calling_sleep_100()

    # Assert
    assert response == 'sleep_100 mocked!'


@pytest.mark.skip(reason="Just skip this test for demo")
def test__skip_me():
    # Arrange
   
    # Act
   
    # Assert
    assert 1 == 0
