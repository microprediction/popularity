import os
from getjson import getjson
from microprediction import MicroWriter

write_key = os.environ.get('WRITE_KEY')    # GitHub action needs to set env variable. You need to create a GitHub secret called WRITE_KEY
mw = MicroWriter(write_key=write_key)
assert mw.key_difficulty(mw.write_key)>=12, "You need a key of difficulty 12 to create a stream"

CATEGORIES = ['watchers_count','stargazers_count','forks_count']
REPOS = {'pykalman':'https://github.com/pykalman/pykalman',
          'microprediction':'https://github.com/microprediction/microprediction',
          'prophet':'https://github.com/facebook/prophet',
          'neuralprophet':'https://github.com/ourownstory/neural_prophet',
          'river':'https://github.com/online-ml/river',
          'scikit-learn':'https://github.com/scikit-learn/scikit-learn',
          'tensorflow':'https://github.com/tensorflow/tensorflow',
          'keras':'https://github.com/keras-team/keras'}
      
REPO_APIS = dict([ (k,v.replace('https://github.com/','https://api.github.com/repos/') for k,v in REPOS.items() ] )
                
                
if __name__ == '__main__':
    for repo_name,repo_url in REPO_APIS.items()
        data = getjson(url)
        if data is not None:
            for category in CATEGORIES:
              current_value = int(data[category])
              level_name = category + '_' + repo_name + '.json'   
              previous_value = mw.get_current_value(name=level_name)
              if previous_value is None:
                  print('No previous value for '+level_name)
                  print( mw.set(name=level_name,value=current_value) )
              else:
                  if int(float(previous_value)) != int(float(current_value)):  
                      print( mw.set(name=level_name,value=current_value) ) 
                      print( level_name+' updated to '+str(current_value) )
                  else:
                      print( (level_name, current_value, ' is unchanged') )
        else:
            print(url)
           
