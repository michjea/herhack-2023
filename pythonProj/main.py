# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd

catalogue = pd.DataFrame  #todo: JsonImporter.importData()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def getProductById(productnumber):
    return catalogue.filter(id=productnumber)

def getSustainability(product):
    return { product.m_check2_packaging,
     product.dimension_circularity.material_health,
     product.dimension_circularity.product_circularity,
     product.m_check_fish }



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
