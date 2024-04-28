import queue
import uuid

request_queue = queue.Queue()

counter = 0

def generate_request_id():
    global counter
    counter += 1
    return counter

def generate_request():
    new_request = {"id": generate_request_id()}
    request_queue.put(new_request)
    print(f"New request {new_request['id']} added to the queue")


def process_request():
    if request_queue.empty():
        print("Request queue is empty")
        return
   
    current_request = request_queue.get()
    print(f"Processing request {current_request['id']}")


while True:
    user_input = input("Press 'Enter' to continue or 'q' to quit: ")

    if user_input.lower() == "q":
        break

    generate_request()
    process_request()