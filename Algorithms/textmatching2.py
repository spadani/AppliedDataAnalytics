
#O(n**2)
#first n determines the parantheses in the polynomials, second n is for determining the evaluations within each polynomail. this results in n squared

### TEXT MATCHING TO SOLVE POLYNOMIAL

#test cases:
polynomial = "(x**2 + 5x**2 - 3x + 3) + (-4x**5 - 2x**2 + 1)"
#polynomial = "(x**2 + 5x**2 - 3x + 3) + (-4x**5 - 2x**2 + 1) + (-8x)"
#polynomial = "(x**2 + 5x**2 - 3x + 3) + (-4x**5 - 2x**2 + 1) - (-1x**2) + (-8x)"


# return the final string
def generate_final_string(poly_dict, extras):
    final = ''

    for exponent, coefficient in poly_dict.items():
        coeff_string = str(coefficient)
        if '-' not in coeff_string:
            coeff_string = '+' + coeff_string

        if exponent == '1':
            final += coeff_string + 'x'
        else:
            final += coeff_string + 'x**' + exponent

    extra_str = str(extras)

    if extra_str.startswith('-'):
        final += str(extras)
    else:
        final += '+' + str(extras)

    if final.startswith('+'):
        final = final[1:len(final)]

    return final


#combine similar polynomials together by checking to see if there is an exponent that was already included and
# if it finds the same exponent it and adds the number aka the coefficients together
#poly_dict: key is the exponent, value is the coefficient
def combine_poly(poly_dict, exponent, operator, number):
    if poly_dict.get(exponent):
        poly_dict[exponent] += eval('0' + operator + number)
    else:
        poly_dict[exponent] = eval('0' + operator + number)

#seperates polys into the mini poly and the exponent
def combine_common_polys(polys):
    poly_dict = {}
    extras = 0

    for operator, poly in polys:
        ### if the poly has an x
        if 'x' in poly:
            ### searches for the ** pattern
            poly_split = poly.split('**')
            # exponent because the length of the array is 2 (the first item is the mini poly and the second is the exponent)
            if len(poly_split) > 1:
                exponent = poly_split[1]
                xnumber = poly_split[0]
                # this assigns the coefficient to each xnumber
                number = xnumber[0] if xnumber != 'x' else '1'
                combine_poly(poly_dict, exponent, operator, number)
            # no exponent - assigns the number to an exponent of 1
            else:
                xnumber = poly_split[0]
                #if its equal to x then assign it a coefficient of 1
                number = xnumber[0] if xnumber != 'x' else '1'
                combine_poly(poly_dict, '1', operator, number)
        # if there is no x in poly we assume that its an integer
        else:
            extras += int(poly)
    return poly_dict, extras


# converts/chunks each poly into the operator and the poly equation
def poly_chunk(operator, equation):
    new_poly = None
    if equation[0] == '-':
        current_operator = '-'
        equation = equation[1:len(equation)]
    else:
        current_operator = '+'

    polys = []


### separate polynomial into individual polynomials using + or - operators and store in polys (list of tuples where the first item is the operator
    # and the second item is the actual poly)
    for i, char in enumerate(equation):
        if char == '-' or char == '+':
            start_index = 0 if new_poly is None else new_poly + 1
            polys.append((current_operator, equation[start_index:i]))
            current_operator = char
            new_poly = i

    start_index = 0 if new_poly is None else new_poly + 1
    polys.append((current_operator, equation[start_index:len(equation)]))

### converts inner polynomial operators based on if the entire polynomial is being added or subtracted
    if operator == '-':
        reverse_polys = []
        for poly_operator, poly in polys:
            if poly_operator == '-':
                poly_operator = '+'
            else:
                poly_operator = '-'
            reverse_polys.append((poly_operator, poly))

        polys = reverse_polys
    return polys


# removes the spaces in the text and finds each polynomial
def find_polys(polynomial):
    spaceless_polynomial = polynomial.replace(" ", "")
    operator_polys = []
    open_index = None
    close_index = None
    for i, char in enumerate(spaceless_polynomial):
        if char == '(':
            open_index = i
        elif char == ')':
            close_index = i

        if open_index is not None and close_index is not None:
            operator = spaceless_polynomial[open_index - 1] if open_index != 0 else None
            equation = spaceless_polynomial[open_index+1:close_index]
            operator_polys.extend(poly_chunk(operator, equation))

            open_index = None
            close_index = None


    return operator_polys


all_polys = find_polys(polynomial)
poly_dict, extras = combine_common_polys(all_polys)
print(generate_final_string(poly_dict, extras))