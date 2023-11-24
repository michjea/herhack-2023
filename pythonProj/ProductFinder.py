class ProductFinder:
    def __init__(self, catalogue):
        self.isReplacement = False #wether it's a brand new search, or replacement for existing shopping item
        self.catalogue = catalogue

    def search(self, keyword, category, minPackagingScore, minPackagingScore, minMaterialScore, minProductCircularity, minFishScore):
        #todo

    def findReplacementForProduct(self, oldProduct, sustainabilityCategory):
        keyword = '';
        category = oldProduct.category
        minPackagingScore = None if (sustainabilityCategory is not "packaging") else oldProduct.m_check2_packaging
        minMaterialScore = None if (sustainabilityCategory is not "material") else oldProduct.material_health
        minProductCircularity = None if (sustainabilityCategory is not "circularity") else oldProduct.product_circularity
        minFishScore = None if (sustainabilityCategory is not "fish") else oldProduct.m_check_fish

        results = self.search(keyword, category, minPackagingScore, minPackagingScore, minMaterialScore, minProductCircularity, minFishScore)

        for item in results:
            if item.m_check2_packaging < oldProduct.m_check2_packaging:
                item.inferiorPackaging = True
            if item.material_health < oldProduct.material_health:
                item.inferiorMaterial = True
            if item.product_circularity < oldProduct.product_circularity:
                item.inferiorCircularity = True
            if item.m_check_fish < oldProduct.m_check_fish:
                item.inferiorFish = True

        return results

