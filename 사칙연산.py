print("과제명 : 사칙연산")
print("날짜 : 2024. 5 .29")
name = input("작성자의 학번 이름을 입력하시오\t")
print("\n")
print("작성자 : {}".format(name))
print("\n")
print("*" * 50)
print("\n")
num_1 = float(input("첫번째 수를 입력하시오\t"))
num_2 = float(input("두번째 수를 입력하시오\t"))
math = input("연산기호(+,-,*,/)중 1개를 입력하시오\t")
print("\n")
print("*** 계산 결과 ***")
print("\n")
if math == "+" :
    math_A = num_1 + num_2
    print("%d" %(math_A))
elif math == "-" :
    math_A = num_1 - num_2
    print("%d" %(math_A))
elif math == "*" :
    math_A = num_1 * num_2
    print("%d" %(math_A))
elif math == "/" :
    math_A = num_1 / num_2
    print("%d" %(math_A)
print("\n")
print("*" * 50)
