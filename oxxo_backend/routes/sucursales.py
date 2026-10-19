from flask import Blueprint, request, jsonify
from database.mongo import db

sucursales_bp = Blueprint('sucursales', __name__)

@sucursales_bp.route('/api/sucursales', methods=['POST'])
def add_sucursal():
    data = request.json
    db.sucursales.insert_one(data)
    return jsonify({"message": "Sucursal registrada con éxito"}), 201

@sucursales_bp.route('/api/sucursales', methods=['GET'])
def get_sucursales():
    # Retorna todas las sucursales omitiendo el _id de mongo para evitar errores de serialización
    sucursales = list(db.sucursales.find({}, {"_id": 0}))
    return jsonify(sucursales), 200