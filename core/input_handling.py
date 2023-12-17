from flask import Flask, request, jsonify
from core.execution import Executor


app = Flask(__name__)

class InputHandler:

    def run(self):
        app.run(host='0.0.0.0', port=5000)

    @app.route('/', methods=["POST"])
    def handle_input():     
        try:
            executor = Executor()
            data = request.json.get("data")
            if data is None:
                raise ValueError("Data is missing.")
            elements, subset_number = data["elements"], data["subset_number"]
            subset_1, subset_2 = executor.execute_cumu(elements, subset_number)
            
            result = {
                "subset_1": subset_1,
                "subset_2": subset_2
            }
            
            return jsonify({'result': result})
        except Exception as e:
            return jsonify({'error': str(e)}), 400