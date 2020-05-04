from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import unittest
from flask import current_app
import turtle
win = turtle.Screen()
win.title("Turtle")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
bootstrap = Bootstrap(app)


class FileName(FlaskForm):
    filename = StringField('Enter the file name?', validators=[DataRequired()])
    submit = SubmitField('Submit and Open Turtle Graphics Window')


@app.route('/', methods=['GET', 'POST'])
def index():
    filename = None
    form = FileName()
    visited = []
    repeated = []
    if form.validate_on_submit():
        filename = form.filename.data


        a = open(filename, 'r').read()
        # a = 'FFFLFFLLF'
        turtle.left(90)
        for i in a:
            if (i == 'L'):
                turtle.left(90)
            elif (i == 'F'):
                turtle.forward(5)
            else:
                turtle.right(90)
            if ([int(turtle.position()[0] / 5), int(turtle.position()[1] / 5)] not in visited and i == 'F'):
                visited.append([int(turtle.position()[0] / 5), int(turtle.position()[1] / 5)])
            elif ([int(turtle.position()[0] / 5), int(turtle.position()[1] / 5)] in visited and i == 'F'):
                repeated.append([int(turtle.position()[0] / 5), int(turtle.position()[1] / 5)])

        set(tuple(element) for element in repeated)
        tom=turtle.Turtle()
        tom.setposition([int(turtle.position()[0] / 5), int(turtle.position()[1] / 5)])
        p=tom.pos()
        tom.write(str(p),True)
    return render_template('base.html', form=form, name=filename,final_pos=[int(turtle.position()[0] / 5), int(turtle.position()[1] / 5)],repeated_position=repeated)


if __name__ == '__main__':

    manager.run()
