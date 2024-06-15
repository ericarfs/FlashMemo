from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
app.app_context().push()

class FlashCard(db.Model):
    id           = db.Column(db.String(200), primary_key=True)
    expression   = db.Column(db.String(200), nullable=False)
    meaning      = db.Column(db.String(200), nullable=False)
    example      = db.Column(db.String(200), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self):
        return '<FlashCard %r> % self.id'


@app.route('/', methods=['POST', 'GET'])
def index():
    cards = FlashCard.query.order_by(FlashCard.date_created).all()
    return render_template('index.html', cards=cards)

@app.route('/new_card', methods=['POST', 'GET'])
def new_card():
    card_error = ""
    if request.method == 'POST':
        card_expression = request.form['expression']
        card_meaning = request.form['meaning']
        card_example = request.form['example']

        card_id = uuid.UUID(str(uuid.uuid4())).hex
        new_card = FlashCard(id = card_id, expression=card_expression, meaning=card_meaning, example =card_example)
            
        try:
            db.session.add(new_card)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your card'
    else:
        return render_template('new_card.html', card_error="")


@app.route('/delete/<id>')
def delete(id):
    card_to_delete = FlashCard.query.get_or_404(id)
    try:
        db.session.delete(card_to_delete)
        db.session.commit()
        return redirect('/')
    except:
       return 'There was an issue deleting that task'



@app.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    card = FlashCard.query.get_or_404(id)
    if request.method == 'POST':
        card.expression = request.form['expression']
        card.meaning = request.form['meaning']
        card.example = request.form['example']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
           return 'There was an issue updating that card'
    else:
        return render_template('update.html', card=card)


if __name__ == "__main__":
    app.run(debug = True)