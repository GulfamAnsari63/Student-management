from bson import ObjectId

def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "address": {
            "city": student["address"]["city"],
            "country": student["address"]["country"]
        }
    }
