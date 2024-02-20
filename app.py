from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
db = SQLAlchemy(app)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    score = db.Column(db.Integer)

# API endpoints
@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([{'id': player.id, 'name': player.name, 'score': player.score} for player in players])

# Other API endpoints (add_player, update_player, delete_player) go here

# Function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

# Run the app
if __name__ == '__main__':
    create_tables()  # Create tables before running the app
    app.run(debug=True)
