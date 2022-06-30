from flask import render_template, Blueprint, request

new_post_blueprint = Blueprint('new_post_blueprint', __name__, template_folder='templates')


@new_post_blueprint.route('/post')
def page_post_form():
    return render_template('post_form.html',)


@new_post_blueprint.route("/post", methods=["GET", "POST"])
def page_post_upload():
    img = request.files.get('picture')
    text = request.values.get('text')
    return render_template('post_uploaded.html',
                           img=img,
                           text=text)