
import os
from pathlib import Path
import modal

from modal import App, Image

GPU = os.environ.get("GPU", "A10G")
TIMEOUT = int(os.environ.get("TIMEOUT", 720))
print(f"Using GPU {GPU}; TIMEOUT {TIMEOUT}")


import modal

import modal

image = modal.Image.from_dockerfile("Dockerfile")
app = App("RFantibody", image=image)

@app.function(image=image, gpu=GPU, timeout=TIMEOUT * 60)
def rfantibody():
    print("Running RFantibody")
    
@app.local_entrypoint()
def main():
    try:
        rfantibody().remote() 
    except Exception as e:
        print(e)
