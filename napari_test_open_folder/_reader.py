import numpy as np
from pathlib import Path

def napari_get_reader(path):
    if Path(path).glob("somefile.txt"):
        return reader_function
    return

def reader_function(path):
    print(list(Path(path).iterdir()))
    return [(np.random.rand(10, 10),)]
