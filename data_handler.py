import data
import util


def get_boards():
    return data.get_data("boards")


def get_statuses():
    return data.get_data("statuses")


def get_cards(board_id):
    return data.get_row("cards", board_id, "board_id")


def create_board(title, user_id):
    data_dictionary = {"title": title, "user_id": user_id}
    return data.add_new_row(data_dictionary, "boards")


def rename_board(board_id, new_name):
    return data.update_board(board_id, new_name)


def rename_column(id, new_name):
    return data.update_column(id, new_name)


def rename_card(id, new_name):
    return data.update_card(id, new_name)


def create_new_card(card_name, board_id, status_id):
    card_data = {"title": card_name, "board_id": board_id, "status_id": status_id, "order_n": 0}
    return data.add_new_row(card_data, 'cards')


def add_new_status(new_status):
    return data.add_new_row(new_status, "statuses")


def update_card_status(card_data):
    return data.update_card_status(card_data['card_id'], card_data['status_id'])


def update_card_order(card_data):
    for card in card_data:
        data.update_card_order(card['card_id'], card['order_n'])
        
        
def check_user_data(username):
    return data.get_row("users", username, "username")


def add_new_user(username, password):
    hashed_password = util.hash_password(password)
    return data.add_new_row({"username": username, "hashed_password": hashed_password}, "users")
