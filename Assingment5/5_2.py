def cutting_choco(cuts) :
    vertical_cuts = round(cuts/2)
    horizantal_cuts = cuts - vertical_cuts
    sum = 0
    for i in range(horizantal_cuts) :
      sum += vertical_cuts
    print(f"maximum pieces : {sum}")
test_cases = int(input("enter number of test case : "))
for _ in range (test_cases) :
    cuts = int(input("enter number of cuts : "))
    cutting_choco(cuts)