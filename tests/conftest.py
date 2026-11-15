import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from backend.models import Application
from backend.database import Base, get_db
from backend.main import app

# To send that request, the test needs two things prepared:

# A database for the route to write to. It must be a throwaway, in RAM, never tracker.db.
# A fake browser (TestClient) connected to your app, so the route uses the throwaway database.

# Preparing those is exactly what fixtures are for. Without them, you would repeat the same setup in every test. So conftest.py holds two fixtures:

# db: gives each test a fresh, empty throwaway database and a session connected to it.
# client: gives each test a fake browser that is wired to that session.

# The tests then ask only for client. They never see the database setup.

test_engine = create_engine("sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,)
SessionTest = sessionmaker(test_engine)

@pytest.fixture
def db():
    with SessionTest() as session:
        Base.metadata.create_all(test_engine)
        yield session
        Base.metadata.drop_all(test_engine)


@pytest.fixture
def client(db):                                  
    def override_get_db():                       
        return db                                
    app.dependency_overrides[get_db] = override_get_db   
    yield TestClient(app)                        
    app.dependency_overrides.clear()             