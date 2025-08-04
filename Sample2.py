import re

keywords = {"int", "float", "char", "void"}
arithmetic_operators = {"*", "+", "="}
punctuation = {",", ";"}
parentheses = {"(", ")", "{", "}"}

keyword_tokens = set()
identifier_tokens = set()
constant_tokens = set()
arithmetic_tokens = set()
punctuation_tokens = set()
parenthesis_tokens = set()

with open("Sample2.c", "r") as file:
    code = file.read()

code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)  
code = re.sub(r'//.*', '', code)  

tokens = re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*|\d+\.\d+|\d+|'[^']'|[+\-*/=,;(){}]", code)

for token in tokens:
    if token in keywords:
        keyword_tokens.add(token)
    elif token in arithmetic_operators:
        arithmetic_tokens.add(token)
    elif token in punctuation:
        punctuation_tokens.add(token)
    elif token in parentheses:
        parenthesis_tokens.add(token)
    elif re.fullmatch(r"\d+\.\d+", token):  
        constant_tokens.add(token)
    elif re.fullmatch(r"\d+", token):  
        constant_tokens.add(token)
    elif re.fullmatch(r"'[^']'", token):  
        constant_tokens.add(token)
    elif re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]*", token):
        identifier_tokens.add(token)

print(f"Keyword ({len(keyword_tokens)}): {', '.join(sorted(keyword_tokens))}")
print(f"Identifier ({len(identifier_tokens)}): {', '.join(sorted(identifier_tokens))}")
print(f"Constant ({len(constant_tokens)}): {', '.join(sorted(constant_tokens))}")
print(f"Arithmetic Operator ({len(arithmetic_tokens)}): {', '.join(sorted(arithmetic_tokens))}")
print(f"Punctuation ({len(punctuation_tokens)}): {', '.join(sorted(punctuation_tokens))}")
print(f"Parenthesis ({len(parenthesis_tokens)}): {', '.join(sorted(parenthesis_tokens))}")
