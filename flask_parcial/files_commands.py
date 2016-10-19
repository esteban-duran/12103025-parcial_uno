from subprocess import Popen, PIPE

def get_all_files():
  file_list = Popen(["ls","-a"], stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None,file_list)

def add_file(filename,content):
  add_process = Popen(["cat",">",filename,"<<","EOF",content,"EOF"], stdout=PIPE, stderr=PIPE)
  add_process.wait()
  return True if filename in get_all_files() else False

def remove_file(filename):
    remove_process = Popen(["rm","-rf",filename], stdout=PIPE, stderr=PIPE)
    remove_process.wait()
    return False if filename in get_all_files() else True
