from pathlib import Path

def get_file_list(directory, extension='*.csv'):
    """
    return: files list found in directory using absolut path 
    """
    p = Path(directory) # type string
    file_list = [] # type list
    for filename in p.glob(extension):
        file_list.append(str(filename.resolve()))
    
    return file_list
