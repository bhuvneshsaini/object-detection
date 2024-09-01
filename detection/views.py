from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from PIL import Image, ImageDraw, ImageFont
import io
import base64
from .load_model import model


class ObjectDetectionAPI(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            # Extract and open the uploaded image
            file = request.data['file']
            image = Image.open(file)

            # Perform object detection
            results = model(image)

            # Process detection results
            annotations = results.pandas().xyxy[0].to_dict(orient="records")

            # Annotate the image with bounding boxes and labels
            annotated_image = self.annotate_image(image, results)

            # Prepare response data
            response_data = {
                "annotations": annotations,
                "annotated_image": self.image_to_base64(annotated_image),
            }

            return Response(response_data)

        except Exception as e:
            return Response({"error": str(e)}, status=400)

    def annotate_image(self, image, results):
        # Create a copy of the image to draw annotations
        annotated_image = image.copy()
        draw = ImageDraw.Draw(annotated_image)

        # Font settings for label
        font = ImageFont.load_default()

        # Draw bounding boxes and labels
        for detection in results.xyxy[0]:
            xmin, ymin, xmax, ymax, confidence, cls = detection.tolist()
            label = f"{results.names[int(cls)]} {confidence:.2f}"
            draw.rectangle([(xmin, ymin), (xmax, ymax)], outline='red', width=2)
            draw.text((xmin, ymin), label, fill='red', font=font)

        return annotated_image

    def image_to_base64(self, image):
        # Convert PIL Image to base64 encoded string
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')


