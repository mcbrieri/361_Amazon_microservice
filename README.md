# 361_Amazon_microservice
Python microservice using ZMQ: This microservice will receive a Beta fish disease from the user in the form of a string. It will use that string to search a dictionary of treatment links and if the disease passed matched one of the keys in the dictionary, the microservice will return a list object that contains links (in the form of strings) to Amazon products recommended for treatment.  


A. Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.

  1. import zmq
  2. set up your sockets (making sure to connect to correct server):

         socket = zmq.Context().socket(zmq.REQ)
         socket.connect("tcp://127.0.0.1:5000")
     
  3. Send request:
     
         def request_link(disease):
         socket.send_string(disease)
     

     Example call:
     
           print(request_link("Dropsy"))
     

B. Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.

  1. Receive link through previously set up socket (using error handling if unsuccessful:
     
         try:
            treatment_links = socket.recv_pyobj()
            return treatment_links
         except zmq.ZMQError as e:
            print(f"An error occurred: {e}")

  treatment_links will be a python list object containing a list of Amazon links with associated treatment items.

  Example (for if Dropsy was the disease passed in by the user):
  Would return:
  
  [
"https://www.amazon.com/API-AQUARIUM-Freshwater-Aquarium-16-Ounce/dp/B000255NIC/ref=sr_1_5_pp?crid=2XVNUK58MG7JZ&keywords=aquarium+salt&qid=1700420360&sprefix=aquarium+sal%2Caps%2C220&sr=8-5", 
"https://www.amazon.com/dp/B00CJ0VY8G?adId=B00CJ0VY8G&ref-refURL=https%3A%2F%2Fbettaboxx.webflow.io%2Fbetta-disease-illness%2Fbacterial-infection&slotNum=0&imprToken=aa2888f48105bdc5232f6face7e255ef&adType=smart&adMode=manual&adFormat=card&impressionTimestamp=1633175544164&linkCode=ll1&tag=bettaboxx-20&linkId=2d455a23214b7a5eb63f2514bfb10574&language=en_US&ref_=as_li_ss_tl&th=1"
]


C. UML sequence diagram showing how requesting and receiving data works:
![updated UML](https://github.com/mcbrieri/361_Amazon_microservice/assets/108555262/8f0ea6e7-50d1-45cc-9ec4-ed6640321f57)

