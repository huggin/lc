class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.cap = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.cap[carType - 1] > 0:
            self.cap[carType - 1] -= 1
            return True
        return False
