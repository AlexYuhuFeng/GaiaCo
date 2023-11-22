import cv2
import pytesseract
from pdf2image import convert_from_path
from intel.openvino.inference_engine import IECore

def scan_book(book_path):
    # Convert the book's pages into images
    images = convert_from_path(book_path)

    # Initialize Intel's Inference Engine
    ie = IECore()

    # Load the OCR model
    net = ie.read_network(model='ocr_model.xml', weights='ocr_model.bin')
    exec_net = ie.load_network(network=net, device_name='CPU')

    # Process each page
    for i, image in enumerate(images):
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Use the OCR model to recognize text
        input_blob = next(iter(net.input_info))
        out_blob = next(iter(net.outputs))
        result = exec_net.infer(inputs={input_blob: gray})

        # Extract the recognized text
        text = pytesseract.image_to_string(result)

        # Save the text to a file
        with open(f'page_{i}.txt', 'w') as f:
            f.write(text)
