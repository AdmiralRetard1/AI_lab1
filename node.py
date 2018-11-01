# class for node
class Node(object):

    # function to enter layout with checking it for uniqueness and fullness
    def __init__(self, new_layout, old_layout=0, level=0):
        self.layout = new_layout
        self.level = level
        # cost to move 1 tile compared to previous layout
        self.wayCost = count_cost(old_layout, new_layout) if old_layout != 0 else 0

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
def count_cost(old_layout, new_layout):
    return new_layout[old_layout.index(" ")]


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
