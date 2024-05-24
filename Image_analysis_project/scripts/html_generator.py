import os

def generate_html(text, image_segments):
    html_content = "<div class='text-content'>"
    html_content += "<h2>Extracted Text</h2>"
    html_content += "<p>" + text.replace("\n", "<br>") + "</p>"
    html_content += "</div>"

    html_content += "<div class='image-content'>"
    html_content += "<h2>Segmented Images</h2>"
    for segment in image_segments:
        html_content += f"<img src='/static/images/{os.path.basename(segment)}' alt='Segmented Image'>"
    html_content += "</div>"

    return html_content
