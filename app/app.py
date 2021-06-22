from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route('/',methods=['POST', 'GET'])

def index():
    if request.method == 'POST':
        add_data = request.form['content']
        new_task = Todo(content=add_data)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "Error"
    else:
        tasks = Todo.query.order_by(Todo.create_at).all()
        return render_template('index.html',tasks=tasks)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id        


if __name__ == "__main__":
    app.run(debug=False)