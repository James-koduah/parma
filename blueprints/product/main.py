from blueprints.product import product
from flask import Flask, render_template, request, redirect, jsonify
from __main__ import control, auth_user


@product.route('/package', strict_slashes=False)
def product_package():
    user = auth_user()
    if user == False:
        return redirect('/')
    return render_template('product/app_package/app_package.html', user=user)


