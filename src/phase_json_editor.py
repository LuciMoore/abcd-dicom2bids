import json
import glob
import os


bids_dir = '/home/groups/brainmri/adhd_asd/data/adhd_Y1-Y8_2022/niftis'
os.chdir(bids_dir)
sublist=glob.glob('sub-*/ses-*')
sublist.sort()

for i in sublist:
    if os.path.exists(os.path.join(bids_dir, i, 'fmap')):
        os.chdir(os.path.join(bids_dir, i, 'fmap'))

        phasejsons = glob.glob('*phasediff.json')
        phasejsons.sort()

        if len(phasejsons)>0:
            print(i)

            for p in phasejsons:
                with open(p, 'r') as f:
                    data = json.load(f)

                if 'EchoNumber' in data:
                    del data['EchoNumber']

                if 'EchoTime' in data:
                    del data['EchoTime']

                if 'EchoTime1' not in data:
                    data['EchoTime1'] = 0.00519
                    data['EchoTime2'] = 0.00765
                    data['B0FieldIdentifier'] = 'phasediff_fmap0'

                with open(p, 'w') as f:
                    json.dump(data, f, indent=4)
