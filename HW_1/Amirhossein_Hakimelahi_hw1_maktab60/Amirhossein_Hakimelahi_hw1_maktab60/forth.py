product_list = [
    {
        "type": "1",
        "name": "shirt",
        "price": 30,
        "unit": "Dollar",
        "commission_groups": ["A", "B"]
    },
    {
        "type": "2",
        "name": "pants",
        "price": 50,
        "unit": "Dollar",
        "commission_groups": ["A", "C"]
    },
    {
        "type": "3",
        "name": "shoes",
        "price": 80,
        "unit": "Dollar",
        "commission_groups": ["B"]
    },
    {
        "type": "4",
        "name": "hat",
        "price": 20,
        "unit": "Dollar",
        "commission_groups": []
    }
]

markup_list = [
    {
        "product_type": "1",
        "lower_cost": 10,
        "upper_cost": 20,
        "unit": "percent",
        "lower_count": 10
    },
    {
        "product_type": "2",
        "lower_cost": 15,
        "upper_cost": 20,
        "unit": "percent",
        "lower_count": 10
    },
    {
        "product_type": "3",
        "lower_cost": 10,
        "upper_cost": 15,
        "unit": "percent",
        "lower_count": 5
    },
    {
        "product_type": "4",
        "lower_cost": 10,
        "upper_cost": 30,
        "unit": "percent",
        "lower_count": 20
    },
]

commission_list = [
    {
        "group_name": "A",
        "cost": 5,
        "unit": "percent",
        "users": [1001, 1002, 1003, 1005]
    },
    {
        "group_name": "B",
        "cost": 3,
        "unit": "Dollar",
        "users": [1001, 1003, 1006]
    },
    {
        "group_name": "C",
        "cost": 7,
        "unit": "percent",
        "users": [1001, 1002, 1004]
    }
]

user_list = [
    {
        "userid": 1001,
        "first_name": "Mohsen",
        "last_name": "Bayat",
    },
    {
        "userid": 1002,
        "first_name": "Sobhan",
        "last_name": "Taghadosi",
    },
    {
        "userid": 1003,
        "first_name": "Javad",
        "last_name": "Jafari",
    },
    {
        "userid": 1004,
        "first_name": "Masoud",
        "last_name": "Hosseini",
    },
    {
        "userid": 1005,
        "first_name": "Hassan",
        "last_name": "Zand",
    },
    {
        "userid": 1006,
        "first_name": "Ali",
        "last_name": "Ebadi",
    }
]


def Calculate_markup_percent(type, count):
    d = markup_list[int(type) - 1]
    if count == 1:
        return d.get("upper_cost")
    elif 1 < count < d.get("lower_count"):
        return ((d.get("lower_count") - count) / (d.get("lower_count") - 1)) * (
                d.get("upper_cost") - d.get("lower_cost")) + d.get("lower_cost")
    else:
        return d.get("lower_cost")


def Calculate_product_price(product_type, count, userid=''):
    output = ((Calculate_markup_percent(product_type, count) + 100) / 100) * product_list[int(product_type) - 1].get(
        "price") * count
    if userid == '': return output
    commission_groups = product_list[int(product_type) - 1].get("commission_groups")
    discount, unit = check_user_in_group(userid, commission_groups)
    if unit == "Dollar":
        return output - discount * count
    elif unit == "percent":
        return (100 - discount) * output / 100


def check_user_in_group(id, gpList):
    for d in commission_list:
        if d.get("group_name") in gpList and id in d.get('users'):
            return d.get('cost'), d.get("unit")
    return 0, "Dollar"



