# ENSF 692 Spring 2025
# May 8 Lab 2
# Exercise 2


# Trace through the execution of the following program. 
# Answer the questions in the comments with your group members.
# After discussing, use print statements to confirm your answers.

foo = 100
bar = foo
foo + bar

print("# point 1")
# POINT 1
print("foo:", foo)
# What is the value of foo at this point? 100
print("foo type:", type(foo))
# What is the type of foo at this point? int
print("bar:", bar)
# What is the value of bar at this point? 100
print("bar type:", type(bar))
# What is the type of bar at this point? int

spam = foo + bar
foo += 50
eggs = foo + bar
ham = [1, 2, 3]
baz = ham
ham.append(bar)

print("# point 2")
# POINT 2
print("foo:", foo)
# What is the value of foo at this point? 150
print("bar:", bar)
# What is the value of bar at this point? 100
print("spam:", spam)
# What is the value of spam at this point? 200
print("eggs:", eggs)
# What is the value of eggs at this point? 250
print("ham:", ham)
# What is the value of ham at this point? [1,2,3,100]
print("baz:", baz)
# What is the value of baz at this point? [1,2,3,100]

eggs = "Python is very flexible!"
spam = ham
ham = bar
bar += bar
foo = eggs
eggs = bar + ham
baz.append(bar)

print("# point 3")
# POINT 3
print("foo:", foo)
print("foo type:", type(foo))
# What is the value of foo at this point? Python is very flexible!
print("bar:", bar)
print("bar type:", type(bar))
# What is the value of bar at this point? 200
print("spam:", spam)
print("spam type:", type(spam))
# What is the value of spam at this point? [1,2,3,100,200]
print("eggs:", eggs)
print("eggs type:", type(eggs))
# What is the value of eggs at this point? 300
print("ham:", ham)
print("ham type:", type(ham))
# What is the value of ham at this point? 100
print("baz:", baz)
print("baz type:", type(baz))
# What is the value of baz at this point? [1,2,3,100,200]

# Print out the types and final values of each variable.
