import math

def surface_area(r, h):
    surfaceArea = (2*math.pi*r*h) + (2*math.pi*r**2)
    print("The surface area of the cylinder is {:.2f} square feet.\n".format(surfaceArea))

if __name__ == "__main__":
    cont = "yes"
    while(cont == "yes"):
        r = input("\nPlease enter the radius of the base: ")
        r = float(r)
        h = input("Please enter the height of the cylinder: ")
        h = float(h)
        surface_area(r, h)
        cont = input("Would you like to continue using the application? ")