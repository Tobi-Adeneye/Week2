class salesPrediction:
    def projected_amount(self):
        total_sales = int(input("Projected amount of sales for this year: "))
        return total_sales

    def growth_per_year(self, n):
        total_sales = self.projected_amount()
        for x in range(n):
            total_sales += (total_sales * 0.05)
            profit = float(23 / 100 * total_sales)
            profit = round(profit, 2)
            print(profit)


sales = salesPrediction()
sales.growth_per_year(10)
