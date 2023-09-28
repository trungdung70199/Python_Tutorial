from enum import Enum
class Color(Enum):
    Red = 'red'
    Green = 'green'
    Blue = 'blue'

color = Color(input("Enter your choice of color: "))
match color:
    case Color.Red:
        print("I see red!")
    case Color.Green:
        print("Grass's color is green")
    case Color.Blue:
        print("I'm feeling the blues :(")
