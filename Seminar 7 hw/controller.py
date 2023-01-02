import model
import view
import logger


def string_calculate():
    calc_string = view.input_string()
    result = model.calculate_str(calc_string)
    logger.string_logger(calc_string, result)
    view.print_result(result)

def console_calculate():
    model.set_first_number(view.input_number())
    operation = view.input_operation()
    operation_count = 1

    while operation != '=':
        if operation_count > 1:
            first = model.get_intermediate_result()
        else:
            first = model.get_first_number()
        model.set_next_number(view.input_number())
        second = model.get_next_number()
        oper = operation
        model.check_operation(operation)
        res = model.get_intermediate_result()
        view.print_result(model.get_intermediate_result())
        logger.logger(first, second, oper, res)
        operation = view.input_operation()
        operation_count += 1

    view.print_result(model.get_intermediate_result())

def start():
    if view.input_calc_type():
        string_calculate()
    else:
        console_calculate()