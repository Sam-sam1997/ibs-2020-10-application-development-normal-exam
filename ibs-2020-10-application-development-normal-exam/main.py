from fish import Fish


class types_of_fish:

    First_type = Fish('Clownfish', '3', 'stripes')
    print("The name is " + First_type.name)
    print("The weight is " + First_type.weight + "kg")
    print("The color is " + First_type.color)

    Second_type = Fish('Tang', '2', 'yellow')
    print("The name is " + Second_type.name)
    print("The weight is " + Second_type.weight + "kg")
    print("The color is " + Second_type.color)

    Third_type = Fish( 'Kong', '1', 'red')
    print("The name is " + Third_type.name)
    print("The weight is " + Third_type.weight + "kg")
    print("The color is " + Third_type.color)
