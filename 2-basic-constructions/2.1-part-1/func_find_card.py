def hide_card(card_number):
    card_number = card_number.replace(" ", "")
    card_number = '*'*12 + card_number[12:]
    return card_number