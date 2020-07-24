import threading


def detTimer(duration, func):
    return threading.Timer(interval=duration, function=func)
