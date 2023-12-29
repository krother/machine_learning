
input1 = float(input("enter first input  : "))
input2 = float(input("enter second input : "))

w1 = [____, ____]
bias1 = ____
dot1 = input1 * w1[0] + input2 * w1[1] + bias1
out1 = 1.0 if dot1 > 0.5 else 0.0

w2 = [____, ____]
bias2 = ____
dot2 = input1 * w2[0] + input2 * w2[1] + bias2
out2 = 1.0 if dot2 > 0.5 else 0.0

w3 = [___, ____]
bias3 = ____
dot3 = out1 * w3[0] + out2 * w3[1] + bias3
out3 = 1.0 if dot3 > 0.5 else 0.0

print(out3)
