
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request

# logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
# logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    # logger.info(request.json)
    
    # TODO add your implementation here to replace the random response
    dims = request.json['arena']['dims']
    
    my_state = request.json['arena']['state']['https://cloud-run-hackathon-python-7ei5boopga-uc.a.run.app']
    all_state = request.json['arena']['state']

    if my_state['x'] == 0 and my_state['y'] == (dims[1] - 1) :
        for key, value in all_state.items():
            if key != 'https://cloud-run-hackathon-python-7ei5boopga-uc.a.run.app':
                if my_state['x'] == value['x'] and my_state['y'] <= (value['y'] + 3):
                    if my_state['direction'] == 'N':
                        return moves[1]
                    elif my_state['direction'] == 'E' or my_state['direction'] == 'S':
                        return moves[2]
                    else:
                        return moves[3]
                elif my_state['x'] >= (value['x'] - 3) and my_state['y'] == value['y']:
                    if my_state['direction'] == 'E':
                        return moves[1]
                    elif my_state['direction'] == 'N' or my_state['direction'] == 'W':
                        return moves[3]
                    else:
                        return moves[2]
            else:
                continue
    
    if  my_state['x'] > 0 :
        if my_state['direction'] == 'W' :
            return moves[0]
        elif my_state['direction'] == 'E' or my_state['direction'] == 'S':
            return moves[3]
        elif my_state['direction'] == 'N' :
            return moves[2]
    
    if my_state['y'] < (dims[1] - 1):
        if my_state['direction'] == 'S' :
            return moves[0]
        elif my_state['direction'] == 'E' or my_state['direction'] == 'N':
            return moves[3]
        elif my_state['direction'] == 'W' :
            return moves[2]

    return moves[1]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
