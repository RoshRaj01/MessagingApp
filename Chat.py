from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load data from JSON file
def load_data():
    try:
        with open('chat.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"users": {}, "chats": {}, "messages": {}, "groups": {}, "notifications": {}}

data = load_data()

# Save data to JSON file
def save_data():
    with open('chat.json', 'w') as file:
        json.dump(data, file, indent=4)

### 1. USER REGISTRATION ###
@app.route('/register', methods=['POST'])
def register():
    """Registers a new user and assigns a unique user ID."""
    new_id = str(len(data['users']) + 1)
    data['users'][new_id] = request.json
    save_data()
    return jsonify({"user_id": new_id, "message": "User registered successfully"})

### 2. USER LOGIN ###
@app.route('/login', methods=['POST'])
def login():
    """Authenticates a user based on email and password."""
    for user_id, user in data['users'].items():
        if user['email'] == request.json['email'] and user['password'] == request.json['password']:
            return jsonify({"message": "Login successful", "user_id": user_id})
    return jsonify({"error": "Invalid credentials"}), 401

### 3. GET USER DETAILS ###
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Fetches details of a specific user by user ID."""
    return jsonify(data['users'].get(user_id, {"error": "User not found"}))

### 4. UPDATE USER DETAILS ###
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Updates user details if the user exists."""
    if user_id in data['users']:
        data['users'][user_id].update(request.json)
        save_data()
        return jsonify({"message": "User updated successfully"})
    return jsonify({"error": "User not found"}), 404

### 5. DELETE USER ###
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Deletes a user from the system."""
    if user_id in data['users']:
        del data['users'][user_id]
        save_data()
        return jsonify({"message": "User deleted successfully"})
    return jsonify({"error": "User not found"}), 404

### 6. SEND MESSAGE ###
@app.route('/messages', methods=['POST'])
def send_message():
    """Sends a message between users."""
    new_id = str(len(data['messages']) + 1)
    data['messages'][new_id] = request.json
    save_data()
    return jsonify({"message_id": new_id, "message": "Message sent successfully"})

### 7. GET MESSAGE DETAILS ###
@app.route('/messages/<message_id>', methods=['GET'])
def get_message(message_id):
    """Fetches details of a specific message."""
    return jsonify(data['messages'].get(message_id, {"error": "Message not found"}))

### 8. GET ALL MESSAGES IN A CHAT ###
@app.route('/chats/<chat_id>/messages', methods=['GET'])
def get_chat_messages(chat_id):
    """Fetches all messages in a chat."""
    chat_msgs = [msg for msg in data['messages'].values() if msg['chat_id'] == chat_id]
    return jsonify(chat_msgs)

### 9. EDIT MESSAGE ###
@app.route('/messages/<message_id>', methods=['PUT'])
def edit_message(message_id):
    """Edits a message content if it exists."""
    if message_id in data['messages']:
        data['messages'][message_id].update(request.json)
        save_data()
        return jsonify({"message": "Message updated successfully"})
    return jsonify({"error": "Message not found"}), 404

### 10. DELETE MESSAGE ###
@app.route('/messages/<message_id>', methods=['DELETE'])
def delete_message(message_id):
    """Deletes a specific message."""
    if message_id in data['messages']:
        del data['messages'][message_id]
        save_data()
        return jsonify({"message": "Message deleted successfully"})
    return jsonify({"error": "Message not found"}), 404

### 11. GET USER MESSAGES ###
@app.route('/users/<user_id>/messages', methods=['GET'])
def get_user_messages(user_id):
    """Fetches all messages sent by a specific user."""
    user_msgs = [msg for msg in data['messages'].values() if msg['sender_id'] == user_id]
    return jsonify(user_msgs)

### 12. REACT TO MESSAGE ###
@app.route('/messages/<message_id>/react', methods=['POST'])
def react_to_message(message_id):
    """Adds a reaction to a message."""
    if message_id in data['messages']:
        data['messages'][message_id]['reaction'] = request.json['reaction']
        save_data()
        return jsonify({"message": "Reaction added successfully"})
    return jsonify({"error": "Message not found"}), 404

### 13. CREATE CHAT ###
@app.route('/chats', methods=['POST'])
def create_chat():
    """Creates a new chat."""
    new_id = str(len(data['chats']) + 1)
    data['chats'][new_id] = request.json
    save_data()
    return jsonify({"chat_id": new_id, "message": "Chat created successfully"})

### 14. GET ALL CHATS ###
@app.route('/chats', methods=['GET'])
def get_chats():
    """Fetches all chats."""
    return jsonify(data['chats'])

### 15. GET CHAT DETAILS ###
@app.route('/chats/<chat_id>', methods=['GET'])
def get_chat(chat_id):
    """Fetches details of a specific chat."""
    return jsonify(data['chats'].get(chat_id, {"error": "Chat not found"}))

### 16. DELETE CHAT ###
@app.route('/chats/<chat_id>', methods=['DELETE'])
def delete_chat(chat_id):
    """Deletes a specific chat."""
    if chat_id in data['chats']:
        del data['chats'][chat_id]
        save_data()
        return jsonify({"message": "Chat deleted successfully"})
    return jsonify({"error": "Chat not found"}), 404

### 17. RENAME CHAT ###
@app.route('/chats/<chat_id>', methods=['PUT'])
def rename_chat(chat_id):
    """Renames a chat."""
    if chat_id in data['chats']:
        data['chats'][chat_id]['name'] = request.json['name']
        save_data()
        return jsonify({"message": "Chat renamed successfully"})
    return jsonify({"error": "Chat not found"}), 404

### 18. ADD USER TO CHAT ###
@app.route('/chats/<chat_id>/add_user', methods=['POST'])
def add_user_to_chat(chat_id):
    """Adds a user to a chat."""
    if chat_id in data['chats']:
        user_id = request.json['user_id']
        if 'users' not in data['chats'][chat_id]:
            data['chats'][chat_id]['users'] = []
        data['chats'][chat_id]['users'].append(user_id)
        save_data()
        return jsonify({"message": "User added to chat successfully"})
    return jsonify({"error": "Chat not found"}), 404

### 19. CREATE GROUP ###
@app.route('/groups', methods=['POST'])
def create_group():
    """Creates a new group."""
    new_id = str(len(data['groups']) + 1)
    data['groups'][new_id] = request.json
    save_data()
    return jsonify({"group_id": new_id, "message": "Group created successfully"})

### 20. GET ALL GROUPS ###
@app.route('/groups', methods=['GET'])
def get_groups():
    """Fetches all groups."""
    return jsonify(data['groups'])

### 21. GET GROUP DETAILS ###
@app.route('/groups/<group_id>', methods=['GET'])
def get_group(group_id):
    """Fetches details of a specific group."""
    return jsonify(data['groups'].get(group_id, {"error": "Group not found"}))

### 22. ADD USER TO GROUP ###
@app.route('/groups/<group_id>/add_user', methods=['POST'])
def add_user_to_group(group_id):
    """Adds a user to a group."""
    if group_id in data['groups']:
        user_id = request.json['user_id']
        if 'users' not in data['groups'][group_id]:
            data['groups'][group_id]['users'] = []
        data['groups'][group_id]['users'].append(user_id)
        save_data()
        return jsonify({"message": "User added to group successfully"})
    return jsonify({"error": "Group not found"}), 404

### 23. REMOVE USER FROM GROUP ###
@app.route('/groups/<group_id>/remove_user', methods=['DELETE'])
def remove_user_from_group(group_id):
    """Removes a user from a group."""
    if group_id in data['groups']:
        user_id = request.json['user_id']
        if 'users' in data['groups'][group_id] and user_id in data['groups'][group_id]['users']:
            data['groups'][group_id]['users'].remove(user_id)
            save_data()
            return jsonify({"message": "User removed from group successfully"})
    return jsonify({"error": "Group or user not found"}), 404

### 24. ADD NOTIFICATION ###
@app.route('/notifications', methods=['POST'])
def add_notification():
    """Adds a new notification."""
    new_id = str(len(data['notifications']) + 1)
    data['notifications'][new_id] = request.json
    save_data()
    return jsonify({"notification_id": new_id, "message": "Notification added successfully"})

### 25. GET UNREAD NOTIFICATIONS ###
@app.route('/notifications', methods=['GET'])
def get_notifications():
    """Fetches unread notifications."""
    return jsonify(data['notifications'])

### 26. MARK NOTIFICATIONS AS READ ###
@app.route('/notifications/mark_read', methods=['PUT'])
def mark_notifications_as_read():
    """Marks all notifications as read."""
    for notification in data['notifications'].values():
        notification['read'] = True
    save_data()
    return jsonify({"message": "All notifications marked as read"})

if __name__ == '__main__':
    app.run(debug=True)