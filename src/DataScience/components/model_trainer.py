import pandas as pd
import os
from src.DataScience import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.DataScience.entity.config_entity import ModelTrainingConfig

class ModelTrainer:
    def __init__(self,config:ModelTrainingConfig):
        self.config = config
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        train_x = train_data.drop([self.config.target_column],axis=1)
        test_x = test_data.drop([self.config.target_column],axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]
        
        lr = ElasticNet(alpha=self.config.alpha,l1_ratio=self.config.l1_ratio)
        lr.fit(train_x,train_y)
        
        joblib.dump(lr,os.path.join(self.config.root_dir,self.config.model_name))
        