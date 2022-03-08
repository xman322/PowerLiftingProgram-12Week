from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Note, Maxes
views = Blueprint('views', __name__)

headings = ("name", "role", "salary")
data=(("rolf", "product ownwer", "55k"), ("amy", "eng", "99k"), ("bob", "sec eng", "100k"), ("rolf", "product ownwer", "55k"), ("amy", "eng", "99k"), ("bob", "sec eng", "100k"))

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
   
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')
           
    return render_template("home.html" , user=current_user, headings = headings, data = data)



@views.route('/StartHere', methods=['GET', 'POST'] )
@login_required
def starthere():
    
    if request.method == 'POST':
        benchmax = request.form.get('benchmax')
        squatmax = request.form.get('squatmax')
        deadmax = request.form.get('deadmax')
        psquatmax = request.form.get('psquatmax')
        pdeadmax = request.form.get('pdeadmax')

        new_max = Maxes(benchmax = benchmax, squatmax = squatmax, deadmax = deadmax, pdeadmax= pdeadmax, psquatmax=psquatmax, user_id = current_user.id)
        db.session.add(new_max)
        db.session.commit()
        return redirect(url_for('views.home'))

    return render_template("starthere.html", user=current_user)
  