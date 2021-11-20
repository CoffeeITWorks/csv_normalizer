from pathlib import Path

def get_file_list(directory, extension='*.csv'):
    """
    return: absolut path list with files found in directory 
    """
    p = Path(directory) # type string
    file_list = [] # type list
    for filename in p.glob(extension):
        file_list.append(filename.resolve())
    
    return file_list
