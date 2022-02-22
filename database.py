import sqlite3

def query(query_text, *param):
    conn = sqlite3.connect('Northwind_large.sqlite')
    cur = conn.cursor()
    cur.execute(query_text, param)

    column_names = []
    for column in cur.description:
        column_names.append(column[0])

    rows = cur.fetchall()
    dicts = []

    for row in rows:
        d = dict(zip(column_names, row))
        dicts.append(d)

    conn.close()
    return dicts

def get_all_suppliers():
    return query("""SELECT COUNT( Product.Id) AS ProductCount, Supplier.*
                    FROM Product
                    Inner JOIN Supplier
		ON Product.SupplierId = Supplier.Id
	
GROUP BY CompanyName
""")

def get_supplier_products(supplier_id):
    return query("""
    SELECT Product.ProductName, Product.QuantityPerUnit, Product.UnitPrice, Supplier.CompanyName, Category.CategoryName
    FROM Product
    Inner JOIN Supplier
		ON Product.SupplierId = Supplier.Id
		
    INNER JOIN Category
		ON Product.CategoryId = Category.Id
		
    WHERE SupplierId = ?""" , supplier_id)

def get_supplier_productName(supplier_id):
    return query("""SELECT CompanyName FROM Supplier 
                    WHERE Id= ?""" , supplier_id)
                    
def categoryProductCount():
    return query(""" 
    SELECT Category.CategoryName, Category.Description, COUNT(Category.Id) as ProductCount
    FROM Category
    INNER JOIN Product
	    ON Product.CategoryId = Category.Id
	
    GROUP BY CategoryName
    """)