# web-image optimization toolkit
## Files:
- `kmeans_comrepss.py`
    ```
    python kmeans_compress.py \
    --inputPath "your input image directory" \
    --outputPath "saved image folder" \
    --kcluster "how many colors want to be used in compressed image, default is 20" \
    --maxiters "how many iteratiosn for kmeans, default is 20"
    ```
- `optimize_images.py`
- `convert_web_images.py`: crop image and covert to webp format. **Make sure [webp installed/enabled](https://stackoverflow.com/questions/19860639/convert-images-to-webp-using-pillow) in your computer**
    ```bash
    python convert_web_images.py \
    --inputPath "your input image directory" \
    --outputPath "saved image folder" \
    --width 68 \
    --height 68 \
    --crop True #resize image if crop=False
    ```
  

