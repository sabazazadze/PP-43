class Car:
    wheels = 4
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

car1 = Car("BMW", "White", 2000)
car2 = Car("Toyota", "Black", 2000)

print(car1.brand, car1.wheels)
print(car2.brand, car2.wheels)
print(car1.wheels)
car2.wheels = 3

print(car2.wheels)
print(Car.wheels)

# car1.wheels = 4, რადგან car1-ს საკუთარი wheels არ აქვს და Python კლასის მნიშვნელობას იღებს
# car2.wheels = 3, რადგან car2.wheels = 3 ხაზმა car2-ში შექმნა საკუთარი ატრიბუტი რომელიც კლასის ატრიბუტს "ფარავს"
# Car.wheels = 4, რადგან კლასის ატრიბუტი არ შეცვლილა, შეიცვალა მხოლოდ car2-ის საკუთარი