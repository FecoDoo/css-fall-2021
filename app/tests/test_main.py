from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_course():
    ## TODO: Check if GET /courses/{course_id} returns status code 200 and that the json response is
    ## correct (as per db) when the course exists
    pass


def test_read_nonexistent_course():
    ## TODO: Check if GET /courses/{course_id} returns status code 404 and that the json response is
    ## {"detail": "Course does not exist"} when the course does not exist
    pass


def test_create_course():
    ## TODO: Check if POST /courses/ returns status code 200 and that the json response
    ## contains the correct data if the course does not exist in the db.
    pass

def test_create_existing_course():
    ## TODO: Check if POST /courses/ returns status code 400 and that the json response
    ## is {"detail": "Course already exists"} if the course already exists in the db.
    pass
