class Fish:

    def init(self, name: str, price_in_uah_per_kilo: float, origin: str, weight: float):
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.origin = origin
        self.weight = weight

     def str(self):
        return self.name + " " + str(self.weight) + " " + str(self.price_in_uah_per_kilo) + " " + self.origin


class FishShop:
    def init(self, shop_name: str):
        self.shop_name = shop_name
        self.fish_set = set()

    def add_fish(self, fish_name: str):
        self.fish_set.add(fish_name)

    def get_fish_names_sorted_by_price(self):
        sorted_fishes = sorted(list(self.fish_set), key=lambda fish: fish.price_in_uah_per_kilo)
        return [fish.name for fish in sorted_fishes]

    def sell_fish(self, fish_name: str):
        self.fish_set.remove(fish_name)


