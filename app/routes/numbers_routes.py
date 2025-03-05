# -*- coding: utf-8 -*-

from flask import Blueprint, request, jsonify
from app.services.numbers_service import sum_numbers, average_numbers

numbers_bp = Blueprint('numbers', __name__)

@numbers_bp.route('/sum', methods=['POST'])
def sum_numbers_route():
    """Endpoint para somar uma lista de numeros."""
    data = request.get_json()
    numbers = data.get('numbers', [])

    if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
        return jsonify({"error": "A lista deve conter apenas numeros."}), 400

    result = sum_numbers(numbers)
    return jsonify({"result": result})

@numbers_bp.route('/average', methods=['POST'])
def average_numbers_route():
    """Endpoint para calcular a média de uma lista de numeros."""
    data = request.get_json()
    numbers = data.get('numbers', [])

    if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
        return jsonify({"error": "A lista deve conter apenas numeros."}), 400
    if len(numbers) == 0:
        return jsonify({"error": "A lista nao pode estar vazia."}), 400

    try:
        result = average_numbers(numbers)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400