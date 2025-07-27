# Image-Analyze
## How to Use

1. Install dependencies:

pip install -r requirements.txt

2. Start the server:

python -m app.run

3. POST request `/main/document/analyze` 
form-data:
   - Key: `file`
   - Value: (Select a single image file: PNG, JPG, or JPEG)

4. POST request `/main/openai/analyze` 
form-data:
   - Key: `file`
   - Value: (Select a single image file: PNG, JPG, or JPEG)

5. Using curl:
   ```
   curl -X POST -F "file=@your_image.jpg" http://127.0.0.1:5000/main/document/analyze
   ```

