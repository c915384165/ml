#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygraphviz as pgv

G = pgv.AGraph(directed=True, rankdir="LR")

# 设置层数、每层节点数
network_structure = input("输入神经网络每层节点数，如：[10, 7, 5, 4, 2, 1]\n")
all_nodes = [[f"layer{layer_index}node{node_index}" for node_index in range(layer_nodes_num)] for
             layer_index, layer_nodes_num in enumerate(eval(network_structure))]

# 添加输入层节点
for node_index, node in enumerate(all_nodes[0]):
    G.add_node(node, label="", shape="circle", style="bold", color="#60acfc", pos=f"0,{0.6 * node_index}!")

# 添加输入层文本
G.add_node(f"Input_Layer", shape="none", label=f"Input_Layer({len(all_nodes[0])})",
           pos=f"{0},{(node_index + 1) * 0.6}!")

# 添加中间层、输出层节点
for layer_index, layer in enumerate(all_nodes[1:]):
    color = "#5bc49f" if layer_index == len(all_nodes[1:]) - 1 else "#ff7c7c"

    for node_index, node in enumerate(layer):
        x = 1.5 * (layer_index + 1)
        y = - 0.3 * (len(all_nodes[layer_index + 1]) - len(all_nodes[0])) + 0.6 * node_index
        G.add_node(node, label="", shape="circle", style="bold", color=color, pos=f"{x},{y}!")

    # 添加中间层、输出层文本
    text = f"Output_Layer({len(all_nodes[-1])})" if layer_index == len(all_nodes[1:]) - 1 else f"Layer_{layer_index + 1}({len(layer)})"
    G.add_node(f"Layer_{layer_index + 1})", shape="none", label=text,
               pos=f"{x},{y + 0.4}!")

# 添加线
for layer_index in range(all_nodes.__len__() - 1):
    for start in all_nodes[layer_index]:
        for end in all_nodes[layer_index + 1]:
            G.add_edge(start, end)

# 导出图形
G.layout()
G.draw("神经网络.png")

# 运行代码，输入 [5, 10, 15, 15, 15, 10, 5, 1]
