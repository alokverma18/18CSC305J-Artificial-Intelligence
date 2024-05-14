# Helper function to apply substitution recursively
def apply_substitution(expr, substitution):
    if isinstance(expr, tuple):
        return tuple(apply_substitution(sub_expr, substitution) for sub_expr in expr)
    elif expr in substitution:
        return apply_substitution(substitution[expr], substitution)
    else:
        return expr

# Function to unify two equations
def unify_equations(equation1, equation2):
    # Find the substitution set
    substitution_set = {}
    for i in range(len(equation1)):
        if isinstance(equation1[i], str):
            substitution_set[equation1[i]] = equation2[i]

    # Apply the substitution set to equations
    final_equation1 = apply_substitution(equation1, substitution_set)
    final_equation2 = apply_substitution(equation2, substitution_set)

    return substitution_set, final_equation1, final_equation2

# Given equations
e1 = ('P', 'x', 'f(y)')
e2 = ('P', 'a', 'f(g(z))')

if(e1[0]!=e2[0]):
    print("Unification Failed")
else:
    equation1 = e1[1:]
    equation2 = e2[1:]
    # Unify equations
    substitution_set, final_equation1, final_equation2 = unify_equations(equation1, equation2)
    # Output substitution set and final unified solution
    print("Substitution set:", substitution_set)
    print("Unified solution:", final_equation1)