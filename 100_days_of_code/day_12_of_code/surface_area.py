############SURFACE AREA
pi= float(input("pi is ", ))
rad= int(input("radius is ", ))
height= int(input("height is ", ))

#surface area of closed cylinder
closed_area= 2 * (pi * rad * rad) + (pi * (rad + rad) *height)
print("Surface area of closed cylinder is ", closed_area)

#surface area for open cylinder
open_area= (pi * rad * rad) + (pi * (rad + rad) *height)
print("Surface area of open cylinder is ", open_area)

#surface area of pipe
pipe_area= (pi * (rad + rad) *height)
print("Surface area of pipe is ", pipe_area)