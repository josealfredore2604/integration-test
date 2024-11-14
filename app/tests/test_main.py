import requests
import time

BASE_URL = "http://backend:8000"

def wait_for_service(url, timeout=30):
  for _ in range(timeout):
    try:
      response = requests.get(url)
      if response.status_code == 200:
        return True
    except requests.ConnectionError:
      time.sleep(1)
  return False

def test_root_endpoint():
  assert wait_for_service(f"{BASE_URL}/"), "Backend service is not ready"
  response = requests.get(f"{BASE_URL}/")
  assert response.status_code == 200
  assert response.json() == {"message": "Hello, World!"}

def test_db_status():
  assert wait_for_service(f"{BASE_URL}/db-status"), "Backend service is not ready"
  response = requests.get(f"{BASE_URL}/db-status")
  assert response.status_code == 200
  assert response.json()["status"] == "Database is reachable"
