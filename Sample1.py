import re

with open("Sample1.c","r") as file:
    code = file.read()

code = re.sub(r"//.*"," ",code)
code = re.sub(r"/\*.*?\*/"," ",code, flags=re.DOTALL)


keywords = {'break', 'return', 'unsigned', 'enum', 'auto', 'signed', 'sizeof', 'do', 'goto', 'float', 'case', 'static', 'long', 'struct', 'else', 'double', 'switch', 'const', 'void', 'for', 'continue', 'short', 'int', 'typedef', 'union', 'while', 'default', 'if', 'char'}
arithmetic_operators = {'--', '+', '++', '=', '/', '*', '-', '%'}
logical_operators = {'||', '!=', '!', '&&'}
punctuation = {'.', ';', ',', '->', ':', '#', '?'}
parentheses = {')', '}', '{', '(', '[', ']'}

tokens = re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*|\d+|!=|[+\-*/=,;(){}]", code)
print("Token list: ")
print(tokens)
print("\nSample 1 Output: ")
keyword_tokens = set()
identifier_tokens = set()
constant_tokens = set()
arithmetic_tokens = set()
logical_tokens = set()
punctuation_tokens = set()
parenthesis_tokens = set()

for token in tokens:
    if token in keywords:
        keyword_tokens.add(token)
    elif token in arithmetic_operators:
        arithmetic_tokens.add(token)
    elif token in logical_operators:
        logical_tokens.add(token)
    elif token in punctuation:
        punctuation_tokens.add(token)
    elif token in parentheses:
        parenthesis_tokens.add(token)
    elif re.fullmatch(r"\d+", token): 
        constant_tokens.add(token)
    elif re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]*", token):  
        identifier_tokens.add(token)

print(f"Keyword ({len(keyword_tokens)}): {', '.join(sorted(keyword_tokens))}")
print(f"Identifier ({len(identifier_tokens)}): {', '.join(sorted(identifier_tokens))}")
print(f"Constant ({len(constant_tokens)}): {', '.join(sorted(constant_tokens))}")
print(f"Arithmetic Operator ({len(arithmetic_tokens)}): {', '.join(sorted(arithmetic_tokens))}")
print(f"Logical Operator ({len(logical_tokens)}): {', '.join(sorted(logical_tokens))}")
print(f"Punctuation ({len(punctuation_tokens)}): {', '.join(sorted(punctuation_tokens))}")
print(f"Parenthesis ({len(parenthesis_tokens)}): {', '.join(sorted(parenthesis_tokens))}")