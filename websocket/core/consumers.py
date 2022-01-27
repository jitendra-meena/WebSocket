from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class MyConsumer(WebsocketConsumer):
  
    def connect(self):
        self.room_name="Jitendra Meena"
        self.room_group_name="Jitendra"
        async_to_sync(channel_layer.group_add)(self.room_name,self.room_group)
        self.accept()
        self.send(test_data=json.dumps({'status':'connected'}))  
        

       
    
    def receive(self, text_data=None, bytes_data=None):
        # self.send(text_data="Hello world!")
       
        # self.send(bytes_data="Hello world!")
        
        # self.close()
        
        # self.close(code=4123)
        pass
    def disconnect(self, close_code):
        pass

