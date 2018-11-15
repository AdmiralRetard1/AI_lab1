import math


# class for node
class Node(object):

    # function to enter layout with checking it for uniqueness and fullness
    def __init__(self, new_layout, old_node_layout=None, wayCost=0, level=0):
        self.layout = new_layout
        self.level = level
        # cost to move 1 tile compared to previous layout
        self.wayCost = wayCost if wayCost else level
        self.prev_node_layout = old_node_layout if old_node_layout else None

    # function to print layout
    def __repr__(self):
        r_val = ""
        layout = [chr(n+48) for n in make_list_layout(self.layout)]
        if "0" in layout:
            layout[layout.index("0")] = " "
        else:
            layout = [" "] + layout
        for i in [0, 3, 6]:
            r_val += "\n" + ("".join(layout[i] + layout[i + 1] + layout[i + 2]))
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


def make_list_layout(number):
    return [number // 10**n % 10 for n in range(getCountOfDigits(number)-1, -1, -1)]

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
                    layout += "0"
                else:
                    layout = list(layout)
                    layout[layout.index(" ")] = "0"
                break
    return int("".join(layout))


# universal func to print our lists of nodes without braces
def print_nodes(lst):
    lines = ["", "", "", ""]
    res = ""
    if lst:
        nodeCounter = 0
        for n in lst:
            layout = [chr(n+48) for n in make_list_layout(n.layout)]
            if "0" in layout:
                layout[layout.index("0")] = " "
            else:
                layout = [" "] + layout
            digits = getCountOfDigits(n.wayCost)
            lines[0] += "".join(layout[:3]) + " " * (digits + 1)
            lines[1] += "".join(layout[3:6]) + " " * (digits + 1)
            lines[2] += "".join(layout[6:]) + " " * (digits + 1)
            lines[3] += "w:{}".format(n.wayCost) + " " * 2
            nodeCounter += 1
            if nodeCounter == 30:
                res += "\n".join(lines) + "\n\n"
                lines = ["", "", "", ""]
                nodeCounter = 0
        res += "\n".join(lines)
        print(res)
    else:
        print("Empty list")


# function to print list of repeating nodes
def print_list(lst):
    lines = ["", "", ""]
    res = ""
    if lst:
        nodeCounter = 0
        for n in lst:
            layout = [chr(ch+48) for ch in make_list_layout(n)]
            if "0" in layout:
                layout[layout.index("0")] = " "
            else:
                layout = [" "] + layout
            lines[0] += "".join(layout[:3]) + "  "
            lines[1] += "".join(layout[3:6]) + "  "
            lines[2] += "".join(layout[6:]) + "  "
            nodeCounter += 1
            if nodeCounter == 30:
                res += "\n".join(lines) + "\n\n"
                lines = ["", "", ""]
                nodeCounter = 0
        res += "\n".join(lines)
        print(res)
    else:
        print("Empty list")


def getCountOfDigits(number):
    return 1 if number == 1 or number == 0 else round(math.log10(number) + 0.5)
