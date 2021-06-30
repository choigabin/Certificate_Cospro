def func_a():
    num = 1
    num = num + ga
    print('func_a', id(ga))

ga = 10
#내 메모리 안에서의 나의 참조값이므로 개인마다 다름
print('ga : ', id(ga))
func_a()
print('ga : ', id(ga))

def func_b():
	num = 1
	ga = 20
	print('func_a : ', ga)

ga = 10
print('ga : ', ga)
func_b()
print('ga : ', ga)

def func_c():
    global ga
    ga = 20
    print('func_a : ', ga)

ga = 10
print('ga : ', ga)
func_c()
print('ga : ', ga)