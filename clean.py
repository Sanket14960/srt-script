import os

def remove_srt(folder_path):

  filenames = os.listdir(folder_path)

  list_of_paths = []

  for i in filenames:
    list_of_paths.append(folder_path +  i)


  for i in range(len(list_of_paths)):
    for k in os.listdir(list_of_paths[i]):
      if k.endswith(".srt"):
        os.chdir(list_of_paths[i])
        os.remove(k)


remove_srt('C:\\Users\\Sanket Patel\\Desktop\\algo\\')
