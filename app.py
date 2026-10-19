"""Flask web server application for hand sign language image recognition."""

# Importing required libs
from flask import Flask, render_template, request
from model import preprocess_img, predict_result

# Instantiating flask app
app = Flask(__name__)


# Home route
@app.route("/")
def main():
    """Render the home page template index.html."""
    return render_template("index.html")


# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    """Predict the digit in the uploaded image."""
    error = None
    pred = None

    try:
        if 'file' not in request.files or request.files['file'].filename == '':
            raise ValueError("No file uploaded or selected.")

        file_stream = request.files['file'].stream
        img = preprocess_img(file_stream)
        pred_value = predict_result(img)
        pred = str(pred_value)
    #Catch specific exceptions related to file processing and prediction
    except (ValueError, KeyError, OSError, RuntimeError) as e:
        error = f"File cannot be processed. Details: {str(e)}"
    #Make sure always return the result.html template with predictions and error message (if any)
    return render_template("result.html", predictions=pred, err=error)


# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
