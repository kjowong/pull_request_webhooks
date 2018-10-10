from flask import json
from flask import request
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/github', methods=['POST'])
def github_webhooks():
    if request.method == 'POST':
        with open('data.txt', 'w', encoding='utf-8') as outputfile:
            info = json.dumps(request.json)
            pull_request = {}
            j = json.loads(info)
            for item in j:
                if j["action"] == "closed" or j["action"] == "opened":
                    pull_request["action"] = j["action"]
                    time = j["pull_request"]["created_at"]
                    pull_request["created_at"] = time
                    pull_request["number"] = j["number"]
                    pull_request["pr_sender"] = j["sender"]["login"]
                    pull_request["head_branch"] = j["pull_request"]["head"]["ref"]
            outputfile.write(str(pull_request))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
