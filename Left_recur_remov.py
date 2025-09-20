def remove_left_recursion(grammar_rules):
    updated_grammar = {}

    for non_terminal in grammar_rules:
        productions = grammar_rules[non_terminal]
        alpha = []  
        beta = []

        for prod in productions:
            if prod.startswith(non_terminal):
                alpha.append(prod[len(non_terminal):])
            else:
                beta.append(prod)

        if alpha:
            new_non_terminal = non_terminal + "'"
            updated_grammar[non_terminal] = [b + new_non_terminal for b in beta]
            updated_grammar[new_non_terminal] = [a + new_non_terminal for a in alpha]
            updated_grammar[new_non_terminal].append("ε") 
        else:
            updated_grammar[non_terminal] = productions

    return updated_grammar


def parse_input():
    grammar_rules = {}
    print("Enter your grammar (format: S->x|y). Empty line to finish:")

    while True:
        line = input()
        if not line.strip():
            break
        if '->' in line:
            non_terminal, productions = line.split("->")
            non_terminal = non_terminal.strip()
            prods = [prod.strip() for prod in productions.split('|')]
            grammar_rules[non_terminal] = prods

    return grammar_rules


def print_grammar(grammar, title):
    print(f"\n{title}")
    for non_terminal in grammar:
        productions = " | ".join(grammar[non_terminal])
        print(f"{non_terminal} → {productions}")


def main():
    grammar = parse_input()
    print_grammar(grammar, "Original Grammar:")
    updated_grammar = remove_left_recursion(grammar)
    print_grammar(updated_grammar, "Grammar after eliminating left recursion:")


if __name__ == "__main__":
    main()
