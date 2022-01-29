from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from channels.layers import get_channel_layer

class TestConsumer(WebsocketConsumer):
  
    def connect(self):
        self.room_name="test_consumer"
        self.room_group_name="test_consumer_group"
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_add)(self.room_name,self.room_group_name)
        self.accept()
        # self.send(test_data=json.dumps({'status':'connected'}))  
        
        

       
    
    def receive(self, text_data=None, bytes_data=None):
        # self.send(text_data="Hello world!")
       
        # self.send(bytes_data="Hello world!")
        
        # self.close()
        
        # self.close(code=4123)
        pass
    def disconnect(self, close_code):
        pass

