from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="nextra_plus"
)
cursor = db.cursor(dictionary=True)

# Get all designations
@app.route("/designations", methods=["GET"])
def get_designations():
    cursor.execute("SELECT * FROM designations ORDER BY rank ASC")
    return jsonify(cursor.fetchall())

# Add designation
@app.route("/designations", methods=["POST"])
def add_designation():
    data = request.json
    cursor.execute("INSERT INTO designations (rank, designation) VALUES (%s, %s)",
                   (data["rank"], data["designation"]))
    db.commit()
    return jsonify({"message": "Designation added!"}), 201

# Update designation
@app.route("/designations/<int:id>", methods=["PUT"])
def update_designation(id):
    data = request.json
    cursor.execute("UPDATE designations SET rank=%s, designation=%s WHERE id=%s",
                   (data["rank"], data["designation"], id))
    db.commit()
    return jsonify({"message": "Designation updated!"})

# Delete designation
@app.route("/designations/<int:id>", methods=["DELETE"])
def delete_designation(id):
    cursor.execute("DELETE FROM designations WHERE id=%s", (id,))
    db.commit()
    return jsonify({"message": "Designation deleted!"})

if __name__ == "__main__":
    app.run(debug=True)
