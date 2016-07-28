# ELIS PDF stuff


## Cover sheet generation

Prerequisites: python-pip, virtualenv (`pip install virtualenv`)

Uses the reportlab library for PDF generation

### Usage

Installation

```
virtualenv venv
. venv/bin/activate

pip install -r requirements.txt
```

Generating a PDF. Here we've chosen out.pdf as our output file (will be overwritten).

```
. venv/bin/activate
./make_cover_sheet.py out.pdf 'RPC  AY0700' 'A12345678' 'IOE0123456789'
```

