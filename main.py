problem = "99 + 12"
split_problem = problem.split()
#print(split_problem)
if split_problem[1] != ("-" or "+"):
    print("Error: Operator must be '+' or '-'.")

top_problem = split_problem[0]
bottom_problem = split_problem[1] + " " + split_problem[2]

solve = True

# solve input
# while True:
#     solve = input('Solve? True or False\n')
#     solve = solve.lower().capitalize()
#     if solve == "True" or solve == 'False':
#         break
#     print("Try again, True or False")

answer = ""

if solve == True:
    if split_problem[1] == "+":
        answer = int(split_problem[0]) + int(split_problem[2])
    elif split_problem[1] == "-":
        answer = int(split_problem[0]) - int(split_problem[2])
    else:
        print("Error: Operator must be '+' or '-'.")

# Find which length is longer top or bottom or answer
a = len(top_problem)
b = len(bottom_problem)
d = len(str(answer))

if a > b and a > d:
    c = a
if b >= a and b >= d:
    c = b
else:
    c = d

# format top and bottom string so that they are the length of the 
# longest half
format_top_problem = f'{top_problem:>{c}}'
format_bottom_problem = f'{bottom_problem:>{c}}'

print(format_top_problem)
print(format_bottom_problem)
print("-"*c)

if solve == True:        
    answer = (f'{answer:>{c}}')
    print(answer)
    #print(len(answer))
