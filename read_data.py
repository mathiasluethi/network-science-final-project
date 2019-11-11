import geopandas as gpd
import fiona 
#create a list of layers with in a file geodatabase 
layerlist = fiona.listlayers('./final-project/Schienennetz_LV03_20171210.gdb')
print(layerlist)
netzknoten = gpd.read_file('./final-project/Schienennetz_LV03_20171210.gdb',layer='Netzknoten')
display(netzknoten.head())
netzsegment = gpd.read_file('./final-project/Schienennetz_LV03_20171210.gdb',layer='Netzsegment')
display(netzsegment.head())
print(len(netzknoten))
#for i in sorted(layerlist):
#    df1 = gpd.read_file('./final-project/Schienennetz_LV03_20171210.gdb',layer=i)