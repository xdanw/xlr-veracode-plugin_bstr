#
# Copyright 2020 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import json
import shutil
import tempfile

from veracode.HttpRequest import HttpRequest

if not veracodeServer:
  raise Exception("Veracode server must be provided")

if not build_id:
  raise Exception("Veracode build id must be provided")


pdfFilename = "veracode-detailed-report-%s.pdf" % build_id

params = {
    'url': veracodeServer['url'],
    'username': veracodeServer['username'],
    'password': veracodeServer['password'],
    'proxyHost': veracodeServer['proxyHost'],
    'proxyPort': veracodeServer['proxyPort'],
    'proxyUsername': veracodeServer['proxyUsername'],
    'proxyPassword': veracodeServer['proxyPassword']
}

status, result, headers = HttpRequest(params).get_file('/api/4.0/detailedreportpdf.do?build_id=%s' % build_id, contentType='application/pdf')

if status != 200:
    raise Exception(
        "Failed to connect to Veracode Server. Status: %s" % status
    )

taskApi.addAttachment(getCurrentTask().id, pdfFilename, result)
