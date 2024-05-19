<!DOCTYPE html>
<html>
<head>
    <title>BeyondChats Assignment</title>
    <style>
        /* Styles for the intro page */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .assignment-info {
            margin-bottom: 30px;
        }
        .assignment-info h2 {
            color: #666;
            margin-top: 0;
        }
        .assignment-info p {
            margin: 10px 0;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #333;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #555;
        }

        
    </style>
</head>
<body>
    <div class="container">
        <div id="intro-page">
            <h1>BeyondChats Assignment</h1>
            <div class="assignment-info">
                <h2>Task Overview</h2>
                <p>The task was to develop a Python program that fetches data from a paginated API, identifies whether the response for each response-sources pair came from any of the sources, lists down the sources from which the response was formed, and returns the citations for all objects coming from the API.</p>

                <h2>Provided Resources</h2>
                <p>The following resources were provided for the assignment:</p>
                <ul>
                    <li>API endpoint: <a href="https://devapi.beyondchats.com/api/get_message_with_sources">https://devapi.beyondchats.com/api/get_message_with_sources</a></li>
                    <li>Example input and output format</li>
                </ul>

                <h2>Requirements</h2>
                <p>The assignment required the following steps to be performed:</p>
                <ol>
                    <li>Fetch the data from the pages of the API.</li>
                    <li>Identify whether the response for each response-sources pair came from any of the sources.</li>
                    <li>List down the sources from which the response was formed, or return an empty array if the response did not come from any source.</li>
                    <li>Return the citations for all objects coming from the API.</li>
                    <li>(Extra points) Present the solution through a user-friendly UI.</li>
                </ol>

                <h2>Solution Approach</h2>
                <p>The assignment was approached using Python and various libraries for data retrieval, natural language processing, and similarity matching. The steps involved fetching data from the API, preprocessing the response and source texts, calculating similarity scores, and determining the citations based on a threshold. The results were then presented through a web-based user interface.</p>
            </div>
            
        </div>
        
</body>
</html>
