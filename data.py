
import requests

NUMBER_OF_QUESTION = 10
QUESTION_TYPE = "boolean"


parameters = {
    "amount": NUMBER_OF_QUESTION,
    "type": QUESTION_TYPE

}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = (data['results'])


