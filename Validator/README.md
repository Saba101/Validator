## JSON Expression Validator

Package Description: A Python package for validating CSV files based on JSON expressions.

Installation
You can install the package using pip:

Copy code: #private repositort
_pip install git+https://github.com/Saba101/Validator.git

Usage
1. Importing the Package: _from Validator import Validator_

2. The supported JSON format is:
```
{
  "expression": [
    {
      "column": "<attribute_name>",
      "condition": "<condition_supported_by_Validator>",
      "value": "<value_to_validate_attribute_against>"
    }

  ],
  "logicalOperators": [
    "<operator1>", 
    "<operator2>"
    ]
}
```
Possible options for 'condition':\
'not_equals',\
'equals',\
'is',\
'greater_than',\
'less_than',\
'greater_than_or_equal',\
'less_than_or_equal',\
'in',\
'is_empty',\
'not_empty',\
'contains',\
'starts_with',\
'ends_with'\

Possible options for 'logicalOperators':\
'and', 'or'

3. Validating CSV Data:
The method _validate_ of Validator package is one go way to validate you csv records against a json expression. \
Provide csv data file path and name, also provide json file path and name.
```
validator = Validator()
validation_info = validator.validate(input_file_path+input_filename, rules_file_path+rule_filename)
```

The function will return a dictionary of all row numbers (of provided file) and validation status against all rows.
e.g. {'record(0)': 'Validation Unsuccessful'

Please check "testValidator" file to learn about usage in more detail.

Please also check samples to view how JSON expression can be created. Provided that column name should match the header in your csv file, you can use these samples for understanding.
