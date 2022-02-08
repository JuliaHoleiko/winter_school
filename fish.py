class FishInfo:

    def init(self, name: str, price_in_uah_per_kilo: float,due_date = datetime, origin: str, catch_date: datetime):
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.due_date = due_date
        self.origin = origin
        self.catch_date = catch_date


     def str(self):
        return self.name + " " + str(self.weight) + " " + str(self.price_in_uah_per_kilo) + " " + self.origin

class Fish (FishInfo):
    def init (self, age_in_month : int, weight: float,name: str, price_in_uah_per_kilo: float,due_date = datetime, origin: str, catch_date: datetime):
        super().init(name, origin, catch_date)
        self.age_in_month = age_in_month
        self.weight = weight

class FishBox():
    def __init__(self, fish_info: FishInfo, weight: float, package_date: datetime, height: float, width: float,
                 lenght: float, is_alive: bool):
        self.fish_info = fish_info
        self.weight = weight
        self.package_date = package_date
        self.height = height
        self.width = width
        self.length = length
        self.is_alive = is_alive

class FishShop:
    def init(self):
        self.frozen_fish_boxes = {}
        self.fresh_fish_boxes = {}

    def add_fish(self):
        pass

    def get_fresh_fish_sorted_by_price(self):
       pass

    def get_frozen_fish_sorted_by_price(self):
       pass
    def sell_fish(self, fish_name: str):
      pass
    def add_fish_in_box(self):
        pass




