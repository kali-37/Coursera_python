# class Recipe():
#     def __new__(cls : type[self_or_any_name]) -> self_or_any_name:
#         pass

#     def __init__(self_or_any_name) -> None:
#         pass

class Recipe():
    def __init__(self_or_any_name, dish, items, time) -> None:
        self_or_any_name.dish = dish
        self_or_any_name.items = items
        self_or_any_name.time = time
# remember no need to enter self here only
    def contents(self_or_any_name):
        print("The " + self_or_any_name.dish + " has " + str(self_or_any_name.items) +
            " and takes " + str(self_or_any_name.time) + " min to prepare")


pizza = Recipe("pizza", ['cheese', 'bread', 'tomato'], 45)
pasta = Recipe("pasta", ['penne', 'sauce'], 55)
print(pizza.items)
print(pasta.time)
print(pizza.contents())
