from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_conn():
    conn = sqlite3.connect("quotes.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/quote", methods=["GET"])
def get_quote():
    category = request.args.get("category")

    if not category:
        return jsonify({"error": "category parameter required"}), 400

    conn = get_conn()

    row = conn.execute(
        "SELECT quote, author, category FROM quotes WHERE category = ? ORDER BY RANDOM() LIMIT 1",
        (category.strip().lower(),)
    ).fetchone()

    conn.close()

    if not row:
        return jsonify({"error": "No quotes found for that category"}), 404

    return jsonify(dict(row))

@app.route("/categories", methods=["GET"])
def get_categories():
    conn = get_conn()

    rows = conn.execute(
        "SELECT DISTINCT category FROM quotes ORDER BY category ASC"
    ).fetchall()

    conn.close()

    categories = [row["category"] for row in rows]

    return jsonify({
        "categories": categories
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004, debug=True)