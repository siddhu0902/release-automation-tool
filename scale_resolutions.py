#Scale_resolution
def scale_resolution(resolution, factor):
    result = []
    for x in resolution:
        result.append(tuple(y * factor for y in x))
    return result

resolution = int(input("Enter the resolution: "))
factor = int(input("enter the factor value: "))
scale_resolution(resolution,factor)