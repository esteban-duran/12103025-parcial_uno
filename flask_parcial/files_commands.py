from subprocess import Popen, PIPE
import os
def get_all_files():
  file_list = Popen(('ls','files_created'), stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None,file_list)

def remove_file(filename):
    os.chdir('files_created')
    remove_process = Popen(["rm","-rf",filename], stdout=PIPE, stderr=PIPE)
    remove_process.wait()
    os.chdir('..')
    return False if filename in get_all_files() else True

def get_all_recent_files():
  file_list = Popen(('ls','files_created','-t'), stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None,file_list)

