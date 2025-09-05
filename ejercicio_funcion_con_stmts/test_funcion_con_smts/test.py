from antlr4 import *
import sys
sys.path.append('/workspaces/compiladores_25')
from ejercicio_funcion_con_stmts.CombinationLangFuncLexer import CombinationLangFuncLexer
from ejercicio_funcion_con_stmts.CombinationLangFuncParser import CombinationLangFuncParser

# === Entrada de prueba ===
input_text = "func suma(a, b) {x = a + b;return x;}func test() {y = 0;for (i = 0; i < 3; i = i + 1) {switch (i) {case 0: y = y + 1;default: y = y + 2;}}return y;}"

# Crear flujo de entrada
input_stream = InputStream(input_text)

# === Fase léxica ===
lexer = CombinationLangFuncLexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("## 🔤 TOKENS")
for token in token_stream.tokens:
    if token.type != Token.EOF:
        print(f"  - {lexer.symbolicNames[token.type]} ('{token.text}') @line {token.line}:{token.column}")

print("\n## 🌳 ÁRBOL SINTÁCTICO (toStringTree)")
parser = CombinationLangFuncParser(token_stream)
tree = parser.programa()
print(tree.toStringTree(recog=parser))

# === Representación indentada ===
def pretty_tree(node, rule_names, level=0):
    if isinstance(node, TerminalNode):
        return "  " * level + f"TOKEN({node.getText()})"
    else:
        rule_name = rule_names[node.getRuleIndex()]
        result = "  " * level + rule_name
        for child in node.children or []:
            result += "\n" + pretty_tree(child, rule_names, level + 1)
        return result

print("\n## 🌲 ÁRBOL SINTÁCTICO (Indentado)")
print(pretty_tree(tree, parser.ruleNames))