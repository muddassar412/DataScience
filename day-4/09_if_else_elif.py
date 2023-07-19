min_age_at_school = 5
hammad_age = input("how old is hammad? ")
hammad_age =int(hammad_age)
# question: can hammad go to school?
if (hammad_age == min_age_at_school):
    print ("yes, he can go to school")  #indent block


elif(hammad_age>=6):
    print("he must go to higher school")

elif(hammad_age<=2):
    print("no one should be allowed in his age group!")
else:
    print("No, he can't go to school")    