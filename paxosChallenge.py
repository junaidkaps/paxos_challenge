#       Paxos Challenge Script             #
#       By Junaid Kapadia                  #
#       Contact: junaidkaps@gmail.com      #
############################################
import hashlib
import requests
import json
from flask import Flask, jsonify, request
app = Flask(__name__)

global messageHash 


@app.route('/messages', methods=['POST'])
def storeMessage(): 

    #Store inputted message and obtain SHA value using hashlib. 
    message = request.json['message'] 
    hash_object = hashlib.sha256(message) 
    messageSha = hash_object.hexdigest() 

    #Store message and messageSha in a global variable. 
    global messageHash 
    messageHash = { messageSha: message } 
    

    #Return the SHA value of the message in JSON format.  
    return jsonify({"digest": messageSha}), 201

@app.route('/messages/<digest>', methods=['GET'])
def getMessage(digest): 
     
    try: 
	return jsonify({"message": messageHash[digest]}), 201
    except: 
	return jsonify({"err_msg": "Message not found"}), 404 


if __name__ == "__main__":
   app.run(host='0.0.0.0')

