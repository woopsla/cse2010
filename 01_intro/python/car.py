class Car:
    count = 0

    def __init__(self, make):
        self.make = make
        self.odometer = 0
        Car.count += 1

    def drive(self, miles):
        self.odometer += miles

    def __str__(self):
        return (
            "Car{"
            + "make='"
            + self.make
            + "'"
            + ", odometer="
            + str(self.odometer)
            + "}"
        )

    @classmethod
    def get_count(cls):
        return Car.count


if __name__ == "__main__":
    car1 = Car("Ford")
    car1.drive(100)

    print(car1.make)
    print(car1.year)
    print(car1)

    print(Car.count)
    print(car1.count)

    car2 = Car("Toyota")
    print(car1.count)
    print(car2.count)
