from QueueImplementation import *

queue_instance = Queue()
queue_instance.enqueue("create")
queue_instance.enqueue("update")
queue_instance.enqueue("read")
queue_instance.enqueue("delete")
print(queue_instance.dequeue())