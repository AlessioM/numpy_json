import json
import numpy as np

_json_keys = dict(
    data="arraydata",
    dtype="arraydtype",
    shape="arraysize"
)    

_complex_keys = dict(
    real="real",
    imag="imag"
)

def dumps(data, json_keys=None, complex_keys=None):
    global _json_keys, _complex_keys
    
    if json_keys is None:
        json_keys = _json_keys

    if complex_keys is None:
        complex_keys = _complex_keys


    class NumpyEncoder(json.JSONEncoder):
    
        def default(self, obj):               
            if isinstance(obj, np.ndarray):            
                data = {
                    json_keys['data']:  obj.tolist(),                     
                    json_keys['shape']: obj.shape                
                }
                if 'dtype' in json_keys:
                    data[json_keys['dtype']] = str(obj.dtype)

                return data
            
            if isinstance(obj, np.complex):            
                return {
                    complex_keys['real']:  obj.real, 
                    complex_keys['imag']:  obj.imag, 
                }
                
            return json.JSONEncoder(self, obj)

    return json.dumps(data, cls=NumpyEncoder)

def loads(json_string, json_keys=None, complex_keys=None):
    global _json_keys, _complex_keys
    
    if json_keys is None:
        json_keys = _json_keys

    if complex_keys is None:
        complex_keys = _complex_keys

    def json_numpy_obj_hook(data):
        
        if isinstance(data, dict) and json_keys['data'] in data and json_keys['shape']  in data:
            if 'dtype' in json_keys and json_keys['dtype'] in data:
                dtype = data[json_keys['dtype']]                
            else:
                dtype = np.float
            
            return np.asarray(data[json_keys['data']],  dtype=dtype).reshape(data[json_keys['shape']])
        
        if isinstance(data, dict) and complex_keys['real'] in data and complex_keys['imag']  in data:
            return complex(data[complex_keys['real']], data[complex_keys['imag']])
            
        return data

    return json.loads(json_string, object_hook=json_numpy_obj_hook)
