import zmq
import time

socket = zmq.Context().socket(zmq.REQ)
print("connecting to server...SUB")
socket.connect("tcp://127.0.0.1:5000")
print("connected to port 5000")

def request_links(disease):
    print("Sending treatment request...")
    time.sleep(1)
    socket.send_string(disease)

    print("Receiving treatment links...")
    try:
        treatment_links = socket.recv_pyobj()
        print("Received treatment links:")
        time.sleep(1)
        return treatment_links
    except zmq.ZMQError as e:
        print(f"An error occurred: {e}")

print(request_links("Dropsy"))
# print(request_links("Hole in the Head"))
# print(request_links("Velvet"))

