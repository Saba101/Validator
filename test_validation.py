import pandas as pd
from Validator import Validator

if __name__ == '__main__':
    input_file_path = "C:\\Users\\saamin\\OneDrive - Zones\\Documents\\_testFiles\\"
    input_filename = "Ingram_832_EDI_Products"
    # ext = ".csv"

    rules_file_path = "C:\\Users\\saamin\\PycharmProjects\\ValidatorModule\\samples\\"
    rule_filename = "sample-2"

    #Create an instance of validator class
    validator = Validator()

    #Pass two files for inspection
    # 1)The data you need to inspect
    # 2)The rules that inspect the data
    validation_info = validator.validate(input_file_path+input_filename, rules_file_path+rule_filename)
    print("\nValidation Info against every record in file:\n", validation_info)