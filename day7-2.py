import re

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
            match = re.match('([0-9]+) (.*)', child)
            rules[bag_type].append(
                (
                    int(match.groups()[0]),
                    match.groups()[1].replace(' bags', '').replace(' bag', '')

                )
            )
    return rules

def get_all_children_for_rule(rules, rule):
    all_children = []

    for child in rules[rule]:
        for i in range(child[0]):
            all_children.append(child[1])
            all_children += get_all_children_for_rule(rules, child[1])

    return all_children

if __name__ == "__main__":
    raw_rules = get_raw_rules()
    rules = parse_rules(raw_rules)

    count = 0

    shiny_gold = get_all_children_for_rule(rules, 'shiny gold')

    print(len(shiny_gold))
    # print('answer:', count)


