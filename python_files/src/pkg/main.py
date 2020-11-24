import time


def main():
    print('\nHELLO FROM MAIN!!')


def raises_exception():
    raise Exception('Noooooo!')


def calling_sleep_100():
    response = sleep_100()
    return response


def sleep_100():
    time.sleep(100)
    return 'I slept for 100 seconds...'


if __name__ == '__main__':
    main()
