# --------------------------------------------------
# import turtle as t
# tim = t.Turtle()
# screen = t.Screen()
#
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# screen.exitonclick
# import random
# ------------------------------------------

# Drawing shapes

# import turtle as t
# import random
#
# colours = ["Blue", "Yellow", "Green", "Black", "White", "Red"]
#
# tim = t.Turtle()
#
# scr = t.Screen()
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)
#
# scr.exitonclick()
# -----------------------------------------------------------------------

# Random walk

# import random
# import turtle as t
#
# tim = t.Turtle()
# tim.pensize(5)
# directions = [0, 90, 180, 270]
# turtle_colors = [
#     "white",
#     "black",
#     "red",
#     "green",
#     "blue",
#     "cyan",
#     "magenta",
#     "yellow",
#     "orange",
#     "purple",
#     "brown",
#     "gray",
#     "pink",
#     "lightblue",
#     "sienna",
#     "salmon",
#     "olive",
#     "navy",
#     "maroon",
#     "khaki",
#     "indigo",
#     "gold",
#     "fuchsia",
#     "coral",
#     "chartreuse",
#     "aquamarine",
#     "violet",
#     "tomato",
#     "teal",
#     "tan",
#     "seashell",
#     "peru",
#     "orchid",
#     "lime",
#     "ivory",
# ]
# scr = t.Screen()
# tim.speed("fastest")
# t.colormode(255)
#
# def walk_a_step():
#     tim.setheading(random.choice(directions))
#     tim.forward(20)
#
#
# def random_color():
#     r = random.randint(0 ,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# for _ in range (0, 200):
#     tim.color(random_color())
#     walk_a_step()
# scr.exitonclick()

# -----------------------------------------------------

# Tuples
# my_tuple = (1, 2, 3)
# tuples cannot be changed, it is immutable
# list(my_tuple) transforms a tuple into a list

# ---------------------------------------------------------

# Spirograph

# import turtle as t
# import random
# tim = t.Turtle()
# scr = t.Screen()
# t.colormode(255)
# angle = 0
# tim.speed("fastest")
#
#
# def random_color():
#     r = random.randint(0 ,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# def draw_spirograph(gap):
#     for _ in range(0, int(360/gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + gap)
#
#
# draw_spirograph(1)
# scr.exitonclick()

# --------------------------------------------------

