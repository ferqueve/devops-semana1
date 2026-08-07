from flask import Flask, jsonify, request

app = Flask(__name__)

pokemons = []

@app.route("/")
def inicio():
    return "API Pokemon funcionando"

@app.route("/pokemons", methods=["GET"])
def obtener_pokemons():
    return jsonify(pokemons)

@app.route("/pokemons", methods=["POST"])
def crear_pokemon():
    nuevo_pokemon = request.get_json()

    pokemons.append(nuevo_pokemon)

    return jsonify({
        "mensaje": "Pokemon creado correctamente",
        "pokemon": nuevo_pokemon
    }), 201

@app.route("/pokemons/<int:id>", methods=["GET"])
def obtener_pokemon(id):
    for pokemon in pokemons:
        if pokemon["id"] == id:
            return jsonify(pokemon)

    return jsonify({"mensaje": "Pokemon no encontrado"}), 404

@app.route("/pokemons/<int:id>", methods=["PUT"])
def actualizar_pokemon(id):
    datos = request.get_json(silent=True) #Nos aseguramos que el JSON recibido sea válido
    if datos is None or not isinstance(datos, dict):
        return jsonify({"error":"Debe enviarse un JSON válido"}), 400
    
    for pokemon in pokemons:
        if pokemon["id"] == id:
            datos.pop("id", None) #Evito que me cambien el id del pokémon
            pokemon.update(datos)
            return jsonify({
                "mensaje": "Pokemon actualizado",
                "pokemon": pokemon
            })

    return jsonify({"mensaje": "Pokemon no encontrado"}), 404

@app.route("/pokemons/<int:id>", methods=["DELETE"])
def eliminar_pokemon(id):
    for pokemon in pokemons:
        if pokemon["id"] == id:
            pokemons.remove(pokemon)
            return jsonify({
                "mensaje": "Pokemon eliminado"
            })

    return jsonify({"mensaje": "Pokemon no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)