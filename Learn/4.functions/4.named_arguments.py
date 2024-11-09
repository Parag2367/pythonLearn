def marks(maths, chem, eng, phy):
    total = maths + chem + eng + phy
    per = total / 5
    print(total)
    print(f"Percentage is {per:2f}")


# we need to pass argument in a sequence which matches function defination
marks(44, 55, 66, 77)

# another way: named argument(in this you dont have to remeber the sequence)
marks(maths=44, phy=33, chem=44, eng=88)

marks(99, chem=98, eng=66, phy=89)
