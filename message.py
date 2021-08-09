def reply(msg):
    if msg.content.lower() == "hi":
        response = f"Hello {msg.author}"

    elif msg.content.lower() == "1":
        pass

    else:
        response = "I don't understand"

    return response