import argparse
################################################################################
########## 参数解析部分 #########################################################
################################################################################
# 1. 新建参数解析器对象parser
parser = argparse.ArgumentParser()

# 2. 添加参数
## 2.1 添加位置参数
parser.add_argument('input_list', nargs='+', help='input a list of nodes examples: 1 3 4 2 3')

## 2.2 添加可选参数
parser.add_argument('-o', nargs='?', help='output file name')
parser.add_argument('-g', nargs='?', help='output gv file')
parser.add_argument('-a', nargs='?', help='activate output block')
parser.add_argument('-t', nargs='?', help='begin test mode')
parser.add_argument('-y', nargs='?', help='add a y hat')
parser.add_argument('-x', nargs='?', help='add x_n')

# 3. 解析参数
args = parser.parse_args()

# 4. 测试输出
int_list = [int(x) for x in args.input_list]
if args.y:
    int_list.append(1)

################################################################################
# 画图部分
################################################################################
import pygraphviz as pgv

G = pgv.AGraph(directed=True, rankdir="LR")

# 设置层数、每层节点数
network_structure = int_list
all_nodes = [[f"layer{layer_index}node{node_index}" for node_index in range(layer_nodes_num)]  for layer_index, layer_nodes_num in enumerate(network_structure)]

# 输入替换为 x_n
if args.x:
    # 添加输入层节点
    print("args.x activate")
    for node_index, node in enumerate(all_nodes[0]):
        # print("add ing node"+str(node_index+1))
        # print(type(node_index))
        G.add_node(
            node, 
            label="", 
            image=f"/Users/macpro/ml/C1/W2/x{len(all_nodes[0])-node_index}.png",
            imagescale=True,
            width=0.25,
            fixedsize=True,
            shape="none",
            style="bold", 
            color="#60acfc", 
            pos=f"0,{0.6 * node_index}!"
        )
    # 添加输入层文本
    G.add_node(
        f"Input_Layer", 
        shape="none", 
        label=f"Input_Layer({len(all_nodes[0])})",
        pos=f"{0},{(node_index + 0.5) * 0.6}!"
    )
else:
    print("args.x not active")
    # 添加输入层节点
    for node_index, node in enumerate(all_nodes[0]):
        G.add_node(node, label="", shape="circle", style="bold", color="#60acfc", pos=f"0,{0.6 * node_index}!")

    # 添加输入层文本
    G.add_node(
        f"Input_Layer", 
        shape="none", 
        label=f"Input_Layer({len(all_nodes[0])})",
        pos=f"{0},{(node_index + 1) * 0.6}!"
    )

# 添加中间层、输出层节点
if args.y:
    print("args.y active")
    for layer_index, layer in enumerate(all_nodes[1:]):
        if layer_index == len(all_nodes[1:]) -2 or layer_index == len(all_nodes[1:]) - 1:
            color = "#5bc49f"
        else:
            color = "#ff7c7c"
        # color = "#5bc49f" if layer_index == len(all_nodes[1:]) - 2 or layer_index == len(all_nodes[1:]) - 1 else "#ff7c7c"

        for node_index, node in enumerate(layer):
            x = 1.5 * (layer_index + 1)
            y = - 0.3 * (len(all_nodes[layer_index + 1]) - len(all_nodes[0])) + 0.6 * node_index
            # print(f"add node node_index:{node_index}")
            # print(f"add node node:{node}")
            if layer_index < len(all_nodes[1:]) -1:
                G.add_node(node, label="", shape="circle", style="bold", color=color, pos=f"{x},{y}!")
            else:
                # if layer_index < len(all_nodes[1:]) -1:
                G.add_node(node, 
                    label="", 
                    image=f"/Users/macpro/ml/C1/W2/yhat.png",
                    imagescale=True,
                    width=0.25,
                    fixedsize=True,
                    shape="none",
                    style="bold", 
                    # color=color, 
                    pos=f"{x},{y}!",
                )

        # 添加中间层、输出层文本
        if layer_index == len(all_nodes[1:]) - 2:
            text = f"Output_Layer({len(all_nodes[-1])})"
        elif layer_index == len(all_nodes[1:]) - 1:
            text = f""
        else:
            text = f"Layer_{layer_index + 1}({len(layer)})"


        # text = f"Output_Layer({len(all_nodes[-1])})" if layer_index == len(all_nodes[1:]) - 2 else f"Layer_{layer_index + 1}({len(layer)})"
        G.add_node(f"Layer_{layer_index + 1})", shape="none", label=text,
                   pos=f"{x},{y + 0.4}!")
else:
    print("args.y not activate")
    # 添加中间层、输出层节点
    for layer_index, layer in enumerate(all_nodes[1:]):
        color = "#5bc49f" if layer_index == len(all_nodes[1:]) - 1 else "#ff7c7c"

        for node_index, node in enumerate(layer):
            x = 1.5 * (layer_index + 1)
            y = - 0.3 * (len(all_nodes[layer_index + 1]) - len(all_nodes[0])) + 0.6 * node_index
            G.add_node(
                node, 
                label="", 
                shape="circle", 
                style="bold", 
                color=color, 
                pos=f"{x},{y}!"
            )

        # 添加中间层、输出层文本
        if layer_index == len(all_nodes[1:]) - 1:
            text = f"Output_Layer({len(all_nodes[-1])})"
        else:
            text = f"Layer_{layer_index + 1}({len(layer)})"
        # text = f"Output_Layer({len(all_nodes[-1])})" if layer_index == len(all_nodes[1:]) - 1 else f"Layer_{layer_index + 1}({len(layer)})"
        G.add_node(
            f"Layer_{layer_index + 1})", 
            shape="none", 
            label=text,
            pos=f"{x},{y + 0.4}!"
        )

# 添加线
for layer_index in range(all_nodes.__len__() - 1):
    for start in all_nodes[layer_index]:
        for end in all_nodes[layer_index + 1]:
            G.add_edge(start, end)
if args.t:
    print("test mode activate")
    # print(all_nodes[0])

    layer0_nodes = network_structure[0]
    # for i in range(layer0_nodes):
        # print(i)
else:
    pass
# 导出图形
if args.a:
    G.layout()
    if not args.o:
        G.draw("神经网络.png")
        print("神经网络.png had exported")
    else:
        G.draw(str(args.o))
        print(f"{args.o} had exported")

    if args.g:
        with open(args.g,"w") as file:
            file.write(str(G))
        print(f"gv file {args.g} had exported")

else:
    print("output not activate")