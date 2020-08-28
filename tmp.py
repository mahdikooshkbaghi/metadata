import pandas as pd
import numpy as np

excel_file = pd.read_excel('./metadata_smn2T6C.xlsx', sheet_name=None)
sample_sheet = excel_file['samples']
read_sheet   = excel_file['reads']

LID = int(304987003)
sample_name = ['smn1_5sslib_ssbc_lib1','smn2T6C_lib2_DNA_good', 'smn2T6C_lib2_RNA_total']

sample_dict = {}
for sample in sample_name:
     idx = sample_sheet.index[(sample_sheet['LID']==LID) & (sample_sheet['sample']==sample)].tolist()
     # Get the name of the amplicon for read1 of current sample
     read1_amp = sample_sheet['read1'][idx]
     ## Find the regex index corresponding to read1_amp
     jdx = list(np.where(read_sheet['read'].values==read1_amp.values)[0])
     sample_dict[sample]={}
     sample_dict[sample]['read1']=read_sheet['regex'][jdx].tolist()[0]
 
     ## Take union of the features
     features_col       = sample_sheet['features'][idx].tolist()
     features_item = []
     for item in features_col:
         features_item.append(item.split(','))
     features_list = list(set().union(*features_item))
     # Remove whitespaces
     features_list = [x.strip(' ') for x in features_list]
 
     sample_dict[sample]['features_list']=features_list

st = sample_sheet[sample_sheet['sample']=='smn2T6C_lib2_DNA_good']['barcode']
print(st.values)
