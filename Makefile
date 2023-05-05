# this should be something like 195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE
DOC_ID := YOUR_DOCUMENT_ID_HERE

upload: venv test.md
	venv/bin/python3 markdown2gdocs.py $(DOC_ID) test.md

.PHONY: test.md
test.md:
	python3 genmd.py > $@

venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt
