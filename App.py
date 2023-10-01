#firebasee
from pyrebase import pyrebase
#OS
import os

#Facial Tracker and Recorder
import TrackNRecord as tr

def Upload(filename):
    print("Uploading to Firebase...")
    print("File selected: " + filename)
     #firebase id
    config = {
      'apiKey': "AIzaSyBCLYNAsV6vFrOJ0iCUlI5fnr7h6V-lbxI",
      'authDomain': "ecea120d-video-upload.firebaseapp.com",
      'projectId': "ecea120d-video-upload",
      'storageBucket': "ecea120d-video-upload.appspot.com",
      'messagingSenderId': "112995751288",
      'appId': "1:112995751288:web:d4768d5a8e1bdb7d73a48d",
      'measurementId': "G-Y7NP0JKC10",
       'databaseURL': ""
    }
    
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    
    path_on_cloud = filename
    path_local = filename
    
    storage.child(path_on_cloud).put(path_local)
    
    
if __name__== "__main__":
    print("Launching app...")
    os.system('cls')
    filename = tr.TrackNRecord() #Resulting output filename of the app.
    print("=================================================")
    print("Output file saved as: " + filename)
    Upload(filename)
    print("Exiting app...")