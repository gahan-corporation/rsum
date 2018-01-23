"""Contact module."""


class Contact(object):
    """Class for contact object export."""

    name = None

    def save(self, name, section, document):
        """Add contact section.

        :param [dict(str, str)] contact:
            Contact section for current document.
        :param object document: Current document.
        :return: Current document with Contact section.
        :rtype: object
        """
        contact = section
        self.name = name
        document = self.start_contact(contact, document)
        print(document)
        return document

    def start_contact(self, contact, document):
        """Start recording contact."""
        paragraph = document.add_paragraph('')
        paragraph.paragraph_format.line_spacing = 0.0
        document.add_paragraph(
            contact.get('title'), style='Heading 3')

        paragraph = document.add_paragraph(
            contact.get('message'), style='Normal')

        paragraph.paragraph_format.space_after = 0
        table = document.add_table(rows=2, cols=6)
        paragraph = table.cell(0, 0).paragraphs[0]
        paragraph.paragraph_format.line_spacing = 0
        table.cell(0, 0).add_paragraph(
            'Website',
            style='Heading 4')
        paragraph = table.cell(0, 0).add_paragraph(
            contact.get('web'),
            style='Heading 5')
        paragraph.paragraph_format.space_before = 0
        paragraph = table.cell(0, 1).paragraphs[0]
        paragraph.paragraph_format.line_spacing = 0
        document = self.complete_contact(contact, document, table)
        return document

    def complete_contact(self, contact, document, table):
        """Complete addition of contact section."""
        print(self.name)
        table.cell(0, 1).add_paragraph(
            'Email',
            style='Heading 4')
        paragraph = table.cell(0, 1).add_paragraph(
            contact.get('email'),
            style='Heading 5')
        paragraph.paragraph_format.space_before = 0
        paragraph = table.cell(1, 0).paragraphs[0]
        paragraph.paragraph_format.line_spacing = 0
        table.cell(1, 0).add_paragraph(
            'Phone',
            style='Heading 4')
        paragraph = table.cell(1, 0).add_paragraph(
            contact.get('phone'),
            style='Heading 5')
        paragraph.paragraph_format.space_before = 0
        paragraph = table.cell(1, 1).paragraphs[0]
        paragraph.paragraph_format.line_spacing = 0
        table.cell(1, 1).add_paragraph('Location', style='Heading 4')
        paragraph = table.cell(1, 1).add_paragraph(
            contact.get('location'),
            style='Heading 5')
        paragraph.paragraph_format.space_before = 0
        return document
