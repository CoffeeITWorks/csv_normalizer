***************
Example config:
***************

.. code-block::

    [common]
    csv_import_folder = C:/temp/csv_import
    csv_export_folder = C:/temp/csv_export
    csv_export_headers = 'Series_reference', 'Period', 'ELEE'
    csv_delimiter = ;
    csv_encoding = utf-8

*****
Usage
*****

.. code-block::

    usage: csv_normalizer [-h] [-c [CONFIG_INI]] [--version [VERSION]] [--no_rename [NO_RENAME_OLD]] [--write_config]

    optional arguments:
    -h, --help            show this help message and exit
    -c [CONFIG_INI],      --config_ini [CONFIG_INI]
                          csv_normalizer ini configuration file
    --version [VERSION]   Print version and exit
    --no_rename [NO_RENAME_OLD]
                          Do not rename to .old the original file
    --write_config        Write configuration with default values, useful to get a config file to modify

*******
Install
*******

.. code-block::

    pip install --user csv_normalizer

    or for root account

    pip install --user csv_normalizer

****
Info
****

This is just a simple script that ensures all your .csv files have always same columns and in the same order. Probably
one of the most common issues with .csv files: 

* Some system doesn't respects the columns orders
* Some system doesn't adds a column when there is no data for such column

The script/program resolves both cases in a simple way, process:

.. uml::

    @startuml
    title Normalize csv process 

    start

    :Get list of .csv files in a directory (import_folder);
    repeat
      :normalize content;
      :rename old by default;
      :export normalized to export_folder;
    repeat while (for each file)
    :return dict with result;

    stop

    @enduml

Normalize: ensure order of columns is always same, add missing columns with empty data.

Returns always a dict/json like, with the 'ok' or 'fail' list of processed files.
examples:

.. code-block::

    {'failed': [],
    'ok': [
        {'export_path': 'C:\\temp\\csv_export\\business-financial-data-jun-2021-quarter.csv',
         'import_path': 'C:\\temp\\csv_import\\business-financial-data-jun-2021-quarter.csv'}
         ]
    }
    
    # Example when nothing was processed:
    {'failed': [],
    'ok': []}

Author: Pablo Estigarribia <pablodav at gmail dot com>
Project site: https://github.com/CoffeeITWorks/csv_normalizer
