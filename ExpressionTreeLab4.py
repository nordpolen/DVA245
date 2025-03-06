# tokenize from:
#
# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# ------------------------
# ADDED: 2025-02-25, Josefina
# Class to represent a node in an expression tree and a main function to test it.
# ------------------------
class Node:
    """
    Abstract base class for all nodes in the tree structure.
    Defines the interface for representing and evaluating an expression.
    """
    def to_string(self):
        """Return a string representation of the expression."""
        raise NotImplementedError('must be implemented by subclass')
    
    def evaluate(self):
        """Return a numeric result of the expression."""
        raise NotImplementedError('must be implemented by subclass')

# Class to represent a numeric node in an expression tree.
class NumericNode(Node):
    """
    Class representing a numeric node (leaf) in the expression tree.
    """
    def __init__(self, value):
        # Value of the numeric node
        self._value = int(value)

    def to_string(self):
        # Return string representation of the numeric value
        return str(self._value)

    def evaluate(self):
        # Return the numeric value of the node
        return self._value

# Class to represent an operator node in an expression tree.
class OperatorNode(Node):
    """
    Class representing an operator node that connects two subtrees.
    """
    def __init__(self, operator, left_operand, right_operand):
        self._operator = operator # Operator symbol (+, -, *, /)
        self._left = left_operand # Left operand (Node)
        self._right = right_operand # Right operand (Node)

    def to_string(self):
        # Return a string representation of the expression
        return '({} {} {})'.format(self._left.to_string(), self._operator, self._right.to_string())

    def evaluate(self):
        # Perform the arithmetic operation based on the operator
        if self._operator == '+':
            result = self._left.evaluate() + self._right.evaluate()
        elif self._operator == '-':
            result = self._left.evaluate() - self._right.evaluate()
        elif self._operator == '*':
            result = self._left.evaluate() * self._right.evaluate()
        elif self._operator == '/':
            result = self._left.evaluate() / self._right.evaluate()
        else:
            raise ValueError('Invalid operator: {self._operator}')
        
        # Convert the result to an integer if it is a whole number
        return int(result) if result == int(result) else result

# ------------------------
def tokenize(raw):
    """Produces list of tokens indicated by a raw expression string.

    For example the string '(43-(3*10))' results in the list
    ['(', '43', '-', '(', '3', '*', '10', ')', ')']
    """
    SYMBOLS = set('+-*/() ')   

    mark = 0
    tokens = []
    n = len(raw)
    for j in range(n):
        if raw[j] in SYMBOLS:
            if mark != j:                 
                tokens.append(raw[mark:j])  # complete preceding token
            if raw[j] != ' ':
                tokens.append(raw[j])       # include this token
            mark = j+1                    # update mark to being at next index
    if mark != n:                 
        tokens.append(raw[mark:n])      # complete preceding token
    return tokens
# ------------------------

# Function to check if a token is an operator.
def is_operator(token):
    """
    Returns True if the token is an operator, False otherwise.
    """
    return token in '+-*/'

# Function to build an expression tree from a list of tokens.
def build_expression_tree(tokens):
    """
    Function that constructs an expression tree from a list of tokens.
    Uses a stack to keep track of nodes and operators.
    """
    stack = [] # Stack to keep track of nodes and operators

    for token in tokens:
        if is_operator(token):
            stack.append(token) # Push operator onto the stack
        elif token.isnumeric():
            try:
                node = NumericNode(token) # Create a numeric node
                stack.append(node)
            except ValueError:
                raise ValueError(f"Invalid token in expression: {token}")
        elif token == ')':
            # Pop the right operand, operator, and left operand
            right = stack.pop()
            operator = stack.pop()
            left = stack.pop()
            # Create a new operator node and push onto the stack
            node = OperatorNode(operator, left, right)
            stack.append(node)

    return stack.pop() # The last element in the stack is the root of the expression tree


def main():
    test_expression_string= '(((3+5)/(5-3))+((2*5)-(9-4)))'
    tokens = tokenize(test_expression_string)
    print(f'Tokens: {tokens}')

    tree = build_expression_tree(tokens)
    print(f'Expression: {tree.to_string()}')
    print(f'Result: {tree.evaluate()}')

    # tokens = tokenize('+')
    # print(f'Tokens: {tokens}')
    # tree = build_expression_tree(tokens)
    # print(f'Expression: {tree}')
    # print(f'Result: {tree.evaluate()}')

    # tokens = tokenize('5.5')
    # print(f'Tokens: {tokens}')
    # tree = build_expression_tree(tokens)
    # print(f'Expression: {tree.to_string()}')
    # print(f'Result: {tree.evaluate()}')

if __name__ == "__main__":
    main()
    