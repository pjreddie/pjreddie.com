import markdown

def markdown_to_html( markdownText, images ):   
    image_ref = ""

    for image in images:
        image_url = image.image.url
        image_ref = "%s\n[%s]: %s" % ( image_ref, image, image_url )

    md = "%s\n%s" % ( markdownText, image_ref )
    html = markdown.markdown( md )

    return html

