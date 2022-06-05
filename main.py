#Assignment 2
#By: Ryan Kaszubski

#URL to get jokes: localhost:5000/?jokes=[number here]

#Docker commands:
#Build: docker build --tag jokesv2 .
#Run: docker run -d -p 5000:5000 jokesv2
#go to localhost:5000/?jokes=[number here] in browser

from flask import Flask, request
import random
import json
import os
app = Flask(__name__)
@app.route('/')
def jokeSeletor():
    numOfJokes = request.args.get('jokes')
    #super unfunny jokes from last assignment
    myJokes = [
        "I don't trust stairs: They are always up to something.",
        "Why didn't Han Solo enjoy his steak dinner? It was Chewie.",
        "When does a joke become a dad joke? When it becomes apparent",
        "What invention allows us to see through walls? Windows",
        "Why is a Jedi knight never lonely?: Because the force is with them",
        "What do you call a fish with no eye? A fsh",
        "Did you hear the rumor about butter? I'm not going to spread it!",
        "What does idk stand for? Everyone I ask says, I don't know.",
        "What do you call a snitching scientist? A lab rat",
        "What did the five fingers say to the face? Slap!"
    ]

    #list to store randomly selected jokes
    jokesToBeReturned = []
    
    #add x amount of jokes the user wants
    for _ in range (int(numOfJokes)):
        jokesToBeReturned.append(random.choice(myJokes))

    return json.dumps(jokesToBeReturned)

if __name__ == "__main__":
    
    app.run(host='0.0.0.0')