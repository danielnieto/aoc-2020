class TreeNode():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def __repr__(self):
        return self.data

def get_raw_rules():
    with open('day7-input', 'r') as file:
        return file.read().splitlines()

def parse_rules(raw_rules):
    rules = dict()

    for raw_rule in raw_rules:
        bag_type =  raw_rule[:raw_rule.index(' bags')]

        children_str = raw_rule[raw_rule.index('contain '):].replace('contain ', '').replace('.', '')
        rules[bag_type] = []

        if children_str.startswith('no'):
            continue

        for child in children_str.split(', '):
            rules[bag_type].append(child[2:].replace(' bags', '').replace(' bag', ''))

    return rules


def make_hierarchy(rules):
    roots = []
    nodes = dict()

    for parent, children in rules.items():

        if parent in nodes:
            root = nodes[parent]
        else:
            root = TreeNode(parent)
            nodes[parent] = root
            roots.append(root)

        for child in children:
            if child in nodes:
                child_node = nodes[child]
            else:
                child_node = TreeNode(child)
                nodes[child] = child_node
            root.add_child(child_node)

    return roots

def get_all_children_for_node(node):
    all_children = []

    # if node.data == 'bright white':
    #     breakpoint()

    for child in node.children:
        all_children.append(child.data)
        all_children += get_all_children_for_node(child)

    return all_children

def get_all_children_for_rule(rules, rule):
    all_children = []

    for child in rules[rule]:
        all_children.append(child)
        all_children += get_all_children_for_rule(rules, child)

    return all_children

if __name__ == "__main__":
    raw_rules = get_raw_rules()
    rules = parse_rules(raw_rules)
    # roots = make_hierarchy(rules)
    count = 0

    for rule in rules:
        all = get_all_children_for_rule(rules, rule)
        if 'shiny gold' in all:
            # print(root.data, all)
            count += 1

    print('answer:', count)


