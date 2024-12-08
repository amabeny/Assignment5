from fastapi.testclient import TestClient
from ..controllers import orders
from ..main import app
import pytest
from ..models import models

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):
    # Create a sample order
    order_data = {
        "customer_name": "John Doe",
        "description": "Test order"
    }

    order_object = models.Order(**order_data)

    # Call the create function
    created_order = orders.create(db_session, order_object)

    # Assertions
    assert created_order is not None
    assert created_order.customer_name == "John Doe"
    assert created_order.description == "Test order"

def test_create_resource(client):
    response = client.post("/resources/", json={"name": "Water", "description": "Essential for life"})
    assert response.status_code == 200
    assert response.json()["name"] == "Water"

# Add more tests for other CRUD operations.
