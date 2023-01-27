# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] += pets_sold


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    return [pet for pet in pet_shop["pets"] if pet["breed"] == breed]


def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet


def remove_pet_by_name(pet_shop, name):
    pet = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet)


def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, cash):
    customer["cash"] -= cash


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)


def customer_can_afford_pet(customer, pet):
    return get_customer_cash(customer) >= pet["price"]


def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None:
        pet_name = pet["name"]
        pet_price = pet["price"]

        pet_available = False if find_pet_by_name(pet_shop, pet_name) == None else True
        can_afford = customer_can_afford_pet(customer, pet)

        if pet_available and can_afford:
            remove_customer_cash(customer, pet_price)
            add_or_remove_cash(pet_shop, pet_price)
            remove_pet_by_name(pet_shop, pet_name)
            add_pet_to_customer(customer, pet)
            pet_shop["admin"]["pets_sold"] += 1
