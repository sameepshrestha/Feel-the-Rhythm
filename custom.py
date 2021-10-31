class Modelss:
    def __init__(self,model):
        self.models=model
    def fit(self,X_train,y_train):
        return (self.models.fit(X_train,y_train))
    def predict(self,X_valid):
        return self.models.predict_proba(X_valid)[:,1]