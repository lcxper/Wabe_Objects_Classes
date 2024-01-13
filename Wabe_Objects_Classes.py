import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_user_input(cls):
        radius = float(input("Enter the radius of the circle: "))
        return cls(radius)

    def area(self):
        circle_area = math.pi * (self.radius ** 2)
        print(f"Area of the circle: {circle_area:.2f}")

    def perimeter(self):
        circle_perimeter = 2 * math.pi * self.radius
        print(f"Perimeter of the circle: {circle_perimeter:.2f}")


# Loop to ask the user
while True:
    my_circle = Circle.from_user_input()

    my_circle.area()
    my_circle.perimeter()

    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice != 'yes':
        break
