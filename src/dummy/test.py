import pandas as pd
csv_import = 'business-financial-data-jun-2021-quarter.csv'
csv_import_folder = ''
csv_export_folder = ''
csv_export_headers = ('Series_reference', 'Period', 'ELEE')
# Import csv file
imported_data = pd.read_csv(csv_import)
# Create new dataset only with columns desired, will automatically add missing column in correct order from tuple.
new_data = imported_data.reindex(columns=csv_export_headers)
# Export to .csv file with separator defined and only with data no dataset index
new_data.to_csv(path_or_buf='new_csv.csv', index=False, sep=";")
#Todo:
# Create lib to read tuple, separator, import_folder, export_folder from .ini file [ok]
# Create class or function to be used. []
# Process:
# Read from folder
# Perform the modification of export
# Rename if same export folder or just export with same name to new folder
# End