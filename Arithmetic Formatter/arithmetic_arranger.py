def arithmetic_arranger(problems, show_results=False):
  if len(problems) > 5:
      return "Error: Too many problems."
  
  arranged_problems = []
  for problem in problems:
      items = problem.split()
      operand1, operator, operand2 = items
  
      if operator not in ['+', '-']:
          return "Error: Operator must be '+' or '-'."
  
      if not (operand1.isdigit() and operand2.isdigit()):
          return "Error: Numbers must only contain digits."
  
      if len(operand1) > 4 or len(operand2) > 4:
          return "Error: Numbers cannot be more than four digits."
  
      width = max(len(operand1), len(operand2)) + 2
      formatted = f"{operand1.rjust(width)}\n{operator} {operand2.rjust(width - 2)}\n{'-' * width}"
  
      if show_results:
          result = str(eval(problem))
          formatted += f"\n{result.rjust(width)}"
  
      arranged_problems.append(formatted)
  
  return "    ".join(arranged_problems)
  
