#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage

def main():
    # Create an instance of BaseModel
    base_model_instance = BaseModel()

    # Print the instance details
    print("BaseModel Instance:")
    print(base_model_instance)

    # Save the instance to the storage
    base_model_instance.save()

    # Print the instance details after saving
    print("\nBaseModel Instance after save:")
    print(base_model_instance)

    # Retrieve the instance from the storage
    loaded_instance = storage.all().get(base_model_instance.__class__.__name__ + "." + base_model_instance.id)

    # Print the loaded instance details
    print("\nLoaded Instance:")
    print(loaded_instance)

if __name__ == "__main__":
    main()
