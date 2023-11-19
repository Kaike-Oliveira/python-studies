# Main file of docstrings

# Imports
import single_line
import multiple_lines
import func_doc


print(20 * '*', 'Single Line', 20 * '*')
print(dir(single_line))
print(help(single_line))

print(20 * '*', 'Multiple Lines', 20 * '*')
print(help(multiple_lines))

print(20 * '*', 'Function Docs', 20 * '*')
print(help(func_doc))
