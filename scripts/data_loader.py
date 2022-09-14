import pandas as pd;

# list of possible na_values
missing_values = ["n/a", "na", 'none', "-", "--", None, '?']


def load_data_from_xsl(filepath: str, na_values: list = []) -> pd.DataFrame:
        """
            A  function which returns a dataframe from a specified .xslx file
            Parameters
            ----------
            filepath:
                Type: str
            na_values:
                Type: list
                Default value = []
            Returns
            -------
            pd.DataFrame
        """
        try:
            na_values.extend(na_values)
            df = pd.read_excel(filepath, na_values=na_values, engine='openpyxl')

            return df
        except:
            print("Error:\n\tCould not find specified .xslx file")