"""
Title: Processing Classes
Desc: A Module for processing Classes
Change Log: (Who, When, What)
NToulas, 2022-Jun-28, Created file
"""

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDInfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of CD Objects): 2D data structure (list of CD Objects) that holds the data during runtime

        Returns:
            None.

        """
        cdId, title, artist = CDInfo
        cdId = int(cdId)
        row = DC.CD(cdId, title, artist)
        table.append(row)