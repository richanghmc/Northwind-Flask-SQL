from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route("/")
def suppliers():
    suppliers = database.get_all_suppliers()
    return render_template('index.html', suppliers=suppliers)


@app.route("/suppliers/<int:supplier_id>")
def products(supplier_id):
    products = database.get_supplier_products(supplier_id)
    supplier_name = database.get_supplier_productName(supplier_id)
    supplier_name = supplier_name[0]["CompanyName"]
    return render_template('products.html', products=products, name=supplier_name)

@app.route("/categories")
def categories():
    categories = database.categoryProductCount()
    return render_template('categories.html', categories=categories)

@app.route("/categories/<int:category_id>")
def productsInCategory(category_id):
    products = database.get_category_products(category_id)
    categoryName = database.get_category(category_id)[0]['CategoryName']
    return render_template('category.html', products=products, name=categoryName)