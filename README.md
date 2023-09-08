<h1>Objective</h1>

Create and host an endpoint using any programming language of your choice.<br>
The endpoint should take two GET request query parameters and return specific information in JSON format.<br>


Requirements<br>
The information required includes:<br>
Slack name<br>
Current day of the week<br>
Current UTC time (with validation of +/-2)<br>
Track<br>
The GitHub URL of the file being run<br>
The GitHub URL of the full source code.<br>
A  Status Code of Success<br>





<h1>JSON</h1>
<p>{
  "slack_name": "example_name",<br>
  "current_day": "Monday",<br>
  "utc_time": "2023-08-21T15:04:05Z",<br>
  "track": "backend",<br>
  "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",<br>
  "github_repo_url": "https://github.com/username/repo",<br>
  "status_code": 200<br>
}</p>

<h2>Acceptance Criteria</h2>

<p>Endpoint Creation: Provide a publicly accessible endpoint.<br>
GET Parameters: The endpoint should accept two GET request query parameters: slack_name and track.
       E.g.: http://example.com/api?slack_name=example_name&track=backend.
Slack Name: The response should include the slack_name passed as a GET request query parameter.
Current Day of the Week: Display the current day of the week in full (e.g., Monday, Tuesday, etc.).
Current UTC Time: Return the current UTC time, accurate within a +/-2 minute window.
Track: The response should display the track of the you signed up for (Backend). This will be based on the track GET parameter passed to the endpoint.
GitHub File URL: Include a direct link to the specific file in the GitHub repository that's being executed.
GitHub Repo URL: Include a link to the main page of the GitHub repository containing the project's entire source code.
Status Code: Return 200 as Integer.
JSON Format: The endpoint's response should adhere to the specified JSON format.
Testing: Before submission:
Ensure the endpoint is accessible.
Check the returned JSON against the defined format.
Validate the correctness of each data point in the JSON response.</p>

