import requests as rq
import json

AUTHPATH = "../graphql/auth.json"
QUERYPATH = "../graphql"

APIURL = "http://localhost:3000/graphql"

s = rq.Session()

def get_data_from_response(queryobject, queryname):
    return queryobject["data"][queryname]

def authenticate():
    with open(AUTHPATH, "r") as authfile:
        authdata = json.load(authfile)

        with open(f"{QUERYPATH}/signin.gql", "r") as queryfile:
            query = queryfile.read().replace("<<username>>", authdata['username']).replace("<<password>>", authdata['password'])

            print("Authenticating...")

            response = s.post(APIURL, json={"query": query})

            data = get_data_from_response(response.json(), "signin")

            if "user" not in data:
                print("Authentication failed, check your credentials")
                quit()
            else:
                print(f"User signed in as {data['user']['username']}")

            return data


def get_tracks(limit=None, random=False):
    with open(f"{QUERYPATH}/tracks.gql", "r") as queryfile:
        limitStr = ""

        if limit != None:
            limitStr = f", limit: {limit}"

        params = f"random: {str(random).lower()}{limitStr}"

        query = queryfile.read().replace("<<params>>", params)

        print("Getting tracks from the Mino API...")

        response = s.post(APIURL, json={"query": query})

        data = get_data_from_response(response.json(), "tracks")

        return data
