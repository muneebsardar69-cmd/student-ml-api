from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)


# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint that returns the application status.
    Returns application name and version.
    """
    response = {
        "status": "healthy",
        "application": "student-ml-api",
        "version": "1.0.0"
    }
    return jsonify(response), 200


# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    """
    Prediction endpoint that takes a numeric value and returns
    a simple prediction (value * 2).
    
    Expected input: {"value": <number>}
    Returns: {"input": <number>, "prediction": <number>}
    """
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        # Check if request body is empty
        if data is None:
            return jsonify({
                "error": "Request body must be JSON"
            }), 400
        
        # Check if 'value' key exists in data
        if 'value' not in data:
            return jsonify({
                "error": "Missing 'value' in request body"
            }), 400
        
        # Get the value from request
        value = data['value']
        
        # Validate that value is a number (int or float)
        if not isinstance(value, (int, float)):
            return jsonify({
                "error": "Value must be a number (int or float)"
            }), 400
        
        # Simple prediction logic: multiply value by 2
        prediction = value * 2
        
        # Return prediction result
        response = {
            "input": value,
            "prediction": prediction
        }
        return jsonify(response), 200
        
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            "error": f"Server error: {str(e)}"
        }), 500


# Main entry point
if __name__ == '__main__':
    # Run Flask app on all interfaces (0.0.0.0) on port 5000
    # debug=False for production-like behavior
    app.run(host='0.0.0.0', port=5000, debug=False)
