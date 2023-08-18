**Image Optimization and Enhancement Script for Web Portfolio**

I've developed a Python script that addresses the challenge of optimizing and enhancing large images for web usage, utilizing the Python Imaging Library (PIL), also known as the Pillow library. The primary goal of this project is to significantly reduce the file sizes of images while maintaining visual quality and making them suitable for web-based platforms. I achieved this by leveraging the capabilities of the Pillow library to process images and apply enhancements to their appearance.

**Key Features:**

1. **Image Size Optimization:** The script takes input images from a specified directory and resizes them to a target resolution of 1920x1080 pixels. This ensures that the images fit well within the common display dimensions of modern web browsers, improving the user experience.

2. **Enhancement Adjustments:** The script goes beyond simple resizing by incorporating enhancement adjustments to improve the visual quality of images. It allows users to customize the degree of contrast, brightness, and saturation through user-defined factors.

3. **File Format and Compression:** The script supports both JPEG and PNG input images. The output images are saved in JPEG format with optimized settings, including reduced quality to further minimize file sizes while preserving acceptable image quality.

**How to Use:**

1. **Input Directory:** Set the `input_directory` variable to the path containing the images you want to optimize and enhance.

2. **Output Directory:** Specify the `output_directory` where the processed images will be saved.

3. **Target Size:** Define the `target_size` tuple with the desired dimensions for the optimized images.

4. **Enhancement Factors:** Adjust the `contrast_factor`, `brightness_factor`, and `saturation_factor` according to your preferences. Higher values result in stronger enhancements.

5. **Supported Formats:** The script processes both JPEG and PNG images. Place your images in the input directory with these formats for processing.

6. **Running the Script:** Execute the script, and it will iterate through the input directory, process the images, and save the optimized versions in the output directory.

**Example Usage:**

Suppose you have a collection of high-resolution property images in the input directory. By running the script, these images will be resized to the target dimensions, while enhancements like improved contrast, brightness, and saturation will be applied. The resulting images, now significantly smaller in file size, are ready for seamless integration into your web portfolio.

This project showcases my ability to combine image processing techniques with automation to solve practical challenges. It's a valuable addition to my portfolio, demonstrating how I optimize images for web usage without compromising on visual appeal.
