## display a table using ipy_table, but format columns
import numpy as np
import ipy_table
from IPython import display

def show(headers, data_dict, header_names=None, display_table=True):
    
    data_cols = tuple()
    
    if header_names == None:
        header_names = headers
    
    for i in range(len(headers)):
        data_cols = data_cols + tuple([[data_dict[headers[i]]]])
    
    table_data = np.concatenate(data_cols, axis=0).T
    
    ipy_table.make_table([header_names] + table_data.tolist())
    ipy_table.apply_theme('basic')
    
    table_rendered = ipy_table.render()
    
    if display:
        display.display(table_rendered)
    
    return table_rendered