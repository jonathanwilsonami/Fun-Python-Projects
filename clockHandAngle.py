h = input("Enter hour: ")
m = input("Enter min as an integer (do not prefix with zeros): ")

def get_angle(m, h):
    """This function returns the angle between the minute hand and hour hand given a time
    input:
    h - Hour an integer 
    m - minute an integer
    return:
    an angle in degrees
    Algorithm:
    I consider two one for min and the other for hour and get the diff of 
    the angle that is between them. The resulting number is a ratio of a 360 degree circle
    which I then multiply by 360 to get the angle in degrees. 
    """
    h = int(h)
    m = int(m)
    angle = (abs((12*m)-((h*60)+m))/720)*360
    print(angle)
    #return angle

get_angle(m,h)


#TODO: Create a visual recognition program that can determine the angle between the arms
