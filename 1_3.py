num = float(input("enter the length in feet "))
units = [ 'inches' , 'yards' , 'miles' , 'millimeters' , 'centimeters' , 'meters' , 'kilometers']
conversion = [ 12,0.333,0.0001893939,304.8,30.48,0.3048,0.0003048]
print("enter the number according to mentioned above ")
for i in range (0,7) :
    print(f"{i+1} for {units[i]}")
value = int(input("enter your choice "))
con = num * conversion[value - 1] 
print(f" {num} feets is equal to {con} {units[value - 1]}")