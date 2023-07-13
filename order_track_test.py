#Павел Кудрявцев, 6-я когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def get_order_track_number():
    track_number = sender_stand_request.post_new_order()
    return track_number.json()["track"]


def test_get_track_order():
    track_number = get_order_track_number()
    get_response = sender_stand_request.get_order_information(track_number)
    assert get_response.status_code == 200
