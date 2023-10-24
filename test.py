from install_dep import *
import os
import csv
import random

model = load_model("https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1")

# # Pick a random test image from the data directory
# test_img = random.choice([x for x in os.listdir('data') if os.path.isfile(os.path.join('data', x))])

# # Run it!
# path = "C:/Users/sshak/Documents/AIBenchmark/data/" + test_img

# inference_time, scores, entities = run_detector(model, path)
# print(inference_time)
# print(scores)
# print(entities)

# For each image in the data folder, run the detector and write the results to a csv file called results.csv 
# in the same folder as this script
with open('results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Image', 'Inference Time', 'Scores', 'Entities'])
    for img in os.listdir('data'):
        path = "C:/Users/sshak/Documents/AIBenchmark/data/" + img
        inference_time, scores, entities = run_detector(model, path)
        writer.writerow([img, inference_time, scores, entities])
        