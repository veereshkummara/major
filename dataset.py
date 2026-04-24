import kagglehub

# Download latest version
path = kagglehub.dataset_download("abhishekunnam/meeting-transcripts")

print("Path to dataset files:", path)