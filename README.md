numpy_json
==========

Library for converting numpy ndarrays to and from json

inspired by
-----------
* [JSON tricks](http://json-tricks.readthedocs.org/en/latest/)
* [tlausch on stackoverflow](http://stackoverflow.com/questions/3488934/simplejson-and-numpy-array)

example usage: complex numbers
------------------------------
```python
import numpy as np
import numpy_json

data = np.random.randint(0, 100, size=(2,3)).astype(np.complex64)
data += 1j * np.random.randint(0, 100, size=(2,3))

json_string = numpy_json.dumps(data)
print "json encoded array:", json_string

parsed_data = numpy_json.loads(json_string)
print "parsed shape: ", parsed_data.shape
print "parsed dtype: ", parsed_data.dtype
```

output:
```
json encoded array: {"arraydtype": "complex64", "arraysize": [2, 3], "arraydata": [[{"real": 56.0, "imag": 38.0}, {"real": 87.0, "imag": 66.0}, {"real": 54.0, "imag": 14.0}], [{"real": 27.0, "imag": 0.0}, {"real": 25.0, "imag": 58.0}, {"real": 24.0, "imag": 46.0}]]}
parsed shape:  (2, 3)
parsed dtype:  complex64
```

example usage: no dtype, custom keys
------------------------------------
```python
import numpy as np
import numpy_json

data = np.random.randint(0, 100, size=(1,5)).astype(np.uint8)
json_keys = dict(data="data", shape="size")

json_string = numpy_json.dumps(data, json_keys=json_keys)
print "json encoded array:", json_string

parsed_data = numpy_json.loads(json_string, json_keys=json_keys)
print "parsed shape: ", parsed_data.shape
print "parsed dtype: ", parsed_data.dtype
```

output:
```
json encoded array: {"data": [[74, 94, 34, 3, 25]], "size": [1, 5]}
parsed shape:  (1, 5)
parsed dtype:  float64
```