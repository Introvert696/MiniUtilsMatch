import time

while True:
    print('\r{}'.format(time.strftime("%H:%M:%S")), end='')
    time.sleep(1)