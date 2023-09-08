from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    
    current_day = datetime.datetime.utcnow().strftime('%A')
    utc_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ')

    
    # Assuming you're running this script from a GitHub repo
    github_file_url = "https://github.com/Samdami/HNG/blob/main/Stage1.py"
    github_repo_url = "https://github.com/Samdami/HNG"
    
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
