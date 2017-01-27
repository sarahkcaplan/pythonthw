# The variable 'cars' refers to the number '100'
cars = 100

# The variable 'space_in_a_car' refers to the number '4'
space_in_a_car = 4

# The variable 'drivers' refers to the number '30'
drivers = 30

# The variable 'passenders' refers to the number '90'
passengers = 90

# The variable "cars_not_driven" refers to the difference between
# the number the variable 'cars' refers to and the number the variable
# 'drivers' revers to
cars_not_driven = cars - drivers

# The variable "cars_driven" refers to number the variable
# "drivers" refers to
cars_driven = drivers

# The variable "carpool_capacity" refers to the product of "cars_driven"
# and "space_in_a_car". The variable "cars_driven" refers to the variable "drivers"
# and the variable "drivers" refers to the number "30". The
# variable "space_in_a_car" refers to the number "4"
carpool_capacity = cars_driven * space_in_a_car

# The variable "average_passengers_per_car" refers to the divisor
# of the variables "passengers" and "cars_driven".
# "passengers" refers to the number "90" and "cars_driven" refers to
# "drivers", which refers to the number "30".
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# The variable "car_pool_capacity" was not defined. It
# did not mean anything to the program. The program did
# not know what to do with it when it encountered it

# Using a floating point for people isn't necessary because
# people can only come in whole numbers
