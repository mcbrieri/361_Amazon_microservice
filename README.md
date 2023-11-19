# 361_Amazon_microservice
Python microservice using ZMQ: receives request from client in the form of an ailment, checks dictionary of treatments and returns a link (in the form of a string) to the associated treatment list if the ailment received is found in the dictionary.


A. Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.

  1. import zmq
  2. set up your sockets (making sure to connect to correct server):

         socket = zmq.Context().socket(zmq.REQ)
         socket.connect("tcp://127.0.0.1:5000")
     
  3. Send request:
     
         def request_link(ailment):
         socket.send_string(ailment)
     

     Example call:
     
           print(request_link("A"))

     This will print: "Link to treatment A"

     Here "A" is a place holder for an ailment and "Link to treatment A" is a place holder for the link to an Amazon list with treatment items for the associated ailment. 
     

B. Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.

  1. Receive link through previously set up socket (using error handling if unsuccessful:
     
         try:
            treatment_link = socket.recv_string()
            return treatment_link
         except zmq.ZMQError as e:
            print(f"An error occurred: {e}")

  treatment_link will be a string containing the address of the Amazon list with associated treatment items.


C. UML sequence diagram showing how requesting and receiving data works:

![microservice_UML_Assignment9](https://github.com/mcbrieri/361_Amazon_microservice/assets/108555262/3d6bbf36-ff50-40b6-ad44-ea6ebbf52450)
