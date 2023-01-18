
import sys
import os
import json
import torch
import argparse
from thop import profile
sys.path.append('/opt/ml/input/final_project_level3-cv-16/')
from custom import SegformerForSemanticSegmentation, SegformerConfig, SegformerForImageClassification
from torchsummaryX import summary as _summary
from ptflops import get_model_complexity_info
from torchinfo import summary as info_summary
from time import time, localtime


def main(opt):
    
    dev = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    with open(os.path.join(opt.data_dir, 'id2label.json'), 'r') as f:
        id2label = json.load(f)
    id2label = {int(k): v for k, v in id2label.items()}
    label2id = {v: k for k, v in id2label.items()}
    
    ### from scratch training
    model = SegformerForSemanticSegmentation(
        SegformerConfig(
            num_labels=len(id2label), 
            id2label=id2label, 
            label2id=label2id, 
            ignore_mismatched_sizes=True)
    )
    
    # model = SegformerForImageClassification(SegformerConfig(
    #     num_labels=len(id2label), 
    #     # id2label=id2label, 
    #     # label2id=label2id
    # ))
    
    # torchsummaryX
    df = _summary(model, torch.randn(1, 3, 512, 512))
    df.to_csv('module_output.csv')
    
    model = model.to(dev)
    # thop
    input_vector = torch.randn(1, 3, 512, 512)
    macs, params = profile(model.cpu(), inputs= (input_vector,))
    print('flops',macs)
    print('params',params)
    print('FLOPs: %.3fG\tParams: %.3fM' % (macs / 1e9, params / 1e6), flush=True)
    
    # ptflops
    if os.path.isfile('module_output.txt'):
        os.remove('module_output.txt')
    prev_time = time()
    macs, params = get_model_complexity_info(model, (3, 512, 512), as_strings=True,
                                           print_per_layer_stat=True, verbose=True)
    print('{:<30}  {:<8}'.format('Computational complexity: ', macs))
    print('{:<30}  {:<8}'.format('Number of parameters: ', params))
    
    print(f'Total time : {time()-prev_time:.3f} sec')
    

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default="/opt/ml/input/data/ADEChallengeData2016")
    return parser.parse_args()

if __name__ == "__main__":
    opt = parse_args()
    main(opt)