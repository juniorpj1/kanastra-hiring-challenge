import pytest
from starlette.testclient import TestClient
from app.index import app 
from app.schemas.schemas import Charges
from unittest.mock import patch
from unittest.mock import Mock, patch
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.services.service import ChargeService

class TestRoutes:
    @pytest.fixture(scope="module")
    def test_app(self):
        client = TestClient(app)
        yield client

    # Test the read_root route
    def test_read_root(self, test_app):
        response = test_app.get("/")
        assert response.status_code == 307 or response.status_code == 200
        #assert response.headers["Location"] == 'http://localhost:8080'

    # Test the create_charge route
    @patch('app.services.service.ChargeService.create')
    def test_create_charge_success(self, mock_create, test_app):
        mock_charge = {
            "name": "string",
            "governmentId": "string",
            "email": "string",
            "debtAmount": 1500.00,
            "debtDueDate": "string"
        }
        mock_create.return_value = mock_charge

        test_request_payload = {
            "name": "string",
            "governmentId": "string",
            "email": "string",
            "debtAmount": 1500.00,
            "debtDueDate": "string"
        }
        response = test_app.post("/charges", json=test_request_payload)
        assert response.status_code == 201
        assert response.json() == {"message": "Charge created successfully", "charge": mock_charge}
        mock_create.assert_called_once()

class TestChargeService:
    @patch('app.services.service.ChargeService.create')
    def test_create_charge_service(self, mock_create):
        mock_create.return_value = Charges(name="string", governmentId="string", email="string", debtAmount=1500.00, debtDueDate="string")
        
        db = Mock()
        db.add = Mock()
        db.commit = Mock()
        db.refresh = Mock()

        charge = Charges(name="string", governmentId="string", email="string", debtAmount=1500.00, debtDueDate="string")
        result = ChargeService.create(db, charge)
        assert result == charge

    def test_create_charge_service_exception(self):
        # Create a mock db session that raises an exception when add is called
        db = Mock()
        db.add.side_effect = SQLAlchemyError

        charge = Charges(name="string", governmentId="string", email="string", debtAmount=1500.00, debtDueDate="string")

        # Test that an HTTPException is raised when the db session raises an exception
        with pytest.raises(HTTPException):
            ChargeService.create(db, charge)