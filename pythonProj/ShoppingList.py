from ProductFinder import ProductFinder

class ShoppingList:
    def __init__(self):
        self.products = []

    def addProduct(self, product):
        self.products.append(product)

    def replaceProduct(self, productOld, productNew, category):
        productNew = ProductFinder.findReplacementForProduct(productOld, category)[0] #todo: oversimplified. Pretends the user doesn't need to choose one
        self.products.pop(productOld)
        self.products.append(productNew)

    def showSustainabilityScores(self, product):
        return { product.id, product.getSustainability() }

