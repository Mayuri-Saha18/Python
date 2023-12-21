height=input()
weight=input()

weight_int=int(weight)
height_int=float(height)

bmi=weight_int / height_int ** 2
bmi_int=int(bmi)
print(bmi_int)