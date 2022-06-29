"""
Title: Test Harness
Desc: A Module to test the Modules
Change Log: (Who, When, What)
NToulas, 2022-Jun-28, Created file
"""

import ProcessingClasses as PC
import IOClasses as IO

lstOfCDObjects = []
file_name = 'TestData.txt'

while True:
    IO.ScreenIO.print_menu()
    user_input = IO.ScreenIO.menu_choice()

    if user_input == 'l':
        IO.FileIO.load_inventory(file_name)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
    if user_input == 'a':
        cd = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(cd, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
    if user_input == 'i':
        IO.ScreenIO.show_inventory(lstOfCDObjects)

    if user_input == 's':
        IO.FileIO.save_inventory(file_name, lstOfCDObjects)

    if user_input == 'x':
        break

# print('\n\nTesting CD class')
# print(DC.CD.__doc__)
# cd1 = DC.CD(1, 'test_title', 'cd_artist')
# print(cd1)
# lstOfCDObjects.append(cd1)
#
# print('\n\nTesting of class FileIO')
# file_name = 'TestData.txt'
# IO.FileIO.save_inventory(file_name, lstOfCDObjects)
# print(IO.FileIO.load_inventory(file_name))
#
# print('\n\nTesting IO class')
# IO.ScreenIO.print_menu()
# print('selection in menu: {}'.format(IO.ScreenIO.menu_choice()))
# print('Inventory:')
# IO.ScreenIO.show_inventory(lstOfCDObjects)
# cd2 = DC.CD(2, 'test_title_2', 'cd_artist_2')
# lstOfCDObjects.append(cd2)
# print('Inventory:')
# for item in lstOfCDObjects:
#     print(item)
#
# print('\n\nTesting Processing Classes')
# PC.DataProcessor.add_CD((3, 'Foreigner', 'Foreigner'), lstOfCDObjects)
# print('Inventory:')
# for item in lstOfCDObjects:
#     print(item)