from flask import Flask, render_template
from db import db
from routes import student_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(student_bp)

with app.app_context():
    db.create_all()

@app.route('/test')
def test():
    return render_template("add_student.html")

if __name__ == "__main__":
    app.run(debug=True)