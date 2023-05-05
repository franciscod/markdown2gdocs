import fileinput
import sys

import goog
from goog import reqs_clear_doc, reqs_for_text, reqs_for_heading_style


def md_to_reqs(md_lines, si=1):
    for line in md_lines:
        if line.strip() == "":
            continue

        style_reqs = []
        sigils, _sep, rest = line.partition(" ")
        if sigils in ("#", "##"):
            line = rest
            style_reqs = reqs_for_heading_style(si, line, len(sigils))

        yield from reqs_for_text(si, line)
        yield from style_reqs
        si += len(line)


def replace_doc_with_md(service, doc, md):
    reqs = [*reqs_clear_doc(doc), *md_to_reqs(md)]
    goog.do_batchupdate(service, doc, reqs)


def main():
    document_id = sys.argv[1]
    del sys.argv[1]  # let fileinput take the next arg

    service = goog.get_service()
    doc = goog.get_doc(service, document_id)

    md = fileinput.input()
    replace_doc_with_md(service, doc, md)


if __name__ == "__main__":
    main()
