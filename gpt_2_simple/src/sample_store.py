import csv

class SampleStore:

    def __init__(self, storefile='samplestore.csv'):

        print("sstore init")
        self.storefile = storefile


    def add_sample(self,text,model_name,iters,prefix=None):
        print("sstore add sample")

        with open(self.storefile, 'a+') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([model_name,iters,prefix,text])
        
