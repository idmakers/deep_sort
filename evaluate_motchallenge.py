# vim: expandtab:ts=4:sw=4
import argparse
import os
import deep_sort_app
from time import time

def parse_args():
    """ Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description="MOTChallenge evaluation")
    parser.add_argument(
        "--mot_dir", help="Path to MOTChallenge directory (train or test)",default="E:/OBJECT_DECTECT/MOT17/train")
    parser.add_argument(
        "--detection_dir", help="Path to detections.",default="E:/OBJECT_DECTECT/deep_sort/MOT17")
    parser.add_argument(
        "--output_dir", help="Folder in which the results will be stored. Will "
        "be created if it does not exist.", default="results/MOT17-001")
    parser.add_argument(
        "--min_confidence", help="Detection confidence threshold. Disregard "
        "all detections that have a confidence lower than this value.",
        default=0.5, type=float)
    parser.add_argument(
        "--min_detection_height", help="Threshold on the detection bounding "
        "box height. Detections with height smaller than this value are "
        "disregarded", default=0, type=int)
    parser.add_argument(
        "--nms_max_overlap",  help="Non-maxima suppression threshold: Maximum "
        "detection overlap.", default=1.0, type=float)
    parser.add_argument(
        "--max_cosine_distance", help="Gating threshold for cosine distance "
        "metric (object appearance).", type=float, default=0.2)
    parser.add_argument(
        "--nn_budget", help="Maximum size of the appearance descriptors "
        "gallery. If None, no budget is enforced.", type=int, default=100)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    

    os.makedirs(args.output_dir, exist_ok=True)
    sequences = os.listdir(args.mot_dir)
    run_time = os.path.join(args.output_dir, "time.txt" )
    f=open(run_time,'w')
    for sequence in sequences:
        
        print("Running sequence %s" % sequence)
        sequence_dir = os.path.join(args.mot_dir, sequence)
        detection_file = os.path.join(args.detection_dir, "%s.npy" % sequence)
        output_file = os.path.join(args.output_dir, "%s.txt" % sequence)
        
        start = time()
        deep_sort_app.run(
            sequence_dir, detection_file, output_file, args.min_confidence,
            args.nms_max_overlap, args.min_detection_height,
            args.max_cosine_distance, args.nn_budget, display=False)
     
        end = time()
        
        if sequence[0:8] == 'MOT17-02':
            num_frames = 600
        elif sequence[0:8] == 'MOT17-04':
             num_frames = 1050
        elif sequence[0:8] == 'MOT17-05':
             num_frames = 837
        elif sequence[0:8] == 'MOT17-10':
             num_frames = 654
        elif sequence[0:8] == 'MOT17-11':
             num_frame = 900
        elif sequence[0:8] == 'MOT17-13':
              num_frames = 750
        elif sequence[0:8] == 'MOT17-13':
              num_frames = 525
        time_run ="finished " + sequence + " at " + str(int(num_frames / (end - start))) + " fps!"
        print(time_run,file=f)
    f.close()
   
