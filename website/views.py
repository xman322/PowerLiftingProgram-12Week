from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Note, Maxes
views = Blueprint('views', __name__)

headings = ("Day 1", "Sets", "Reps", "Weight", "RPE")
data=(("rolf", "product ownwer", "55k","5"), ("amy", "eng", "99k","5"), ("bob", "sec eng", "100k","5"), ("rolf", "product ownwer", "55k","5"))
totals = []


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
   
    return render_template("home.html" , user=current_user, headings = headings, data = data, entries=totals)



@views.route('/StartHere', methods=['GET', 'POST'] )
@login_required
def starthere():
    
    if request.method == 'POST':
        totals.append(float(request.form.get('benchmax')))
        totals.append(float(request.form.get('squatmax')))
        totals.append(float(request.form.get('deadmax')))
        totals.append(float(request.form.get('psquatmax')))
        totals.append(float(request.form.get('pdeadmax')))
        """


        
        totals.append(
            (
            float(request.form.get('benchmax')),
            float(request.form.get('squatmax')),
            float(request.form.get('deadmax')),
            float(request.form.get('psquatmax')),
            float(request.form.get('pdeadmax'))
            )
        )
        
        benchmax = request.form.get('benchmax')
        squatmax = request.form.get('squatmax')
        deadmax = request.form.get('deadmax')
        psquatmax = request.form.get('psquatmax')
        pdeadmax = request.form.get('pdeadmax')

        new_max = Maxes(benchmax = benchmax, squatmax = squatmax, deadmax = deadmax, pdeadmax= pdeadmax, psquatmax=psquatmax, user_id = current_user.id)
        db.session.add(new_max)
        db.session.commit()
        """
        return redirect(url_for('views.home'))

    return render_template("starthere.html", user=current_user)
  