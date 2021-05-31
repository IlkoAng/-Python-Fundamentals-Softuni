basic_electrons = int(input())
shell = []
position = 1

while basic_electrons > 0:
    current_shell = 2 * position ** 2
    if basic_electrons < current_shell:
        shell.append(basic_electrons)
        break
    shell.append(current_shell)
    basic_electrons -= current_shell
    position += 1

print(shell)