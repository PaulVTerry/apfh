#a/p forward hedge


AP = 1000000.0
ForwardRate = 1.06

ForwardHedge = AP * ForwardRate

print "test", ForwardHedge


#use code above to check accuracy of code below
#-------------------------------------------------------------------------------
#use code below in CLI

AP = float(input("What are your Account Payables?"))
ForwardRate = input("What is the forward Rate?")

print "Your Forward Hedge for Account Payables is", AP * ForwardRate
