# CSV Normalizer main class
import pandas as pd

class Csv_Normalizer:
    def __init__(self, config_dict) -> None:
        """
        :param: config_dict
        {
            'csv_import_folder': '/path/import/folder',
            'csv_export_folder': '/path/export/folder',
            # Export headers you want, those missing in the import will be added 
            # with empty data.
            'csv_export_headers': ('Series_reference', 'Period', 'ELEE'),
            # delimiter only affects the output file.
            'csv_delimiter': ';',
            # Options: https://docs.python.org/3.5/library/codecs.html#text-encodings
            # use mbcs for ansi on python prior 3.6
            'csv_encoding': 'utf-8',
        }

        """
        self.csv_import_folder = config_dict.get('csv_import_folder')
        self.csv_export_folder = config_dict.get('csv_export_folder')
        self.csv_export_headers = config_dict.get('csv_export_headers')
        self.csv_delimiter = config_dict.get('csv_delimiter', ";")
        self.csv_encoding = config_dict.get('csv_encoding', "utf-8")

    @staticmethod
    def _import_file(file):
        """
        Read the .csv file and return pandas Dataset.
        """
        imported_data = pd.read_csv(file)
        return imported_data
    
    def _normalize_data(self, dataset):
        """
        input: dataset to normlize
        return: normalized dataset with only columns desired in csv_export_headers
        """
        new_data = dataset.reindex(columns=self.csv_export_headers)
        return new_data
    
    def _export_csv(self, dataset, file):
        """
        input: dataset to export to csv
        return: True: No errors
                False: Failed to export
        """
        export_succeed = True # type: bool
        try:
            dataset.to_csv(path_or_buf=file, index=False, sep=self.csv_delimiter, encoding=self.csv_encoding)
        except:
            export_succeed = False
        
        return export_succeed

    @staticmethod
    def run(self):
        """
        TODO: Create the method
        run the process, 
            - scan the directory for .csv files
            - For each file:
                - read and Normalize the columns
                - export to the desired directory the .csv resultant file
                - rename old to _normalized?
        """

        # Get the list of the files
        #iterate over each file
        # normalize

        # export

        # resume?
        pass
