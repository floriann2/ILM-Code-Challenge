# ILM-Code-Challenge

# # Execution
- Clone the repository locally
- Open a DOS terminal from the directory which contains the modules

Run any of the following:

1) `python address_parser.py`
- From the example input in `__main__.py`
```
C:\Documents\Git\ILM-Code-Challenge> python address_parser.py     
ADDRESS: {'province': 'BC', 'city': 'Vancouver', 'number': 567, 'street': 'W8th Ave', 'postal_code': 'D4E5F6', 'unit': 4}
C:\Documents\Git\ILM-Code-Challenge>
```

2) `python test_address_parser.py`
- Run the unit test
```
C:\Documents\Git\ILM-Code-Challenge> python test_address_parser.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.002s

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
>>> from ILM-Code-Challenge import address_parser
>>> address_parser = address_parser.AddressParser()
>>> address_parser.get_unit_number(4)
True
>>> address_parser.get_street_number(567)
True
>>> address_parser.get_street_name('W8th Ave')
True
>>> address_parser.get_city_name('Vancouver')
True
>>> address_parser.get_province_name('BC')
True
>>> address_parser.get_postal_code('D4E5F6')
True
>>> address = address_parser.get_address()
>>> address
{'province': 'BC', 'city': 'Vancouver', 'number': 567, 'street': 'W8th Ave', 'postal_code': 'D4E5F6', 'unit': 4}
>>>
