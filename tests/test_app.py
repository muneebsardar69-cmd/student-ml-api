import pytest
from app import app


@pytest.fixture
def client():
    """
    Fixture that sets up Flask test client.
    This allows us to make test requests without running the server.
    """
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client


def test_health_endpoint(client):
    """
    Test that GET /health returns correct status and version.
    Expected status code: 200
    """
    response = client.get('/health')
    
    # Check status code
    assert response.status_code == 200
    
    # Get JSON data from response
    data = response.get_json()
    
    # Verify response contains correct fields
    assert data['status'] == 'healthy'
    assert data['application'] == 'student-ml-api'
    assert data['version'] == '1.0.0'


def test_predict_valid_input(client):
    """
    Test that POST /predict works with valid numeric input.
    Input: {"value": 10}
    Expected output: {"input": 10, "prediction": 20}
    """
    response = client.post('/predict', 
        json={'value': 10})
    
    # Check status code
    assert response.status_code == 200
    
    # Get JSON response
    data = response.get_json()
    
    # Verify input and prediction
    assert data['input'] == 10
    assert data['prediction'] == 20


def test_predict_missing_input(client):
    """
    Test that POST /predict returns error when 'value' is missing.
    Expected status code: 400 (Bad Request)
    """
    response = client.post('/predict', 
        json={})
    
    # Check status code is 400 (Bad Request)
    assert response.status_code == 400
    
    # Get error response
    data = response.get_json()
    
    # Verify error message exists
    assert 'error' in data
    assert 'value' in data['error'].lower()


def test_predict_invalid_input(client):
    """
    Test that POST /predict returns error when value is not a number.
    Input: {"value": "not_a_number"}
    Expected status code: 400 (Bad Request)
    """
    response = client.post('/predict', 
        json={'value': 'not_a_number'})
    
    # Check status code is 400 (Bad Request)
    assert response.status_code == 400
    
    # Get error response
    data = response.get_json()
    
    # Verify error message contains info about number type
    assert 'error' in data
    assert 'number' in data['error'].lower()
