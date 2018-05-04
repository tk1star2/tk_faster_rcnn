NET=res101
TRAIN_IMDB=KITTI_trainval
GPU_ID=0

CUDA_VISIBLE_DEVICES=${GPU_ID} OMP_NUM_THREADS=4 ./tools/demo.py --net ${NET} --dataset KITTI 
