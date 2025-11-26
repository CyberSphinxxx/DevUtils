import sys
import re

def markdown_to_html(markdown_text):
    """
    Simple Markdown to HTML converter.
    Supports headers, bold, italic, and links.
    """
    html = markdown_text

    # Headers
    html = re.sub(r'^# (.*$)', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*$)', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*$)', r'<h3>\1</h3>', html, flags=re.MULTILINE)

    # Bold
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)

    # Italic
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)

    # Links
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)

    # Paragraphs (simple)
    lines = html.split('\n')
    html_lines = []
    for line in lines:
        if line.strip() and not line.startswith('<'):
            html_lines.append(f'<p>{line}</p>')
        else:
            html_lines.append(line)
    
    return '\n'.join(html_lines)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            md = f.read()
            print(markdown_to_html(md))
    else:
        print("Usage: python markdown_to_html.py <file.md>")
