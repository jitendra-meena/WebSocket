from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json
from channels.layers import get_channel_layer
from channels.consumer import AsyncConsumer,SyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
from channels.db import database_sync_to_async
from .models import ChatModel
from .models import ChatModel


class ChatOneToOneConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        me = self.scope['user'].id
        print("Here",me)
        friend = self.scope['url_route']['kwargs']['id']
        print(friend)
        if int(me) > int(friend):
            self.room_name = f'{me}-{friend}'
        else:
            self.room_name = f'{friend}-{me}'

        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']

        await self.save_message(username, self.room_group_name, message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def save_message(self, username, thread_name, message):
        ChatModel.objects.create(
            sender=username, message=message, thread_name=thread_name)
        
class ChatOneToOneConsumer3(AsyncWebsocketConsumer):
    async def connect(self):
        me = self.scope['user'].id
        print("Here me",me)
        friend = self.scope['url_route']['kwargs']['id']
        print("Dost-",friend)
        print("Web Socket Connection Stebliesd")
        if int(me)>int(friend):
            self.room_name = f'{me}-{friend}'
        else:
            self.room_name = f'{friend}-{me}'
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        
        async def receive(self, text_data=None, bytes_data=None):
                data = json.loads(text_data)
                message = data['message']
                username = data['username']

        await self.save_message(username, self.room_group_name, message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )
        async def chat_message(self,event):
            username = event['username']
            message = event['message']
            await self.send(text_data = json.dumps({
                'message':message,
                'username':username
            }))
        
        async def disconnect(self,code):
            self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            ) 
        @database_sync_to_async
        def save_message(self,username,message,thread_name):
            ChatModel.objects.create(sender=username,message=message,thread_name=thread_name)
                
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


