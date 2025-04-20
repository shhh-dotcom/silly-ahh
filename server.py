from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session handling

@app.route('/')
def home():
    return render_template('index.html', background_color="black")

@app.route('/play', methods=['GET', 'POST'])
def play():
    if 'randomnum' not in session:
        reset_game()
    
    if request.method == 'POST':
        guess = request.form.get('guess')
        if guess:
            guess = [int(num) for num in guess.split()]
            return bro_plays(guess)
    
    return render_template('play.html', message="Enter your first guess", background_color="black")

def bro_plays(guess):
    randomnum = session.get('randomnum', [])
    tries = session.get('tries', 4) - 1
    moons = session.get('moons', 0)
    stars = session.get('stars', 0)
    feedback = []
    randomnum2 = []
    
    for i, (a, b) in enumerate(zip(randomnum, guess)):
        if a == b:
            feedback.append(f'<span style="color:lightgreen;">{a} and {b} match at index {i} - You get 1 star!</span>')
            stars += 1
        elif a in guess:
            feedback.append(f'<span style="color:yellow;">{a} is correct but in a different index - You get 1 moon!</span>')
            moons += 1
        else:
            randomnum2.append(a)
    
    session['randomnum'] = randomnum2
    session['tries'] = tries
    session['moons'] = moons
    session['stars'] = stars
    
    if not randomnum2:
        final_message = f'<span style="color:lightgreen;">You won!</span><br>Stars: {stars} | Moons: {moons}<br>Mysterious Number: {session.get("mysterious_number", [])}'
        reset_game()
        return render_template('play.html', message=final_message, background_color="black", game_over=True)
    elif tries == 0:
        final_message = f'<span style="color:red;">You lose!</span><br>Stars: {stars} | Moons: {moons}<br>Mysterious Number: {session.get("mysterious_number", [])}'
        reset_game()
        return render_template('play.html', message=final_message, background_color="black", game_over=True)
    else:
        return render_template('play.html', message=f'<span style="color:cyan;">{tries} tries left!</span>', feedback=feedback, background_color="black")

def reset_game():
    session.clear()
    session['randomnum'] = random.sample(range(1, 21), 4)
    session['tries'] = 4
    session['moons'] = 0
    session['stars'] = 0
    session['mysterious_number'] = session['randomnum'][:]

if __name__ == '__main__':
    app.run(debug=True)
