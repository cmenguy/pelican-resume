'''
resume
==============================================================================
This plugin generates a PDF resume from a Markdown file using customizable CSS
'''

import os
import logging
import tempfile

from subprocess import Popen

from pelican import signals

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CSS_DIR = os.path.join(CURRENT_DIR, "static", "css")

logger = logging.getLogger(__name__)

def set_default_settings(settings):
    settings.setdefault("RESUME_SRC", "pages/resume.md")
    settings.setdefault("RESUME_PDF", "pdfs/resume.pdf")
    settings.setdefault("RESUME_CSS_DIR", CSS_DIR)
    settings.setdefault("RESUME_TYPE", "moderncv")
    settings.setdefault("RESUME_PANDOC", "pandoc")
    settings.setdefault("RESUME_WKHTMLTOPDF", "wkhtmltopdf")

def init_default_config(pelican):
    from pelican.settings import DEFAULT_CONFIG
    set_default_settings(DEFAULT_CONFIG)
    if (pelican):
        set_default_settings(pelican.settings)

def generate_pdf_resume(generator):
    path = generator.path
    output_path = generator.settings.get("OUTPUT_PATH")
    markdown = os.path.join(path, generator.settings.get("RESUME_SRC"))
    css_type = generator.settings.get("RESUME_TYPE")
    css = os.path.join(generator.settings.get("RESUME_CSS_DIR"), "%s.css" % css_type)
    if not os.path.exists(markdown):
        logging.critical("Markdown resume not found under %s" % markdown)
        return
    if css and not os.path.exists(os.path.join(path, css)):
        logging.warn("Resume CSS not found under %s, CSS will be ignored" % css)
    css = os.path.join(path, css) if css else css

    with tempfile.NamedTemporaryFile(suffix=".html") as html_output:
        pdf_output = os.path.join(output_path, generator.settings.get("RESUME_PDF"))
        pdf_dir = os.path.dirname(pdf_output)
        if not os.path.exists(pdf_dir):
            os.makedirs(pdf_dir)
        pandoc = generator.settings.get("RESUME_PANDOC")
        wkhtmltopdf = generator.settings.get("RESUME_WKHTMLTOPDF")

        html_cmd = "%s --standalone " % pandoc
        if css:
            html_cmd += "-c %s " % css
        html_cmd += "--from markdown --to html -o %s %s" % (html_output.name, markdown)
        Popen(html_cmd, shell=True).wait()
        pdf_cmd = "%s %s %s" % (wkhtmltopdf, html_output.name, pdf_output)
        Popen(pdf_cmd, shell=True).wait()

def register():
    signals.initialized.connect(init_default_config)
    signals.article_generator_finalized.connect(generate_pdf_resume)