from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from channels.layers import get_channel_layer
from channels.consumer import AsyncConsumer,SyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("Websocket Connected....",event)
        await self.send({'type':'websocket.accept'})
    async def websocket_receive(self,event):
        print("Websocket Received....",event)
        print(event['text'])
        l1 = ["Jitendra","Meena","Software Developer","Indore","Hii","Jitendra","How Are You","Hope you doing Well","Good By Jitendra"]

        for i in l1:
            
            await self.send({
            'type':'websocket.send',
            'text':str(i)
            
                })
        await asyncio.sleep(1)    
    async def websocket_disconnect(self,event):
        print("Websocket Disconnected....",event)  
        raise StopConsumer()  



class ChatSyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("Websocket Connected....",event)
        print("Channel Layer",self.channel_layer)
        async_to_sync(self.channel_layer.group_add)('programmer',self.channel_name)
        self.send({'type':'websocket.accept'})
        print("Channel name",self.channel_name)
    def websocket_receive(self,event):
        print("Websocket Received....",event['text'])
        l1 = ["Jitendra","Meena","Software Developer","Indore","Hii","Jitendra","How Are You","Hope you Doing Well","Good By Jitendra"]
        for i in l1:
            print(i)
            self.send({
            'type':'websocket.send',
            'text':str(i)
            
            })
            print("It's Working Bro.")
            sleep(1)
    def websocket_disconnect(self,event):
        print("Websocket Disconnected....",event)
        raise StopConsumer()

# class TestConsumer(WebsocketConsumer):
  
#     def connect(self):
#         self.room_name="test_consumer"
#         self.room_group_name="test_consumer_group"
#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_add)(self.room_name,self.room_group_name)
#         self.accept()
#         # self.send(test_data=json.dumps({'status':'connected'}))  
        
        

       
    
#     def receive(self, text_data=None, bytes_data=None):
#         # self.send(text_data="Hello world!")
       
#         # self.send(bytes_data="Hello world!")
        
#         # self.close()
        
#         # self.close(code=4123)
#         pass
#     def disconnect(self, close_code):
#         pass

