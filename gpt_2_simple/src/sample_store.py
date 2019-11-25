import pandas as pd

class SampleStore:

    def __init__(self, storefile='samplestore.csv'):

        print("sstore init")
        self.storefile = storefile

        self.openOrCreate()


    def openOrCreate(self):
        print("sstore open")

        try:
            self.csv = pd.read_csv(self.storefile)
        except:
            self.csv = pd.DataFrame({ 'model':[],
                                      'iters':[],
                                      'prefix':[],
                                      'text':[],
                                      })

    def add_sample(self,text,model_name,iters,prefix=None):
        print("sstore add sample")

        self.csv = pd.append(self.csv,
                             pd.DataFrame({ 'model':[model_name],
                                            'iters':[iters],
                                            'prefix':[prefix],
                                            'text':[text],
                             }))
        self.save()

    def save(self):
        print("sstore save")
                
        self.csv.to_csv(self.storefile)

