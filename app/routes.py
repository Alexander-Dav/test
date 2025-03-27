from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_required, current_user
from datetime import datetime
import time

@app.route('/test/<int:test_id>')
@login_required
def view_test(test_id):
    test = Test.query.get_or_404(test_id)
    if not test.is_active:
        abort(403)
    session['test_start'] = time.time()
    return render_template('test/view.html', test=test)

@app.route('/submit-test/<int:test_id>', methods=['POST'])
def submit_test(test_id):
    test = Test.query.get_or_404(test_id)
    time_spent = int(time.time() - session.get('test_start', 0))
    
    if test.timer_enabled and time_spent > test.timer_seconds:
        flash('Время вышло!', 'danger')
        return redirect(url_for('test_result', test_id=test_id))
    
    score = calculate_score(request.form, test)
    save_result(test_id, current_user.id, score, time_spent)
    
    return redirect(url_for('test_result', test_id=test_id))

def calculate_score(form, test):
    correct = 0
    for q in test.questions:
        if form.get(f'q_{q.id}') == q.correct_answer:
            correct += 1
    return (correct / len(test.questions)) * 100