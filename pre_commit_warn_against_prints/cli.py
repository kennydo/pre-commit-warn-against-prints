import argparse
import ast


def user_responds_affirmatively():
    received = input()
    if not received:
        return False

    truthy_responses = set([
        'y',
        'yes',
        'true',
    ])
    return received.lower() in truthy_responses


class PrintStatementParser(ast.NodeVisitor):
    def __init__(self):
        self.print_nodes = []

    def visit_Call(self, node):
        if not isinstance(node.func, ast.Name):
            return

        if node.func.id != 'print':
            return

        self.print_nodes.append(node)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    detected_print_nodes = False

    for filename in args.filenames:
        with open(filename) as f:
            file_content = f.read()

        try:
            ast_object = ast.parse(file_content, filename=filename)
        except SyntaxError:
            print("Could not parse AST of {0}".format(filename))
            return 1

        file_lines = file_content.split("\n")

        visitor = PrintStatementParser()
        visitor.visit(ast_object)

        for node in visitor.print_nodes:
            print("{filename}:{lineno} called `print`: {source}".format(
                filename=filename,
                lineno=node.lineno,
                source=file_lines[node.lineno - 1],
            ))

        if visitor.print_nodes:
            detected_print_nodes = True

    retval = 0

    if detected_print_nodes:
        print("")
        print("There were calls to `print` detected.")
        print("Have you considered using the standard library logger instead (y/[n])? ", end="")

        if user_responds_affirmatively():
            retval = 0
        else:
            retval = 1

    return retval

