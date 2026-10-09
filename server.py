try:
    # try to import flask, or return error if has not been installed
    from flask import Flask
    from flask import redirect
    from flask import send_from_directory
    from flask import url_for
except ImportError:
    print("You don't have Flask installed, run `$ pip3 install flask` and try again")
    exit(1)

import os

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), './')
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 #disable cache

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def serve_home():
    return send_from_directory(static_file_dir, 'home.html')


@app.route('/catalog', methods=['GET'])
def serve_catalog():
    return send_from_directory(static_file_dir, 'catalog_page/catalog.html')


@app.route('/product', methods=['GET'])
def serve_product():
    return send_from_directory(static_file_dir, 'product_view.html')


@app.route('/cart', methods=['GET'])
def serve_cart():
    return send_from_directory(static_file_dir, 'cart/index.html')


@app.route('/payment', methods=['GET'])
def serve_payment():
    return send_from_directory(static_file_dir, 'PaymentForm.html')


@app.route('/home.html', methods=['GET'])
def redirect_home_html():
    return redirect(url_for('serve_home'), code=301)


@app.route('/catalog_page/catalog.html', methods=['GET'])
def redirect_catalog_html():
    return redirect(url_for('serve_catalog'), code=301)


@app.route('/product_view.html', methods=['GET'])
def redirect_product_html():
    return redirect(url_for('serve_product'), code=301)


@app.route('/cart/index.html', methods=['GET'])
def redirect_cart_html():
    return redirect(url_for('serve_cart'), code=301)


@app.route('/PaymentForm.html', methods=['GET'])
def redirect_payment_html():
    return redirect(url_for('serve_payment'), code=301)

# Serving any other image
@app.route('/<path:path>', methods=['GET'])
def serve_any_other_file(path):
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = os.path.join(path, 'index.html')
    response = send_from_directory(static_file_dir, path)
    response.cache_control.max_age = 0 # avoid cache memory
    return response

app.run(host='0.0.0.0',port=3000, debug=True, extra_files=['./',])
