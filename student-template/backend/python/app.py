from flask import Flask, jsonify
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Configure database connection using os.getenv('DATABASE_URL')
DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    # Establish connection to PostgreSQL using the DATABASE_URL environment variable
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)

@app.route('/api/inventory/alerts', methods=['GET'])
def get_alerts():
    """
    1. Connect to the database.
    2. Query 'inventory' table where quantity <= reorder_level.
    3. Return JSON list of products.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Query products where quantity <= reorder_level
        cur.execute("SELECT id, product_name, quantity, reorder_level FROM inventory WHERE quantity <= reorder_level;")
        rows = cur.fetchall()
        
        cur.close()
        conn.close()
        
        # Format rows into the expected JSON structure (ensuring UUID is cast to string)
        result = [{
            "id": str(row["id"]),
            "product_name": row["product_name"],
            "quantity": row["quantity"],
            "reorder_level": row["reorder_level"]
        } for row in rows]
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
