import threading

class Worker(threading.Thread):
    """Our workers constructor, note the super()
     method which is vital if we want this to
     function properly.

    Args:
        threading ([type]): [description]
    """

    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        for i in range(10):
            print(i)