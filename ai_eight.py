import time
import node


# menu output
def menu():
    print("\nChoose what to do next:")
    print("1 - Next step of algorithm")
    print("2 - Continue calculating to the end")
    nice = False
    while not nice:
        pressed_key = input()
        if pressed_key != "1" and pressed_key != "2":
            print("invalid option, try again!")
        else:
            nice = True
    return pressed_key


# universal func to print our lists without braces
def printlist(lst):
    if lst:
        for n in lst:
            print(n)
    else:
        print("Empty list")


# func with our algorithm
def find_solution(start, target):

    # NodeList - custom expansion of list class
    nodes_to_expand = node.NodeList()
    solution = node.NodeList()
    bad_nodes = node.NodeList()
    nodes_to_expand.append(start)
    solved = False
    step_by_step = True

    # start solving
    while not solved:

        # print the menu if we are in step-by-step mode (default is yes)
        if step_by_step:
            pressed_key = menu()
            if pressed_key == "2":
                start_time = time.time()
                step_by_step = False

        # get next node
        next_node = nodes_to_expand.pop()
        solution.append(next_node)
        temp = list()

        # possible ways to move tile depending on its position
        pos_ways = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4, 6], 4: [1, 3, 5, 7],
                    5: [2, 4, 8], 6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}

        # determine empty tile position
        pos = next_node.layout.index(" ")

        # append new nodes to tree
        for i in pos_ways[pos]:
            new_layout = list(next_node.layout)

            # move tile
            new_layout[i], new_layout[pos] = new_layout[pos], new_layout[i]
            new_node = node.Node("".join(ch for ch in new_layout), next_node.layout, next_node.level + 1)

            # checking newly created node
            if new_node in solution:  # if we already have this node
                if new_node not in bad_nodes:                  # we append it to the list of bad nodes (repeating)
                    bad_nodes.append(new_node)             # to avoid looping

            # looks like node is good for us, so we add it to the temporary result
            elif new_node not in nodes_to_expand and new_node not in bad_nodes:
                temp.append(new_node)

        # then we sort the result, so appropriate nodes with lesser wayCost will be expanded first
        temp = sorted(temp, key=lambda x: x.wayCost, reverse=True)

        # append new nodes to the stack
        for n in temp:
            nodes_to_expand.append(n)

        # check if we found a solution
        for n in nodes_to_expand:
            if n == target:
                solution.append(n)
                solved = True
                break

        # if we are using step-by-step mode, we need to print this on each step
        if step_by_step:
            print("New nodes to expand:")
            printlist(temp)
            print("\nRepeating nodes:")
            printlist(bad_nodes)
            print("\nCurrent border state:")
            printlist(nodes_to_expand)
            print("\nNext expanding node:")
            tmp_node = nodes_to_expand.pop()
            print(tmp_node)
            nodes_to_expand.append(tmp_node)

    # if solved, print solution
    if solved:
        print("Solution :")
        for n in solution:
            print(n)
        print("Time of execution: ", time.time() - start_time, "Generated nodes: ",
              len(solution) + len(nodes_to_expand) + len(bad_nodes))


start_layout = node.input_layout("Enter starting layout: ")
target_layout = node.input_layout("Enter target layout: ")
start_node = node.Node(start_layout)
target_node = node.Node(target_layout, level=10000)
find_solution(start_node, target_node)
