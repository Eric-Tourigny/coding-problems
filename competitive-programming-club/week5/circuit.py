def T_or_F(s):
    if (s == "T"):
        return True
    else:
        return False


n = int(input())
truth_values = list(map(T_or_F, input().split()))

def get_truth_value(char):
    if char is None:
        return False
    return truth_values[ord(char) - ord('A')]

class Tree:
    def __init__(self, parent):
        self.lhs = None
        self.rhs = None
        self.op = None
        self.parent = parent
    
    def __str__(self):
        if self.op == "-":
            return f"(- {self.lhs})"
        else:
            return f"({self.lhs} {self.op} {self.rhs})"
    
    def add_op(self, char):
        if self.op is None:
            self.op = char
            return True
        else:
            return False

def build_tree(expression, char):
    if char in ("*", "+", "-"):
        if expression.op is None:
            expression.op = char
            if expression.op == "-":
                expression.rhs = "A"
        else:
            if expression.rhs is None:
                expression.rhs = Tree(expression)
                expression = expression.rhs
                return build_tree(expression, char)
            elif expression.lhs is None:
                expression.lhs = Tree(expression)
                expression = expression.lhs
                return build_tree(expression, char)
            else:
                return build_tree(expression.parent, char)
    else:
        if expression.rhs is None:
            expression.rhs = char
        elif expression.lhs is None:
            expression.lhs = char
        else: 
            return build_tree(expression.parent, char)
    return expression

original_expression = Tree(None)
current_expression = original_expression

input_values = input().split()
if len(input_values) == 1:
    print("T" if get_truth_value(input_values[0]) else "F")
else:
    for char in reversed(input_values):
        current_expression = build_tree(current_expression, char)

    def evaluate_tree(expression):
        if type(expression) is str:
            return get_truth_value(expression)

        if expression.op == "*":
            return evaluate_tree(expression.lhs) and evaluate_tree(expression.rhs)
        if expression.op == "+":
            return evaluate_tree(expression.lhs) or evaluate_tree(expression.rhs)
        if expression.op == "-":
            return not evaluate_tree(expression.lhs)
    print("T" if evaluate_tree(original_expression) else "F")