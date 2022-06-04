# OpticalMarxistRecognition

To run locally you'll need to install tesseract-ocr [https://github.com/tesseract-ocr/tesseract]

Should be something like apt-get install tesseract-ocr or brew install tesseract


Then (after installing the requirements in requirements.txt) just run `python ocr_test.py` and probably some webserver so you can be served the html file (`python3 -m http.server 8001` in the directory and then head to localhost:8001/ocr.html is a workable initial hack; use your favorite)
