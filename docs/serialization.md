# Saving and Loading from Files

## Serialization to `dict`

Any `Solution` can be converted into a `dict` by calling `as_dict`:

```python
>>> from pyEQL import Solution
>>> s = Solution({"Na+": "0.5 mol/L", "Cl-": "0.5 mol/L"})
>>> s.as_dict()
{'@module': 'pyEQL.solution', '@class': 'Solution', '@version': '0.5.2', 'solutes': {'H2O(aq)': '55.34455402076251 mol', 'H[+1]': '1e-07 mol', 'OH[-1]': '1e-07 mol'}, 'volume': '1 l', 'temperature': '298.15 K', 'pressure': '1 atm', 'pH': 7.0, 'pE': 8.5, 'balance_charge': None, 'solvent': 'H2O(aq)', 'engine': 'native', 'database': {'@module': 'maggma.stores.mongolike', '@class': 'JSONStore', '@version': '0.19.1.post1.dev1792+g0517496', 'paths': ['/home/ryan/mambaforge/envs/pbx/code/pyEQL/src/pyEQL/database/pyeql_db.json'], 'read_only': True, 'serialization_option': None, 'serialization_default': None, 'key': 'formula'}}
```

This `dict` can be stored in a database or used to [recreate the `Solution`](creating.md)
using `from_dict()`.

## Saving to a `.json` file

`Solution` can be serialized (and later recreated from) a `.json` file using
[`monty.serializtaion.dumpfn`](https://pythonhosted.org/monty/monty.html#module-monty.serialization).

```python
>>> from pyEQL import Solution
>>> from monty.serialization import dumpfn
>>> s = Solution({"Na+": "0.5 mol/L", "Cl-": "0.5 mol/L"})
>>> dumpfn(s, 'test.json')
```

## Loading from a `.json` file

Similarly, [monty.serialization.loadfn](https://pythonhosted.org/monty/monty.html#module-monty.serialization) can be used to create a `Solution` from a compatible
`.json` file.

```python
>>> from monty.serialization import loadfn
>>> s = loadfn('test.json')
print(s)
Volume: 1.000 l
Pressure: 1.000 atm
Temperature: 298.150 K
Components: ['H2O(aq)', 'H[+1]', 'OH[-1]']
```

:::{note}
In a future release, `to_file()` / `from_file()` methods may be added to `Solution` to
make the above steps easier. Please post on GitHub if you have strong opinions about
this!
:::
