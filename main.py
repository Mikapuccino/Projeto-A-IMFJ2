gravity = 9.81
fluid_density = 1
object_density = 0.2
object_volume = 3
object_mass = 1.5
base_spring_length = 0.5
constant = 0.2
problem = 0

buoyancy = fluid_density * gravity * object_volume
fg = object_mass * gravity
submerged_object_volume = fg / (fluid_density * gravity)
floatation_result = submerged_object_volume / (object_volume ** 2)

stretch_force = object_mass * gravity
extension = stretch_force / constant
springs_result = extension + base_spring_length

def menu():

    global problem

    print("What problem do you want to solve?")
    print("1. Floatation")
    print("2. Springs")
    problem = input(">")

def problem1():

    global object_mass
    global object_density
    global object_volume
    global fluid_density
    global gravity
    global floatation_result
    global fg
    global submerged_object_volume

    print("Object properties: Mass=" + str(object_mass) + ", Density=" + str(object_density) + ", Volume=" + str(object_volume))
    print("Fluid has a density of " + str(fluid_density) + ", gravity is " + str(gravity))
    print("Object would float at " + str(floatation_result) + " meters")
    option = input(">")
    option = option.split()

    if (option[0] == "set" and option[1] == "mass"):

        object_mass = option[2]
        fg = float(object_mass) * int(gravity)
        submerged_object_volume = fg / (int(fluid_density) * int(gravity))
        floatation_result = submerged_object_volume / (int(object_volume) ** 2)
        problem1()

    elif (option[0] == "set" and option[1] == "density"):

        object_density = option[2]
        fg = float(object_mass) * int(gravity)
        submerged_object_volume = fg / (int(fluid_density) * int(gravity))
        floatation_result = submerged_object_volume / (int(object_volume) ** 2)
        problem1()

    elif (option[0] == "set" and option[1] == "volume"):

        object_volume = option[2]
        fg = float(object_mass) * int(gravity)
        submerged_object_volume = fg / (int(fluid_density) * int(gravity))
        floatation_result = submerged_object_volume / (int(object_volume) ** 2)
        problem1()

    elif (option[0] == "set" and option[1] == "fluid" and option[2] == "density"):

        fluid_density = option[3]
        fg = float(object_mass) * int(gravity)
        submerged_object_volume = fg / (int(fluid_density) * int(gravity))
        floatation_result = submerged_object_volume / (int(object_volume) ** 2)
        problem1()

    elif (option[0] == "set" and option[1] == "gravity"):

        gravity = option[2]
        fg = float(object_mass) * int(gravity)
        submerged_object_volume = fg / (int(fluid_density) * int(gravity))
        floatation_result = submerged_object_volume / (int(object_volume) ** 2)
        problem1()

    elif (option[0] == "exit"):

        menu()

    else:

        print("Try something else.")
        problem1()

def problem2():

    global object_mass
    global gravity
    global base_spring_length
    global constant
    global springs_result

    print("Object mass is " + str(object_mass) + ", gravity is " + str(gravity))
    print("Base spring length is " + str(base_spring_length) + ", constant = " + str(constant))
    print("Spring would stretch " + str(springs_result) + " meters")
    option = input(">")
    option = option.split()

    if (option[0] == "set" and option[1] == "mass"):

        object_mass = option[2]
        stretch_force = float(object_mass) * float(gravity)
        extension = stretch_force / float(constant)
        springs_result = extension + int(base_spring_length)
        problem2()

    elif (option[0] == "set" and option[1] == "gravity"):

        gravity = option[2]
        stretch_force = float(object_mass) * float(gravity)
        extension = stretch_force / float(constant)
        springs_result = extension + int(base_spring_length)
        problem2()

    elif (option[0] == "set" and option[1] == "length"):

        base_spring_length = option[2]
        stretch_force = float(object_mass) * float(gravity)
        extension = stretch_force / float(constant)
        springs_result = extension + int(base_spring_length)
        problem2()

    elif (option[0] == "set" and option[1] == "constant"):

        constant = option[2]
        stretch_force = float(object_mass) * float(gravity)
        extension = stretch_force / float(constant)
        springs_result = extension + int(base_spring_length)
        problem2()

    elif (option[0] == "exit"):

        menu()

    else:

        print("Try something else.")
        problem2()



menu()

if (int(problem) == 1):

    problem1()

elif (int(problem) == 2):

    problem2()

else:

    print("Try something else.")