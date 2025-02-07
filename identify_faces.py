import face_recognition
from PIL import Image, ImageDraw
from PIL import ImageFont

bill_image = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(bill_image)[0]

steve_image = face_recognition.load_image_file('./img/known/Steve Jobs.jpg')
steve_face_encoding = face_recognition.face_encodings(steve_image)[0]

known_face_encodings = [
    bill_face_encoding,
    steve_face_encoding
]

known_names = [
  'Bill Gates',
    'Steve Jobs'
]

test_image = face_recognition.load_image_file('./img/groups/bill-steve-elon.jpg')

find_faces = face_recognition.face_locations(test_image)
test_image_face_encoding = face_recognition.face_encodings(test_image, find_faces)

pil_image = Image.fromarray(test_image)

draw = ImageDraw.Draw(pil_image)


for (top, right, bottom, left), test_image_face_encoding in zip(find_faces, test_image_face_encoding):
  matches = face_recognition.compare_faces(known_face_encodings, test_image_face_encoding)
  name = "Unknown Person"

  if True in matches:
    first_match_index = matches.index(True)
    name = known_names[first_match_index]

  draw.rectangle(((left, top), (right, bottom)), outline = (0,0,0))

  font = ImageFont.load_default()  # Load a font (ensure you import ImageFont)
  bbox = draw.textbbox((0, 0), name, font=font)
  text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]  # Extract width & height

  draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
  draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255))

del draw

pil_image.show()
#pil_image.save(f'{top}.jpg')

