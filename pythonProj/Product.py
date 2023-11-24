class Product:
    def __init__(self, id, desc):
        self.id = id
        self.desc = desc

    def getSustainability(self):
        return { self.m_check2_packaging,
         self.dimension_circularity.material_health,
         self.dimension_circularity.product_circularity,
         self.m_check_fish }

    def getSustainablitySummary(self): #for icon in shopping list
        return (self.m_check2_packaging + self.dimension_circularity.material_health + self.dimension_circularity.product_circularity + self.m_check_fish) / 4
