#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Views for the export app."""
import os
from io import StringIO

from django.http import HttpResponse

from export.models import ExportDocument


def index(request):
    """Export cv to word document.

    :param request: HttpRequest object for export_docx page.
    :type request: object
    :return: Word document generated by export module.
    :rtype: object
    """
    document = ExportDocument().export_word(1)

    # Special thanks to: https://stackoverflow.com/a/24122313
    print(request)

    target_stream = StringIO()
    document.document.save(target_stream)
    length = target_stream.tell()
    target_stream.seek(0)
    response = HttpResponse(
        target_stream.getvalue(),
        content_type=(
            "application/vnd.openxmlformats-officedocument."
            "wordprocessingml.document"
        )
    )
    response['Content-Disposition'] = (
        'attachment; filename={0}-cv.docx'.format(os.environ.get('RSUM_ENV'))
    )
    response['Content-Length'] = length
    return response
