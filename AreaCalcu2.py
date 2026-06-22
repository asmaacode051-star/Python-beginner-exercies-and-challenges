str_length = input ("Please type Length :\n")
str_width = input ("Please type width:\n")
str_meter = input ("how much for 1 meter ?:\n")


length = float (str_length)
width = float (str_width)
meter = float (str_meter)

area = length * width
price = area * meter

str_area = str(area)
str_price = str(price)

print ("The total area is:" + str_area)
print ("Give the guy : " + str_price)