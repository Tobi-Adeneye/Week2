class Circle:
    def areaOfAcircle(userInput):
            userInput = input("Enter a Radius: ")
            radius = float(userInput)
            area = round(3.14159*(radius * radius), 2)
            circumference = round(2 * 3.14159 * radius, 2)

            print(f"The area of the circle is {area} and the circumference of the circle is {circumference}")


circle = Circle()
print(circle.areaOfAcircle())
# circle.areaOfAcircle()

