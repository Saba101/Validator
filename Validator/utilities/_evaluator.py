from Validator.utilities._operator import Operations
class Evaluator:

    ## Evaluator needs to evalate a single expression against a particular record

    def __init__(self):
        self._operations = Operations()
        self.__evaluated_expressions = list()
        self.failed_record_data = dict()

    def evaluate(self, expression, record, column_names):
        for col_name in column_names:
            if str(expression['column']) == str(col_name):
                record_value = record[str(col_name)]
                condition = str(expression['condition']).lower()
                exp_info = str(expression['value'])

                # print(record_value , condition, exp_info)

                self._operations.select_operation(condition)
                evaluated = self._operations.apply_operation((str(record_value), str(exp_info)))
                print(f"> value: {record_value} {condition} {exp_info} ({evaluated})")

                if evaluated == False:  # failed expression
                    key = col_name
                    value = record_value
                    self.failed_record_data[str(key)] = value

                self.__evaluated_expressions.append(evaluated)
                return record_value, condition, exp_info, evaluated

    def get_evaluated_expressions(self):
        return self.__evaluated_expressions

    def get_failed_record_data(self):
        return self.failed_record_data