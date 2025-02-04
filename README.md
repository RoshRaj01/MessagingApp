Create Virtual Environment

python.exe -m venv env | Windows
python3 -m venv env | MAC & Linux
---------------------------------

Activate Virtual Environment

.\env\Scripts\activate | Windows
source env/bin/activate | MAC & Linux
pip install flask
---------------------------------

Running the application:

python Chat.py
---------------------------------

Testing the endpoints:

POST: http://127.0.0.1:5000/register
{
  "name": "Mathews",
  "email": "mathews.doe@example.com",
  "password": "12password"
}

Returns:
{
    "message": "User registered successfully",
    "user_id": "2"
}
---------------------------------

POST: http://127.0.0.1:5000/login
{
"email": "john.doe@example.com",
"password": "password123"
}

Returns:
{
    "message": "Login successful",
    "user_id": "1"
}
---------------------------------

GET: http://127.0.0.1:5000/users/2

Returns:
{
    "email": "mathews.doe@example.com",
    "name": "Mathews",
    "password": "12password"
}
---------------------------------

PUT: http://127.0.0.1:5000/users/2
{
  "name": "Mathews",
  "email": "mathews.plathottam@example.com",
  "password": "1234password"
}

Returns:
{
    "message": "User updated successfully"
}
---------------------------------
DELETE: http://127.0.0.1:5000/users/2

Returns:
{
    "message": "User deleted successfully"
}
---------------------------------
PUT: http://127.0.0.1:5000/messages
{
  "sender_id": "1",
  "chat_id": "1",
  "content": "Hello, how are you?"
}

Returns:
{
    "message": "Message sent successfully",
    "message_id": "1"
}
---------------------------------
GET: http://127.0.0.1:5000/messages/1

Returns:
{
    "chat_id": "1",
    "content": "Hello, how are you?",
    "sender_id": "1"
}
---------------------------------
GET: http://127.0.0.1:5000/chats/1/messages

Returns:
[
    {
        "chat_id": "1",
        "content": "Hello, how are you?",
        "sender_id": "1"
    }
]
---------------------------------
PUT: http://127.0.0.1:5000/messages/1
{
  "sender_id": "1",
  "chat_id": "1",
  "content": "Hi, where are you?"
}

Returns:
{
    "message": "Message updated successfully"
}
---------------------------------
DELETE: http://127.0.0.1:5000/messages/1

Returns:
{
    "message": "Message deleted successfully"
}
---------------------------------
GET: http://127.0.0.1:5000/users/1/messages

Returns:
[
    {
        "chat_id": "1",
        "content": "Hello, how are you?",
        "sender_id": "1"
    },
    {
        "chat_id": "1",
        "content": "Hello, how are you?",
        "sender_id": "1"
    }
]
---------------------------------
POST: http://127.0.0.1:5000/messages/2/react
{
  "reaction": "👍"
}


Returns:
{
    "message": "Reaction added successfully"
}
---------------------------------
POST: http://127.0.0.1:5000/chats
{
  "name": "Chat 2",
  "users": ["1", "3"]
}

Returns:
{
    "chat_id": "2",
    "message": "Chat created successfully"
}
---------------------------------
GET: http://127.0.0.1:5000/chats

Returns:
{
    "1": {
        "name": "Chat 1",
        "users": [
            "1",
            "2"
        ]
    },
    "2": {
        "name": "Chat 2",
        "users": [
            "1",
            "3"
        ]
    }
}
---------------------------------
GET: http://127.0.0.1:5000/chats/1

Returns:
{
    "name": "Chat 1",
    "users": [
        "1",
        "2"
    ]
}
---------------------------------
DELETE: http://127.0.0.1:5000/chats/2

Returns:
{
    "message": "Chat deleted successfully"
}
---------------------------------
PUT: http://127.0.0.1:5000/chats/1
{
  "name": "Chat 10",
  "users": ["1", "2"]
}

Returns:
{
    "message": "Chat renamed successfully"
}
---------------------------------
POST: http://127.0.0.1:5000/chats/1/add_user
{
  "user_id": "2"
}

Returns:
{
    "message": "User added to chat successfully"
}
---------------------------------
POST: http://127.0.0.1:5000/groups
{
  "name": "Study Group",
  "users": ["1", "2", "3"]
}

Returns:
{
    "group_id": "2",
    "message": "Group created successfully"
}
---------------------------------
GET: http://127.0.0.1:5000/groups

Returns:
{
    "1": {
        "name": "Study Group",
        "users": [
            "1",
            "2",
            "3"
        ]
    },
    "2": {
        "name": "Fun Group",
        "users": [
            "1",
            "2",
            "3"
        ]
    }
}
---------------------------------
GET: http://127.0.0.1:5000/groups/2

Returns:
{
    "name": "Fun Group",
    "users": [
        "1",
        "2",
        "3"
    ]
}
---------------------------------
POST: http://127.0.0.1:5000/groups/2/add_user
{
  "user_id": "4"
}

Returns:
{
    "message": "User added to group successfully"
}
---------------------------------
DELETE: http://127.0.0.1:5000/groups/2/remove_user
{
  "user_id": "4"
}

Returns:
{
    "message": "User removed from group successfully"
}
---------------------------------
POST: http://127.0.0.1:5000/notifications
{
  "message": "You have a new message from User 2",
  "read": true
}

Returns:
{
    "message": "Notification added successfully",
    "notification_id": "3"
}
---------------------------------
GET: http://127.0.0.1:5000/notifications

Returns:
{
    "1": {
        "message": "You have a new message from User 2",
        "read": false
    },
    "2": {
        "message": "You have a new message from User 2",
        "read": false
    },
    "3": {
        "message": "You have a new message from User 2",
        "read": true
    }
}
---------------------------------
PUT: http://127.0.0.1:5000/notifications/mark_read

Returns:
{
    "message": "All notifications marked as read"
}
---------------------------------