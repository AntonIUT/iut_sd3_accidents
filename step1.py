import pandas as pd

carac = pd.read_csv("carac.csv",sep=';',dtype=str)
lieux = pd.read_csv("lieux.csv",sep=';',dtype=str)
veh = pd.read_csv("veh.csv",sep=';',dtype=str)
vict = pd.read_csv("vict.csv",sep=';',dtype=str)

victime = vict.merge(veh,on=['Num_Acc','num_veh'])
accident = carac.merge(lieux,on = 'Num_Acc')
victime = victime.merge(accident,on='Num_Acc')

victime.to_csv('merged_data.csv', index=False)
