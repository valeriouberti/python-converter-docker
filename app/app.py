import json
import logging

from flask import (
    Flask, request, jsonify, render_template
)


from .converter import CurrencyConverter


def create_app(additional_modules=None):
    """Initializes the Flask app."""
    app = Flask(__name__)
    app.config.from_object('app.config')

    app.secret_key = app.config.get("SECRET_KEY")



    @app.route('/convert/<reference_date>/<float:current_amount>/<src_currency>/<dest_currency>')
    def converter(reference_date, src_currency, current_amount, dest_currency  ):

        amount = CurrencyConverter.convert_amount(reference_date=reference_date, amount=current_amount,
                                             src_currency=src_currency, dest_currency=dest_currency)

        resp = jsonify({
            "amount": amount,
            "currency": dest_currency,
        })

        return resp

    return app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
