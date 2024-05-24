from flask import render_template, request
from app import app
from scripts.text_extraction import extract_text
from scripts.visual_segmentation import segment_image
from scripts.html_generator import generate_html
import os

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)

            text = extract_text(file_path)
            image_segments = segment_image(file_path)
            html_content = generate_html(text, image_segments)

            return render_template('index.html', content=html_content)
    return render_template('index.html', content='')
