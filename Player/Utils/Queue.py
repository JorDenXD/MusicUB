"""
Telegram @Itz_Your_4Bhi
Copyright ©️ 2025
"""


QUEUE = {}


def add_to_queue(chat_id, title, duration, songlink, link):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.append([chat_id, title, duration, songlink, link])
        return int(len(chat_queue) - 1)
    else:
        QUEUE[chat_id] = [[chat_id, title, duration, songlink, link]]


def get_queue(chat_id):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        return chat_queue
    else:
        return 0


def pop_an_item(chat_id):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.pop(0)
        return 1
    else:
        return 0


def clear_queue(chat_id):
    if chat_id in QUEUE:
        QUEUE.pop(chat_id)
        return 1
    else:
        return 0
