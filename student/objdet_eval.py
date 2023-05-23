# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Evaluate performance of object detection
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# general package imports
import numpy as np
import matplotlib
#matplotlib.use('wxagg') # change backend so that figure maximizing works on Mac as well     
import matplotlib.pyplot as plt

import torch
from shapely.geometry import Polygon
from operator import itemgetter

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# object detection tools and helper functions
import misc.objdet_tools as tools


# compute various performance measures to assess object detection
def measure_detection_performance(detections, labels, labels_valid, min_iou=0.5):   
    # find best detection for each valid label 
    num_true_positives = 0  # number of correctly detected objects
    center_deviations = []
    iou_scores = []   
    for label, is_valid in zip(labels, labels_valid):
        matched_label_detections = []       
        if is_valid:  # exclude all labels from statistics that are not considered valid            
            # compute intersection over union (iou) and distance between centers
            ####### ID_S4_EX1 START #######     
            #######
            print("student task ID_S4_EX1 ")
            ## Step 1: Extract the four corners of the current label bounding box
            bbox = label.box
            label_corners = tools.compute_box_corners(x=bbox.center_x, y=bbox.center_y,
                                                      w=bbox.width, l=bbox.length,
                                                      yaw=bbox.heading)           
            ## Step 2: Loop over all detected objects
            for detection in detections:                
                ## Step 3: Extract the four corners of the current detection
                det_id, det_x, det_y, det_z, det_h, det_w, det_l, det_yaw = detection
                detection_corners = tools.compute_box_corners(det_x, det_y, det_w, det_l, det_yaw)                
                ## Step 4: Compute the center distance between the label and detection bounding box in x, y, and z
                center_dist_x = bbox.center_x - det_x
                center_dist_y = bbox.center_y - det_y
                center_dist_z = bbox.center_z - det_z              
                ## Step 5: Compute the intersection over union (IOU) between the label and detection bounding box
                label_poly = Polygon(label_corners)
                detection_poly = Polygon(detection_corners)
                intersection_area = label_poly.intersection(detection_poly).area
                union_area = label_poly.union(detection_poly).area                
                iou = intersection_area / union_area
                
                ## Step 6: If IOU exceeds the min_iou threshold, store [iou, center_dist_x, center_dist_y, center_dist_z] in matched_label_detections and increase the true positive count
                if iou > min_iou:
                    matched_label_detections.append([iou, center_dist_x, center_dist_y, center_dist_z])
                    num_true_positives += 1
        #######
        ####### ID_S4_EX1 END #######     
        # Find the best match and compute metrics
        if matched_label_detections:
            best_match = max(matched_label_detections, key=itemgetter(1))  # retrieve entry with max iou in case of multiple candidates
            iou_scores.append(best_match[0])
            center_deviations.append(best_match[1:])
    ####### ID_S4_EX2 START #######     
    #######
    print("student task ID_S4_EX2")
    # compute positives and negatives for precision/recall
    num_labels = len(labels)
    ## Step 1: Compute the total number of positives present in the scene
    all_positives = labels_valid.sum()
    ## Step 2: Compute the number of false negatives
    false_negatives = all_positives - num_true_positives
    ## Step 3: Compute the number of false positives
    false_positives = len(detections) - num_true_positives
        #######
    ####### ID_S4_EX2 END #######   
    det_performance = [iou_scores, center_deviations, [all_positives, num_true_positives, false_negatives, false_positives]]
    
    return det_performance


# evaluate object detection performance based on all frames
def compute_performance_stats(det_performance_all, configs):
    # extract elements
    iou_scores = []
    center_deviations = []
    pos_neg_counts = []
    for item in det_performance_all:
        iou_scores.append(item[0])
        center_deviations.append(item[1])
        pos_neg_counts.append(item[2])

    ####### ID_S4_EX3 START #######     
    #######    
    print('student task ID_S4_EX3')

    ## step 1 : extract the total number of positives, true positives, false negatives and false positives
    print(pos_neg_counts)

    total_positives, true_positives, false_negatives, false_positives = np.array(pos_neg_counts).sum(axis=0)

    ## step 2 : compute precision
    precision = true_positives / (true_positives + false_positives)

    ## step 3 : compute recall 
    recall = true_positives / (true_positives + false_negatives)

    #######    
    ####### ID_S4_EX3 END #######     
    print('precision = ' + str(precision) + ", recall = " + str(recall))    

    # serialize intersection-over-union and deviations in x,y,z
    ious_all = [element for tupl in iou_scores for element in tupl]
    devs_x_all = []
    devs_y_all = []
    devs_z_all = []
    for tuple in center_deviations:
        for elem in tuple:
            dev_x, dev_y, dev_z = elem
            devs_x_all.append(dev_x)
            devs_y_all.append(dev_y)
            devs_z_all.append(dev_z)
    

    # compute statistics
    stdev__ious = np.std(ious_all)
    mean__ious = np.mean(ious_all)

    stdev__devx = np.std(devs_x_all)
    mean__devx = np.mean(devs_x_all)

    stdev__devy = np.std(devs_y_all)
    mean__devy = np.mean(devs_y_all)

    stdev__devz = np.std(devs_z_all)
    mean__devz = np.mean(devs_z_all)
    #std_dev_x = np.std(devs_x)

    # plot results
    data = [precision, recall, ious_all, devs_x_all, devs_y_all, devs_z_all]
    titles = ['detection precision', 'detection recall', 'intersection over union', 'position errors in X', 'position errors in Y', 'position error in Z']
    textboxes = ['', '', '',
                 '\n'.join((r'$\mathrm{mean}=%.4f$' % (np.mean(devs_x_all), ), r'$\mathrm{sigma}=%.4f$' % (np.std(devs_x_all), ), r'$\mathrm{n}=%.0f$' % (len(devs_x_all), ))),
                 '\n'.join((r'$\mathrm{mean}=%.4f$' % (np.mean(devs_y_all), ), r'$\mathrm{sigma}=%.4f$' % (np.std(devs_y_all), ), r'$\mathrm{n}=%.0f$' % (len(devs_x_all), ))),
                 '\n'.join((r'$\mathrm{mean}=%.4f$' % (np.mean(devs_z_all), ), r'$\mathrm{sigma}=%.4f$' % (np.std(devs_z_all), ), r'$\mathrm{n}=%.0f$' % (len(devs_x_all), )))]

    f, a = plt.subplots(2, 3)
    a = a.ravel()
    num_bins = 20
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    for idx, ax in enumerate(a):
        ax.hist(data[idx], num_bins)
        ax.set_title(titles[idx])
        if textboxes[idx]:
            ax.text(0.05, 0.95, textboxes[idx], transform=ax.transAxes, fontsize=10,
                    verticalalignment='top', bbox=props)
    plt.tight_layout()
    plt.show()
