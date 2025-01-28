import pytest
import requests
import json

base_url = "https://api.restful-api.dev/objects"

headers = {"content-type": "application/json"}

@pytest.fixture
def create_object():
    payload = json.dumps({
        "name": "Apple AirPods", 
        "data": { 
            "color": "white", 
            "price": 135
        }
    })
    
    print("Creating a new object using POST...")
    response = requests.post(base_url, data=payload, headers=headers)
    
    # Verify the POST request is successful
    assert response.status_code == 200, f"Failed to create object. Status code: {response.status_code}"
    print("Object created successfully!")
    
    # Return the created object ID
    object_id = response.json()["id"]
    print(f"New object ID: {object_id}")
    return object_id

def test_patch_object(create_object):
    object_id = create_object
    patch_payload = json.dumps({
        "data": { 
            "color": "black", 
            "generation": "3rd", 
            "price": 1150
        }
    })
    
    # Send PATCH request
    patch_url = f"{base_url}/{object_id}"
    print(f"Updating object with ID {object_id} using PATCH...")
    patch_response = requests.patch(patch_url, data=patch_payload, headers=headers)
    
    # Verify the PATCH request is successful
    assert patch_response.status_code == 200, f"Failed to update object. Status code: {patch_response.status_code}"
    print("Object updated successfully!")

    patched_data = patch_response.json()
    print(f"Updated object data: {patched_data}")

    assert patched_data["data"]["color"] == "black", "Color was not updated correctly"
    assert patched_data["data"]["generation"] == "3rd", "Generation was not updated correctly"
    assert patched_data["data"]["price"] == 1150, "Price was not updated correctly"
    print("All data verified successfully.")

def test_patch_non_existent_object():
    patch_payload = json.dumps({
        "data": { 
            "color": "red", 
            "price": 999
        }
    })
    
    # Use a non-existent object ID for PATCH request
    non_existent_id = 99999
    patch_url = f"{base_url}/{non_existent_id}"
    
    print(f"Trying to update non-existent object with ID {non_existent_id} using PATCH...")
    patch_response = requests.patch(patch_url, data=patch_payload, headers=headers)
    
    # Verify that the PATCH request fails with 404 Not Found
    assert patch_response.status_code == 404, "Expected 404 for non-existent object"
    print(f"Received expected 404 status for non-existent object ID {non_existent_id}.")
