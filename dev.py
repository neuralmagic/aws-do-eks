import requests
import json
import time

url = 'http://localhost:8080/invocations'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
data = {
    "question": "What does the little engine say",
    "context": "In the childrens story about the little engine a small locomotive is pulling a large load up a mountain.\n  Since the load is heavy and the engine is small it is not sure whether it will be able to do the job. This is a story \n  about how an optimistic attitude empowers everyone to achieve more. In the story the little engine says: \'I think I can\' as it is \n  pulling the heavy load all the way to the top of the mountain. On the way down it says: I thought I could.",
    # "id": "string"
}

start_time = time.perf_counter()
# for _ in range(100):
    
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())
    
end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Response: {response.json()}")
print(f"Elapsed Time: {elapsed_time} seconds")