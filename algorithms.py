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


# func with our algorithm (depth walkthrough)
def find_solution_depth(start, target):
    # NodeList - custom expansion of list class
    nodes_to_expand = node.NodeList()  # border state
    solution = node.NodeList()  # current solution state
    bad_nodes = node.NodeList()  # repeating nodes
    nodes_to_expand.append(start)
    counter = 0 # loop counter
    no_solution = False
    solved = False
    step_by_step = True

    # possible ways to move tile depending on its position
    pos_ways = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4, 6], 4: [1, 3, 5, 7],
                5: [2, 4, 8], 6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}

    # start solving
    while not solved and not no_solution:

        good_node = False

        # print the menu if we are in step-by-step mode (default is yes)
        if step_by_step:
            pressed_key = menu()
            if pressed_key == "2":
                start_time = time.time()
                step_by_step = False

        # get next node
        while not good_node:
            if nodes_to_expand:
                next_node = nodes_to_expand.pop()
            else:
                no_solution = True
                break
            if next_node.level != 100:
                good_node = True
            else:
                bad_nodes.append(next_node)

        if not no_solution:
            solution.append(next_node)
            temp = list()

            # determine empty tile position
            pos = next_node.layout.index(" ")

            # append new nodes to tree
            for i in pos_ways[pos]:
                new_layout = list(next_node.layout)

                # move tile
                new_layout[i], new_layout[pos] = new_layout[pos], new_layout[i]

                # depending on the chosen way to solve, choose constructor for node
                new_node = node.Node("".join(ch for ch in new_layout), level=next_node.level + 1)

                # checking newly created node
                if new_node in solution:  # if we already have this node
                    if new_node not in bad_nodes:                  # we append it to the list of bad nodes (repeating)
                        bad_nodes.append(new_node)             # to avoid looping

                # looks like node is good for us, so we add it to the temporary result
                elif new_node not in nodes_to_expand and new_node not in bad_nodes:
                    temp.append(new_node)

            if temp:  # if we found some new nodes
                 # first of all, simply add new nodes to the stack
                for n in temp:
                    if n == target:
                        solution.append(n)
                        solved = True
                        break
                    else:
                        nodes_to_expand.append(n)
            else:
                solution.pop()

            # increment loop counter
            counter += 1

            # if we are using step-by-step mode, we need to print this on each step
            if step_by_step:
                print("New nodes to expand:")
                node.printlist(temp)
                print("\nRepeating nodes:")
                node.printlist(bad_nodes)
                print("\nCurrent border state:")
                node.printlist(nodes_to_expand)
                print("\nNext expanding node:")
                tmp_node = nodes_to_expand.pop()
                print(tmp_node)
                nodes_to_expand.append(tmp_node)

    # if solved, print solution
    if solved and not step_by_step:
        print("Solution :")
        node.printlist(solution)

    print("Time of execution: {:.2f}".format(time.time() - start_time), "Generated nodes: ",
              len(solution) + len(nodes_to_expand) + len(bad_nodes), "Loops passed: ", counter)


# func with our algorithm (weight considering)
# both algorythms are pretty similar, but i decided to divide them to be more readable
def find_solution_weight(start, target):
    # NodeList - custom expansion of list class
    nodes_to_expand = node.NodeList()  # border state
    solution = node.NodeList()  # current solution state
    bad_nodes = node.NodeList()  # repeating nodes
    nodes_to_expand.append(start)
    counter = 0 # loop counter
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

            # depending on the chosen way to solve, choose constructor for node
            new_node = node.Node("".join(ch for ch in new_layout), next_node, next_node.level + 1)

            # checking newly created node
            if new_node in solution:  # if we already have this node
                if new_node not in bad_nodes:                  # we append it to the list of bad nodes (repeating)
                    bad_nodes.append(new_node)             # to avoid looping

            # looks like node is good for us, so we add it to the temporary result
            elif new_node not in nodes_to_expand and new_node not in bad_nodes:
                temp.append(new_node)

        # first of all, simply add new nodes to the stack
        for n in temp:
            if n == target:
                solution.append(n)
                solved = True
                break
            else:
                nodes_to_expand.append(n)

        # and if we have chosen the second way to find solution, we need to sort expanding nodes by their wayCost
        nodes_to_expand = sorted(nodes_to_expand, key=lambda x: x.wayCost, reverse=True)

        # increment loop counter
        counter += 1



        # if we are using step-by-step mode, we need to print this on each step
        if step_by_step:
            print("New nodes to expand:")
            node.printlist(temp)
            print("\nRepeating nodes:")
            node.printlist(bad_nodes)
            print("\nCurrent border state:")
            node.printlist(nodes_to_expand)
            print("\nNext expanding node:")
            tmp_node = nodes_to_expand.pop()
            print(tmp_node)
            nodes_to_expand.append(tmp_node)

    # if solved, print solution
    if solved and not step_by_step:
        print("Solution :")
        node.printlist(solution)
        print("Time of execution: {:.2f}".format(time.time() - start_time), "Generated nodes: ",
              len(solution) + len(nodes_to_expand) + len(bad_nodes), "Loops passed: ", counter)
