from antlr4 import *
import sys
sys.path.append('/workspaces/compiladores_25')
from actividad_combinacion_if_for_switch.CombinationLangLexer import CombinationLangLexer
from actividad_combinacion_if_for_switch.CombinationLangParser import CombinationLangParser

# === Entrada de prueba ===
input_text = "x = 0; for (i = 0; i < 3; i = i + 1) {switch (i) {case 0: x = x + 1;case 1: x = x + 2;default: x = x + 3;}}if (x > 5) {y = x * 10;}"

# Crear flujo de entrada
input_stream = InputStream(input_text)

# === Fase léxica ===
lexer = CombinationLangLexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("## 🔤 TOKENS")
for token in token_stream.tokens:
    if token.type != Token.EOF:
        print(f"  - {lexer.symbolicNames[token.type]} ('{token.text}') @line {token.line}:{token.column}")

print("\n## 🌳 ÁRBOL SINTÁCTICO (toStringTree)")
parser = CombinationLangParser(token_stream)
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