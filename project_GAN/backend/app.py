from flask import Flask, render_template, request, redirect, url_for
from database import db_session
from gan_processor import process_image
from models import User, Image, ProcessedImage

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
    flash('No file part', 'error')
    return redirect(request.url)
file = request.files['file']
if file and allowed_file(file.filename):
    # продолжить обработку
else:
    flash('Invalid file format. Please upload a valid image.', 'error')
    return redirect(request.url)

    if file:
        # Сохраняем изображение в БД
        new_image = Image(filename=file.filename)
        db_session.add(new_image)
        db_session.commit()
        return redirect(url_for('home'))

@app.route('/process/<image_id>', methods=['GET'])
def process_image_route(image_id):
    image = Image.query.get(image_id)
    processed_image = process_image(image)
    db_session.add(processed_image)
    db_session.commit()
    return render_template('result.html', image=processed_image)

@app.route('/process', methods=['POST'])
def process_images():
    styles = request.form.getlist('styles')  # список стилей
    image = Image.query.get(request.form['image_id'])
    processed_images = process_image(image, styles)
    # Сохранение обработанных изображений


if __name__ == '__main__':
    app.run(debug=True)
