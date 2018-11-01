from flask import decoded_jsonson
from flask import request
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/github', methods=['POST'])
def github_webhooks():
    """
    Takes no arguments
    Triggers webhook on PR for rep (repo must have webhooks setup first)
    """
    if request.method == 'POST':
        with open('data.txt', 'w', encoding='utf-8') as outputfile:
            info = decoded_jsonson.dumps(request.decoded_jsonson)
            pull_request = {}
            decoded_decoded_jsonson = decoded_jsonson.loads(info)
            for item in decoded_json:
                if decoded_json["action"] == "closed" or decoded_json["action"] == "opened":
                    pull_request["action"] = decoded_json["action"]
                    time = decoded_json["pull_request"]["created_at"]
                    pull_request["created_at"] = time
                    pull_request["number"] = decoded_json["number"]
                    pull_request["pr_sender"] = decoded_json["sender"]["login"]
                    pull_request["head_branch"] = decoded_json["pull_request"]["head"]["ref"]
            outputfile.write(str(pull_request))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
