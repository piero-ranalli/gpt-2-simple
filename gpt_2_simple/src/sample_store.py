import pandas as pd

class SampleStore:

    def __init__(self, storefile):

        self.storefile = storefile

        self.open()


    def openOrCreate(self):

        try:
            self.csv = pd.read_csv(self.storefile)
        except:
            self.csv = pd.DataFrame({ 'model':[],
                                      'iters':[],
                                      'prefix':[],
                                      'text':[],
                                      })

    def add_sample(self,text,model_name,iters,prefix=None):
        self.csv = pd.append(self.csv,
                             pd.DataFrame({ 'model':[model_name],
                                            'iters':[iters],
                                            'prefix':[prefix],
                                            'text':[text],
                             }))

    def save(self):
        self.csv.to_csv(self.storefile)

