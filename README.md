# ILM-Code-Challenge

# # Execution
- Clone the repository locally
- Open a DOS terminal from the directory which contains the modules

Run any of the following:

1) `python address_parser.py`
- From the example input in `__main__.py`
```
C:\Documents\Git\ILM-Code-Challenge> python address_parser.py
Address: {'province': 'BC', 'city': 'Vancouver', 'number': 567, 'street': 'W8th Ave', 'postal_code': 'D4E5F6', 'unit': 4}
C:\Documents\Git\ILM-Code-Challenge>
```

2) `python test_address_parser.py`
- Run the unit test
```
C:\Documents\Git\ILM-Code-Challenge> python test_address_parser.py
.Address: {'province': 'BC', 'city': 'Vancouver', 'street': 'Main St', 'postal_code': 'A1B2C3', 'number': '123'}
......
----------------------------------------------------------------------
Ran 7 tests in 0.008s

OK
C:\Documents\Git\ILM-Code-Challenge>
```

3) `python -m ILM-Code-Challenge`

- Runs the initialization of the package
```
C:\Documents\Git> python -m ILM-Code-Challenge
----------Running ILM Code Challenge---------
C:\Documents\Git>
```
4) Launch a Python Terminal & Run: `from ILM-Code-Challenge import {}`

- If you are in the `ILM-Code-Challenge` folder already, you can `import` directly
```
>>> import address_parser
>>> address_parser = address_parser.AddressParser()
>>> address = '4-567_W8th_Ave_Vancouver_BC_D4E5F6'
>>> address_parser.parse_address(address)
Address: {'province': 'BC', 'city': 'Vancouver', 'number': 567, 'street': 'W8th Ave', 'postal_code': 'D4E5F6', 'unit': 4}
{'province': 'BC', 'city': 'Vancouver', 'number': 567, 'street': 'W8th Ave', 'postal_code': 'D4E5F6', 'unit': 4}
>>>
```
