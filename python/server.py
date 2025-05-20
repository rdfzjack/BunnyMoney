from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/bunny/update', methods=['POST'])
def update_bunny():
    data = request.json
    token_id = str(data.get("token_id"))
    new_status = data.get("status")

    file_path = f"metadata/{token_id}.json"

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    with open(file_path, "r") as f:
        metadata = json.load(f)

    if new_status == "dead":
        metadata["name"] = f"Bunny #{token_id} (DEAD)"
        metadata["image"] = "https://yourdomain.com/static/dead.gif"
        metadata["description"] = "This bunny has died in battle."

    with open(file_path, "w") as f:
        json.dump(metadata, f, indent=4)

    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
