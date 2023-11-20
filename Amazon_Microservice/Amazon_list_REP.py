import zmq
import time
import json

class Reply:
    def __init__(self, socket, filepath):
        self.socket = socket
        self.treatment_links = {}
        with open(filepath) as infile:
            self.treatment_links = json.load(infile)
        
    def get_treatment_links(self, disease):
        if disease in self.treatment_links:
            return self.treatment_links[disease]
        else:
            return "Disease not found in treatment dictionary."

    def reply_link(self):
        while True:
            print("Waiting for treatment request...")
            time.sleep(1)
            disease = self.socket.recv_string()
            print("Received Disease:", disease)
            time.sleep(1)
            
            treatment_links = self.get_treatment_links(disease)

            print("Sending treatment links...", treatment_links)
            time.sleep(1)
            self.socket.send_pyobj(treatment_links)

    def handle_reply(self):
        #wrapper
        self.reply_link()


socket = zmq.Context().socket(zmq.REP)
print("connecting to server...")
socket.bind("tcp://127.0.0.1:5000")
print("listening on port 5000")
reply = Reply(socket, "treatment_links.json")
reply.handle_reply()




