name = 'Zed A. Shaw'
age = 35 # not a lie
height = (74 * 2.54) # cms
weight = (180 * 2.2) # kgs
eyes = 'Blue'
teeth = 'White'
hair = "This and 'this'"

print "Let's talk about %s." % name
print "He's %F cms tall." % height
print "He's %i kgs heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %r hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth


print "If I add %r, %d, and %d I get %i." % (age, height, weight,
age + height + weight)
