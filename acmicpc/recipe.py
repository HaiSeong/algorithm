import requests
import json


def get_all_recipes(api_key, service_id, data_type):
    base_url = "http://openapi.foodsafetykorea.go.kr/api"

    initial_url = f"{base_url}/{api_key}/{service_id}/{data_type}/1/1"
    response = requests.get(initial_url)
    data = json.loads(response.text)

    total_count = int(data[service_id]['total_count'])

    all_recipes = []
    batch_size = 1000

    for start_idx in range(1, total_count + 1, batch_size):
        end_idx = min(start_idx + batch_size - 1, total_count)
        url = f"{base_url}/{api_key}/{service_id}/{data_type}/{start_idx}/{end_idx}"

        response = requests.get(url)
        data = json.loads(response.text)

        recipes = data[service_id]['row']
        all_recipes.extend(recipes)

    return all_recipes


# 사용 예
api_key = "79e8e1c07b534988ab85"
service_id = "COOKRCP01"
data_type = "json"

all_recipes = get_all_recipes(api_key, service_id, data_type)
for a in all_recipes:
    print(a['RCP_PARTS_DTLS']) # 재료
    print(a['ATT_FILE_NO_MAIN']) # 사진
    print(a)
print(f"Total recipes fetched: {len(all_recipes)}")