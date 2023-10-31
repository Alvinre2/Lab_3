import price_info


def test_total_cost_shopping():

    price_info.price_list = {'apple': 1.20, 'orange': 1.40}
    price_info.quantity_list = {'apple': 5, 'orange': 5}

    result = price_info.total_cost_shopping()

    assert result == 13


def test_cost_of_fruits():
    price_info.price_list = {'apple': 1}
    price_info.quantity_list = {'apple': 10}

    fruit = 'apple'
    quantity = 10

    result = price_info.cost_of_fruits(fruit, quantity)

    assert result == 10

