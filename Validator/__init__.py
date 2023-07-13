import json

from Validator.utilities._evaluator import Evaluator
import Validator.utilities._operator as operator
import pandas as pd

class Validator:

    ## Validator is responsible for the validation of all the expressions against
    ## a single record from source file

    def __init__(self):
        self.rules = None

        self._validated = False
        self.__validation_operations = {
            "and": operator.and_,
            "or": operator.or_,
        }
        self.validation_result = dict()


    def extract_rules(self, rules_file):
        import json
        file = open(rules_file + ".json")
        rules = json.load(file)
        print('Rule in file: ', rules, '\n')

        if len(rules['expression']) - 1 == len(rules['logicalOperators']):
            # Get expressions and operators out of rules
            self._expressions = rules['expression']
            self._operators = rules['logicalOperators']

        else:
            print("Invalid rules defined in file..")
            print("Validation could not be performed. Ending program!")


    def validate(self, file_to_inspect, rules_file):
        self.extract_rules(rules_file)
        df = pd.read_csv(file_to_inspect + '.csv', na_filter=False)
        column_names = df.columns.tolist()

        for i, record in df.iterrows():
            print(f"\nRecord {i+1}:")

            self._evaluator = Evaluator()
            for exp in self._expressions:
                print("Expression: ", exp['column'], exp['condition'], exp['value'])
                self._evaluator.evaluate(exp, record, column_names)

            evaluated_expressions = self._evaluator.get_evaluated_expressions()
            # print(evaluated_expressions)

            eval1 = evaluated_expressions[0]
            if len(evaluated_expressions) > 1:
                for j in range(len(evaluated_expressions)):
                    if j < len(self._operators):
                        op = self.__validation_operations.get(str.lower(self._operators[j]))
                        eval2 = evaluated_expressions[j + 1] if (evaluated_expressions[j + 1] != None) and \
                                                                (j + 1 <= len(evaluated_expressions)) else None

                        if eval2 != None:
                            self._validated = op(eval1, eval2)
                            eval1 = self._validated
                        else:
                            print("Error: cannot evaluate expression - one expression is missing!")
            else:
                self._validated = eval1

            if self._validated == True:
                self._validated = "Validation Successful"
            else:
                self._validated = "Validation Unsuccessful"
            print(self._validated)

            # print(f"record({i+1}): {self._validated}")
            self.validation_result[f"record({i})"] = self._validated
        return self.validation_result


    # # def validate(self, record):
    #     self._evaluator = Evaluator()
    #     for exp in self._expressions:
    #         print("Expression: ", exp['Column'], exp['Condition'], exp['Value'])
    #         self._evaluator.evaluate(exp, record)
    #
    #     evaluated_expressions = self._evaluator.get_evaluated_expressions()
    #     eval1 = evaluated_expressions[0]
    #     if len(evaluated_expressions) > 1:
    #         for i in range(len(evaluated_expressions)):
    #             if i < len(self._operators):
    #                 op = self.__validation_operations.get(str.lower(self._operators[i]))
    #                 eval2 = evaluated_expressions[i + 1] if (evaluated_expressions[i + 1] != None) and \
    #                                                         (i + 1 <= len(evaluated_expressions)) else None
    #
    #                 if eval2 != None:
    #                     self._validated = op(eval1, eval2)
    #                     eval1 = self._validated
    #                 else:
    #                     print("Error: cannot evaluate expression - one expression is missing!")
    #     else:
    #         self._validated = eval1
    #     return self._validated, self._evaluator.get_failed_record_data()
