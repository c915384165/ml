import argparse

# 1. 新建参数解析器对象parser
parser = argparse.ArgumentParser()

# 2. 添加参数
## 2.1 添加位置参数
parser.add_argument('input_list', nargs='+', help='input a list of nodes')

## 2.2 添加可选参数
parser.add_argument('-o', nargs='?', help='output file name')
parser.add_argument('-a', '--active', help='output file name', action="store_true")
parser.add_argument('-nl', help='output file name', action="store_false")
# parser.add_argument('-na',  action='store_true', help='')
# parser.add_argument('-na', '--not-active', nargs='?', help='output file name')
# parser.add_argument('bar', help='output file name', nargs="?")
#parser.add_argument('-o', nargs='?', help='output file name')
#parser.add_argument('-o', nargs='?', help='output file name')

# 3. 解析参数
args = parser.parse_args()

# 4. 测试输出
int_list = [int(x) for x in args.input_list]
print(int_list)
print(args.o)
# print(args.na)
if args.active:
	print(f"args.active is : {args.active}")
if args.a
	print(f"args.active is : {args.a}")
if not args.nl:
	print(f"args.nl is :{args.nl}")
# if args.na: 	
	# print(f"args.na is :{args.na}")
