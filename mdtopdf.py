from markdown_pdf import MarkdownPdf, Section


def convertMD(name, text):
    pdf = MarkdownPdf(toc_level=2)

    pdf.add_section(Section(text, toc=False))

    pdf.save(f"{name}.pdf")
