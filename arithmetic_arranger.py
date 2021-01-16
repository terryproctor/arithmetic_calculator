def arithmetic_arranger(problems, solve = False):
    # lists created so that they can be printed as one line
    # each problem will have the same width
    # each problem will need to have 4 spaces printed between each
    # maybe using seperators of "    "
    # format then append to each list, if solve on then function 
    # will solve problem too
    top_list = list()
    bottom_list = list()
    dash_list = list()
    answer_list = list()
    
    # no more than 4 problems to solve
    if len(problems) > 4:
        return "Error: Too many problems."
    
    for problem in problems:
        split_problem = problem.split() 

        #creating top and bottom parts of each equation
        top_problem = split_problem[0]
        bottom_problem = split_problem[1] + " " + split_problem[2]
        
        # removing errors and following rules
        if split_problem[1] != "+" and split_problem[1] != "-":
            return ("Error: Operator must be '+' or '-'.")

        for section in split_problem:
            if section != split_problem[1]:
                if section.isdigit() != True:
                    return "Error: Numbers must only contain digits."
            
            if len(section) > 4:
                return "Error: Numbers cannot be more than four digits."

        # solving the answer if required
        
        if solve == True:
            answer = ""
            if split_problem[1] == "+":
                answer = int(split_problem[0]) + int(split_problem[2])
            elif split_problem[1] == "-":
                answer = int(split_problem[0]) - int(split_problem[2])

        # Find which length is longer top or bottom or answer
        a = len(top_problem)
        b = len(bottom_problem)
        if solve == True:
            d = len(str(answer))
        else:
            d = 0

        if a > b and a > d:
            c = a
        elif b >= a and b >= d:
            c = b
        else:
            c = d

        # making sure that bottom line always has sign sticking out
        if b < a or b < d:
            bottom_problem = split_problem[1] + " "*c + split_problem[2]
            c = len(bottom_problem)

        # format top and bottom string so that they are the length of the 
        # longest half
        format_top_problem = f'{top_problem:>{c}}'
        format_bottom_problem = f'{bottom_problem:>{c}}'
        dash = ("-"*c)

        if solve == True:        
            answer = (f'{answer:>{c}}')
            answer_list.append(answer)

        top_list.append(format_top_problem)
        bottom_list.append(format_bottom_problem)
        dash_list.append(dash)

        print(c)
    
    # creating each line #!create a loop in future
    top_line = ''
    for entry in top_list:
        top_line += entry
        if entry != (len(top_list)-1):
            top_line += "    "

    bottom_line = ''
    for entry in bottom_list:
        bottom_line += entry
        if entry != (len(bottom_list)-1):
            bottom_line += "    "

    dash_line = ''
    for entry in dash_list:
        dash_line += entry
        if entry != (len(dash_list)-1):
            dash_line += "    "
    
    answer_line = ""
    if solve == True:
        for entry in answer_list:
            answer_line += entry
            answer_line += "    "

    #creating an output string 
    if solve:
        output = f"{top_line}\n{bottom_line}\n{dash_line}\n{answer_line}"
    else:
        output = f"{top_line}\n{bottom_line}\n{dash_line}"
    
    return output

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

# 123 + 49 the sign needs to be one more out, ie c needs to be one more