import numpy as np
import open3d as o3d
import torch

masks = torch.load('/content/scene0011_00_rgb_masks.pt')
pcd = o3d.io.read_point_cloud("/content/scene0011_00_vh_clean_2.ply")
features = np.load('/content/scene0011_00_vh_clean_2_openmask3d_features.npy')
