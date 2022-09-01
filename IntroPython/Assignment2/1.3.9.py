# print a payroll statement based on employee name, hours worked, pay rate, and tax rate
# include calculations for gross pay and total deductions


def payroll(name, hours, rate, ftax_rate, stax_rate):
    # define payroll variables
    gpay = rate*hours
    ftax = gpay * ftax_rate
    stax = gpay * stax_rate
    total_ded = ftax + stax
    net = gpay - total_ded
    # print statements for payroll, format values
    print('Employee Name:', name)
    print('Hours Worked:', hours)
    print('Pay Rate: ${}.00'.format(rate))
    print('Gross Pay: ${}.00'.format(gpay))
    print('  Deductions: ')
    print('  Federal Withholding ({}%): ${}.00'.format(ftax_rate * 100, ftax))
    print('  State Withholding ({}%): ${}.00'.format(stax_rate * 100, stax))
    print('  Total Deduction: ${}.00'.format(total_ded))
    print('Net Pay: ${}.00'.format(net))


def main():
    # print user statements and evaluate, callback to payroll function
    name = input("Enter employees name: ")
    hours = eval(input("Enter number of hours worked in a week: "))
    rate = eval(input("Enter hourly pay rate: "))
    ftax_rate = eval(input("Enter federal tax withholding rate: "))
    stax_rate = eval(input("Enter state tax withholding rate: "))
    payroll(name, hours, rate, ftax_rate, stax_rate)


main()

