import random
import json
from flask import escape, jsonify
from flask_cors import cross_origin

# Quotes list.
quotes = [
    "Life is what happens when you're busy making other plans. — John Lennon",
    "Get busy living or get busy dying. — Stephen King",
    "You only live once, but if you do it right, once is enough. — Mae West",
    # Add as many quotes as you want here...
]

# This function will respond to web requests.
@cross_origin()  # Allows CORS for all domains on all routes
def random_quote(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    # Check if a specific key was provided as part of the JSON payload or query string.
    if request_json and 'key' in request_json:
        key = request_json['key']
    elif request_args and 'key' in request_args:
        key = request_args['key']
    else:
        key = None

    if key:
        # Filter quotes that contain the 'key'.
        filtered_quotes = [q for q in quotes if key.lower() in q.lower()]
        if not filtered_quotes:
            # If no quotes are found with the 'key', return a 'not found' message.
            return jsonify({"error": "No matching quotes found"}), 404
        # If filtered quotes exist, randomly choose one from the filtered list.
        quote = random.choice(filtered_quotes)
    else:
        # If no 'key' is provided, randomly choose a quote from the full list.
        quote = random.choice(quotes)

    # Return the quote in JSON format with CORS headers set.
    return jsonify({"quote": escape(quote)})
