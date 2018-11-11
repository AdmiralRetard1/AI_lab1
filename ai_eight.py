import node
import algorithms

start_layout = node.input_layout("Enter starting layout: ")
target_layout = node.input_layout("Enter target layout: ")
start_node = node.Node(start_layout)
target_node = node.Node(target_layout, level=10000)
# starting menu, defines the way to find solution
print("\nChoose algorithm:")
print("1 - Depth walkthrough")
print("2 - Consider the way cost")
if input() == "1":
    algorithms.find_solution_depth(start_node, target_node)
else:
    algorithms.find_solution_weigth(start_node, target_node)
