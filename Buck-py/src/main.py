import sys
import json 
import os
import shlex 
import pprint
import importlib.resources

import firebase_admin
from firebase_admin import credentials,firestore


with importlib.resources.path("src","serviceAccountKey.json") as fire_resource:
  cred = credentials.Certificate(fire_resource)
  firebase_admin.initialize_app(cred)

# Checks / Creates a local data.json file to store buckets.
with importlib.resources.path("src","main.py") as haar_resource:
    
  file = os.path.abspath(haar_resource)
  file = file[:-11]
  file = file + "buck-data/"
  
  if os.path.isdir(file):
    i = 0
    
  else:
    os.mkdir(file)
    data = file + "data.json"
    f = open(data,"a+")
    
    
# Creates the Bucket class 
class Bucket: 
  def __init__(self,name,executor,commandList,description):
    self.name = name
    self.executor = executor
    self.commandList = commandList
    self.description = description
  def __str__(self):
    return "{} {} {} {} {}". format(self.name, self.executor,self.commandList,self.description, self.count)


# Interacts with local db

def middleMan(arg,data): 
  try :
    #Fetches data from data file 
    with importlib.resources.path("src","main.py") as haar_resource:
      
      file = os.path.abspath(haar_resource)
      file = file[:-11]
      dataFilePath = file + "buck-data/data.json"
      
      if arg == "r":
        with open (dataFilePath, 'r') as f:
          data = f.read()
          f.close()
          
        return data
      
      elif arg == "a":
        data = json.dumps(data)
        with open(dataFilePath,"a") as f: 
          data = '\n'+data+', \n'
          f.write(data)
          f.close()

      elif arg == "w":
        data = json.dumps(data)

        with open(dataFilePath,"w") as f: 
          data = '\n'+data+', \n'
          f.write(data)
          f.close()
  
      else: 
        return dataFilePath

  except FileNotFoundError:
    print(">> Cannot locate data file :  " + dataFilePath )
  except Exception as e:
    print (">> Error")

# Creates a New Bucket
def createBucket():
  try :
    print(' >> Howdy! Create A New Bucket ')
    name = input("\n Name : ")
    print ('\n >> Seperate commands with a comma')
    preCmds = input (" Commands : ")
    
    cmds = preCmds.split(',')
    executor = str(input("\n Executor : ")) 
    detail = str(input("""\n Description : """))
    data = Bucket(name,executor,cmds,detail)
    
    # Load data object into a new object (spaghetti code❗)
    newData = {
      "name": data.name,
      "executor":data.executor,
      "buck_list":data.commandList,
      "description":data.description
    }
    
    middleMan("a",newData)

    # Sucess Message
    print('\n >> yay! it is done ')

    # terrible code that needs to be fixed.
    score = 0
    for i in data.commandList:
     
      if "$"  in i :
        score += 10000
      if "$" not in i :
        score -= 10
      if score > 1000:
        print (f"\n >> Usage : 'buck {data.executor} [extra argument]' ")
        break
      elif score < 1000:
        print (f"\n >> Usage : 'buck {data.executor}' ")

  except KeyboardInterrupt:
    print("\n >> KeyboardInterrupt :  Process terminated !") 


#List out bucketsq
def listBucket(arg):
  
  if len(arg) > 2:
  
    # fetch data from middleMan()
    data = middleMan("r","")
    if data :
      if data[-4] == ",":
        data = data[:-4]
      else:
        data = data[:-3]
    
      otherData = '{ "bucket" : [' + data + ' ] } '

      data = json.loads(otherData)
      data = data['bucket']
      
      # Logic
      for i in data:
    
        response = i.get('name')

      if arg[2] in response:
        if i:
          print (' >> Here you go : \n')
          print(json.dumps(i,indent=2))
        else:
          print(">> no data")
    else:
      print(">> no data")
  else:
    # fetch data from middleMan()
    data = middleMan("r","")
    if data:
      modifiedData = '{ "bucket" : [' + data + '{} ] } '
  
      #Coverts Data To Json
      jsonData = json.loads(modifiedData)
  
      # Renders Data 
      print (' >> Here you go : \n')
  
      print(json.dumps(jsonData,indent=2))
    else:
      print(">> no data")
  

# Check if command is cd
def is_cd(command: str) -> bool:
  command_split = shlex.split(command)
  return command_split[0] == "cd" 
  # this returns True if command is cd or False if not
  
  
# Runs commands if is_cd == True
def run_command(command: str) -> int:
  if is_cd(command):
    split_command = shlex.split(command)
    directory_to_change = ' '.join(split_command[1:])
    os.chdir(directory_to_change)
  else: 
    os.system(command)

#Run Commands From Bucket
def run(arg):
  
 # Fetch Data from middleMan()
  data = middleMan("r","")
  data = data[:-3]
  
  otherData = '{ "bucket" : [' + data + '] } '
  
  # Coverts modified data to json
  data = json.loads(otherData)
  
  
  # Logic
  for i in data['bucket']:
    response = i.get('executor')

    if arg[1] in response:
      
      buck = i.get('buck_list')

      if len(arg) > 2 :
        for i in buck:
          #  print (cmd)
          if '$' in i:
            
            cmd = i
            newCmd = cmd.replace('$',arg[2])
     
            for i in range(len(buck)):
              if buck[i] == cmd:
                buck[i] = newCmd
        for i in buck:
          run_command(i)
        
        if len(buck) == 1 :
          print('>> Done! executed 1 command.')
          
        else:
          print('>> Done! executed '+ str(len(buck)) + ' commands.')
          
      else:
        for i in buck:
        
          if '$' in i:
            print(">> This command takes in an extra argument -'" + arg[1] + " <extra argument>'")
            sys.exit()
          
        for i in buck:
          run_command(i)
        
        if len(buck) == 1 :
          print('\n >> Done! executed 1 command.')
        else:
          print('\n >> Done! executed '+ str(len(buck)) + ' commands.')
          
def eraseBucket():
  ans = input('\n>> This would wipe out your bucket data ! , "y" or "n" : ' )
  if ans == "y" or ans == "Y":
    file = middleMan("","")
    # Write Json to a Json Data Fi
    with open(file,"w") as f: 
      f.write("")
      f.close()
    # Sucess Message
    print('\n>> Your bucket is now empty.  ')
    # End Process
    sys.exit()
  elif ans == "n" or ans == "N":
    print("\n>> Process Terminated...")
  else:
    print("\n>> error :  You did not enter a valid input, try again !")
    sys.exit()

#Add bucket from cloud
def addBucket(arg):
  print("\n >> Searching for " + arg[2] + " ...\n")
  try :
    exe = arg[2]
    db = firestore.client()
    collection = db.collection('buckets')
    doc = collection.document(exe)
    res = doc.get().to_dict()
    

    if res is not None:
      print(' >> Fetching ' + arg[2] + " ...\n" )
      name = res.get("name")
      executor = res.get('executor')
      commandList = res.get('commands')
      description = res.get('description')
      newData = {
        "name": name,
        "executor":executor,
        "buck_list":commandList,
        "description":description
      }
      
      middleMan("a",newData)

      print(' >> yay! it is done ')
      score = 0
      for i in commandList:
       
        if "$"  in i :
          score += 10000
        if "$" not in i :
          score -= 10
        if score > 1000:
          print (f"\n >> Usage : 'buck {executor} [extra argument]' ")
          break
        elif score < 1000:
          print (f"\n >> Usage : 'buck {executor}' ")
 
    elif res == None:
      print(" >> No bucket - " + arg[2] + " :(")

    # End Process
    sys.exit()

  except Exception as e:
    print(" >> Oops! :( An error occured")

# deletes a bucket 
def deleteBucket(arg):
  if len(arg) > 2:
    # fetch data from middleMan()
    data = middleMan("r","")
    data = data[:-3]
  
    otherData = '{ "bucket" : [' + data + '] } '
  
    # Coverts modified data to json
    data = json.loads(otherData)
    data = data['bucket']
    #Logic
    try:
      
      for i in range(len(data)):
        response = data[i].get('executor')
      
         
        if arg[2] == response: 
          
          ans = input('\n>> This would delete bucket "' + arg[2] + '" ! , "y" or "n" : ' )
          if ans == "y" or ans == "Y":
            
            # Write new Json to a Json Data file
           
            del data[i]

            if data == [] or data == None:
              file = middleMan("","")
              # Write Json to a Json Data Fi
              with open(file,"w") as f: 
                f.write("")
                f.close()
            else:
              middleMan("w",data)
    
             # Sucess Message
            print('\n>> Done !  ')
            # End Process
            sys.exit()
          elif ans == "n" or ans == "N":
            print("\n>> Process Terminated...")
          else:
            print("\n>> error :  You did not enter a valid input, try again !")
            sys.exit()
        
         
    except Exception:
      return

def helpGuide():
  print(" >> Welcome to buck :) \n")
  print(" >> Let's tour buck together. Visit https://getbuck.tech/ for more info \n")
  print(" >> Run 'buck --list' or 'buck -l' to list all your buckets. \n")
  print(" >> Run 'buck --create' or 'buck -c' to create a new bucket. \n")
  print(" >> Run 'buck --add <name> ' or 'buck -a <name>' to add a new bucket from the cloud. \n")
  print(" >> Run 'buck --delete <name> ' or 'buck -d <name>' to delete a bucket . \n")
  print(" >> Run 'buck --erase' or 'buck -e' to clear all your buckets. \n")
  print(" >> Run 'buck --help' or 'buck -h' for help. \n")
  print(" >> Happy hacking, chief :) \n")

# Main Function
def main(arg=sys.argv):
  
  args = ['--create','-c','--list','-l','--erase','-e','--help','-h','--add','-a','-d','--delete']
  if len(arg) == 1:
    print (""" >> Hello, chief :) \n """)
    print(" >> Run 'buck --help' for help \n")
    print(" OR \n")
    print(" >> Visit https://getbuck.tech/")
    
  elif arg[1] == '--create' or arg[1] == '-c':
    createBucket()
    
  elif arg[1] == '--list' or arg[1]=='-l':
    
    listBucket(arg)

  elif arg[1] == '--erase' or arg[1]=='-e':
    
    eraseBucket()

  elif arg[1] == '--help' or arg[1]=='-h':
    
    helpGuide()

  elif arg[1] == '--delete' or arg[1]=='-d':
    deleteBucket(arg)

  elif arg[1] == '--add' or arg[1]=='-a':
    addBucket(arg)

  elif arg[1] not in args:
    run(arg)
 
