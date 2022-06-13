import json


def test_create_job(client):
    data = {
        "title": "11",
        "company": "d23232e",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20"
        }
    response = client.post("/jobs/create-job/",json.dumps(data))
    assert response.status_code == 200
    assert response.json()["company"] == "d23232e"
    assert response.json()["description"] == "python"


def test_read_job(client):     #new test
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20"
        }
    response = client.post("/jobs/create-job/",json.dumps(data))

    response = client.get("/jobs/get/1/")
    assert response.status_code == 200
    assert response.json()['title'] == "SDE super"