Amount =int(input("Please Enter Amount for Withdraw :"))\

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print( "note of 100 taka" , note_1)
print("note of 50 taka" , note_2)
print("note of 10 taka" , note_3)