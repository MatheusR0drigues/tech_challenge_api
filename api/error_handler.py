from flask import jsonify

def handle_error(e):
    if hasattr(e, 'code'):  # Erros HTTP padrão
        response = jsonify({"error": str(e.description)})
        response.status_code = e.code
    else:
        response = jsonify({"error": "Ocorreu um erro interno no servidor."})
        response.status_code = 500
    return response

def register_error_handlers(app):
    app.register_error_handler(404, handle_error)
    app.register_error_handler(400, handle_error)
    app.register_error_handler(500, handle_error)
