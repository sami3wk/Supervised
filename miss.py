def catconsep(df):
    cat = []
    con = []
    for i in df.columns:
        if(df[i].dtypes == "object"):
            cat.append(i)
        else:
            con.append(i)
    return cat,con



def replacer(df):
    misscols=[]
    rowcount = df.shape[0]
    for i in df.columns:
        if(df[i].count() < rowcount):
            misscols.append(i)
    
    cat,con = catconsep(df[misscols])
    for i in cat:
        x = df[i].mode()[0]
        df[i]=df[i].fillna(x)

    for i in con:
        x = round(df[i].mean(),2)
        df[i]=df[i].fillna(x)

        
def preprocessing(X):
    import pandas as pd
    cat = []
    con = []
    for i in X.columns:
        if(X[i].dtypes == "object"):
            cat.append(i)
        else:
            con.append(i)

    from sklearn.preprocessing import StandardScaler
    ss = StandardScaler()
    X1 = pd.DataFrame(ss.fit_transform(X[con]),columns=con)
    X2 = pd.get_dummies(X[cat])
    X3 = X1.join(X2)
    return X3