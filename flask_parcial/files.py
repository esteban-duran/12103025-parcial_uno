from flask import Flask, abort, request
import json, os

from files_commands import get_all_files, remove_file, get_all_recent_files

app = Flask(__name__)

@app.route('/files', methods=['POST'])
def create_file():
  content = request.get_json(silent=True)
  filename = content['filename']
  content = content['content']
  os.chdir('files_created')
  add_process = open(filename+'.txt','a')
  add_process.write(content+'\n')
  add_process.close()
  os.chdir('..')
  return "File created",201

@app.route('/files', methods=['GET'])
def read_file():
  list = {}
  list["files"] = get_all_files()
  return json.dumps(list), 200

@app.route('/files', methods=['PUT'])
def update_file():
  return "not found", 404
  
@app.route('/files', methods=['DELETE'])
def delete_file():
  error = False
  for filename in get_all_files():
    if not remove_file(filename):
      error = True
  if error:
    return 'some files were not deleted', 400
  else:
    return 'all files were deleted', 200

@app.route('/files/recently_created', methods=['POST'])
def create_recent_file():
  return "not found", 404
  
@app.route('/files/recently_created', methods=['GET'])
def read_recent_file():
  list = {}
  list["files"] = get_all_recent_files()
  return json.dumps(list), 200
  
@app.route('/files/recently_created', methods=['PUT'])
def update_recent_file():
  return "not found", 404
  
@app.route('/files/recently_created', methods=['DELETE'])
def delete_recent_file():
  return "not found", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=9090, debug='True')
