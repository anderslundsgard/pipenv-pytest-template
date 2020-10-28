import os
# from python_files.src import main

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_test_resource(file_name):
    return os.path.join(__location__, 'test_resources', file_name)


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
