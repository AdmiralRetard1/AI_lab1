import math

# class for node
class Node(object):

    # function to enter layout with checking it for uniqueness and fullness
    def __init__(self, new_layout, old_node=None, level=0):
        self.layout = new_layout
        self.level = level
        # cost to move 1 tile compared to previous layout
        self.wayCost = count_cost(old_node, new_layout) if old_node else level

    # function to print layout
    def __repr__(self):
        r_val = ""
        for i in [0, 3, 6]:
            r_val += "\n" + ("".join(self.layout[i] + self.layout[i + 1] + self.layout[i + 2]))
        return r_val

    # redefined equality function
    def __eq__(self, comp_node):
        return True if self.layout == comp_node.layout else False


# list class expansion to represent nodes
class NodeList(list):

    # magic function to use in "in" clause
    def __contains__(self, key):
        layouts = (o.layout for o in self)
        return key.layout in layouts


# function that return the value of tile in new layout that was moved on empty position
def count_cost(old_node, new_layout):
    return int(new_layout[old_node.layout.index(" ")]) + old_node.wayCost


# function to check correctness of input
def input_layout(message):
    while True:
        layout = input(message)
        if (len(layout) != 8) and (len(layout) != 9):
            print("Invalid number of elements! Please enter again")
        else:
            # checking uniqueness
            checked = ""
            legal = True
            for ch in layout:
                if ch not in checked:
                    checked += ch
                else:
                    print("Numbers should not repeat! Try again")
                    legal = False
                    break
            # if everything is ok, check if we have only 8 elements - then the last is empty and we need
            # to fill it with space
            if legal:
                if len(layout) == 8:
                    layout += " "
                break
    return layout


# universal func to print our lists without braces
def printlist(lst):
    lines = ["", "", "", ""]
    res = ""
    if lst:
        nodeCounter = 0
        for n in lst:
            digits = getCountOfDigits(n.wayCost)
            lines[0] += n.layout[:3] + " "*(digits + 1)
            lines[1] += n.layout[3:6] + " "*(digits + 1)
            lines[2] += n.layout[6:] + " "*(digits + 1)
            lines[3] += "w:{}".format(n.wayCost) + " "*2
            nodeCounter += 1
            if nodeCounter == 30:
                res += "\n".join(lines) + "\n\n"
                lines = ["", "", "", ""]
                nodeCounter = 0
        res += "\n".join(lines)
        print(res)
    else:
        print("Empty list")


def getCountOfDigits(number):
    return 1 if number == 1 else round(math.log10(number) + 0.5)
