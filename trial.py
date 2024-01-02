# import math
# a = 5694
# check = isinstance(a,int)
# print(check)
# b = [
#       [0,2,3, 4,5,6, 7,8,9],
#       [1,2,3, 4,5,6, 7,8,9],
#       [1,2,3, 4,5,6, 7,8,9],
      
#       [1,2,3, 4,5,6, 7,8,9],
#       [1,2,3, 4,5,6, 7,8,9],
#       [1,2,3, 4,5,6, 7,8,9],
#       [2],
      
#       [1,2,3, 4,5,6, 7,8,9],
#       [1,2,3, 4,5,6, 7,8,9],
#       [1,2,3, 4,5,6, 7,8]
      
#     ]
# total_length = sum(len(item) if isinstance(item, list) else 1 for item in b)
# print(total_length)
# sqt_val = math.sqrt(total_length)
# print(sqt_val)
# checker = False
# for elmt in b:
#     if(len(elmt)==sqt_val):
#         print("coninue")
#         checker = True
#     else:
#         print("stop")
#         checker = False
#         break

# print(checker)

# if checker:
#     for sub_lis in b:
#         for i in sub_lis:
#             pass
    
    
    
def justify_text(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(current_line)
            current_line = [word]
            current_length = len(word)

    # Add the last line without justification
    lines.append(current_line)

    justified_lines = []
    for line in lines[:-1]:
        total_spaces = width - sum(len(word) for word in line)
        gaps = len(line) - 1

        if gaps == 0:
            justified_lines.append(' '.join(line))
        else:
            spaces_per_gap = total_spaces // gaps
            extra_spaces = total_spaces % gaps

            justified_line = ''
            for i, word in enumerate(line[:-1]):
                justified_line += word + ' ' * spaces_per_gap
                if i < extra_spaces:
                    justified_line += ' '

            justified_line += line[-1]
            justified_lines.append(justified_line)

    # Add the last line without justification
    justified_lines.append(' '.join(lines[-1]))

    return '\n'.join(justified_lines)


# Example usage:
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
width = 30
justified_text = justify_text(text, width)
print(justified_text)


from itertools import permutations

def string_permutations(input_str):
    # Use itertools.permutations to generate permutations
    perms = permutations(input_str)
    print(perms)

    # Convert each permutation tuple to a string
    result = [''.join(p) for p in perms]

    return result

# Example usage:
input_string = "abc"
permutations_result = string_permutations(input_string)

# Print the result
print(permutations_result)




# spaces_distribution.reverse()
# 



    
