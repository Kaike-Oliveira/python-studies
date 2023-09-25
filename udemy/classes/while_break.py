# While and Break
# Execute an action when condition is true
# Be careful this can cause a infinite looping

counter = 0

while counter < 10:
    counter += 1
    print(counter)

counter_2 = 10

while counter_2 > 0:
    counter_2 -= 1
    print(counter_2)

print(15 * '#')

qtd_rows = 5
qtd_cols = 5

current_row = 1
while current_row <= qtd_rows:
    current_col = 1
    while current_col <= qtd_cols:
        print(f'{current_row=} {current_col=}')
        current_col += 1
    current_row += 1
