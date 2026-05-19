import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapi_project.settings')
import django

django.setup()

from django.contrib.auth.models import User
from django.test import Client

User.objects.filter(username='testuser').delete()
User.objects.create_user('testuser', 'test@example.com', 'testpass')
client = Client()
logged = client.login(username='testuser', password='testpass')
print('login', logged)

payload = json.dumps({'bio': 'hello', 'location': 'test'})
resp = client.post('/api/profiles/', payload, content_type='application/json')
print('status', resp.status_code)
print('body', resp.content.decode())
resp2 = client.get('/api/profiles/')
print('list status', resp2.status_code)
print('list body', resp2.content.decode())
