import os
import struct

def get_image_info(file_path):
  if not os.path.exists(file_path):
    print(f"Error: File {file_path} not found.")
    return None
  
  try:
    with open(file_path, 'rb') as file:
      header = file.read(24)

      if header.startswith(b'\xFF\xD8\xFF'):
        file.seek(0)

        file_size = os.path.getsize(file_path)

        while True:
          marker = file.read(2)
          if marker[0] != 0xFF:
            break

          if marker[1] >= 0xC0 and marker[1] <= 0xCF and marker[1] != 0xC4 and marker[1] != 0xC8:
            length = struct.unpack('>H', file.read(2))[0]
            bits = file.read(1)[0]
            height, width = struct.unpack('>HH', file.read(4))
            return {
              'format': 'JPEG',
              'width' : width,
              'height': height,
              'bit_depth': bits,
              'file_size': file_size
            }
          
          size = struct.unpack('>H', file.read(2))[0]
          file.seek(size - 2, 1)

        return {
          'format':'JPEG',
          'file_size': file_size,
          'width': 'Unknown',
          'height': 'Unknown'
        }
      elif header.startswith(b'\x89Png\r\n\x1a\n'):
        width = struct.unpack('>I', header[16:20])[0]
        height = struct.unpack('>I', header[16:20])[0]
        bit_depth = header[24]
        color_type = header[25]

        color_type = {
          0: 'Grayscale',
          2: 'RGB',
          3: 'Palette',
          4: 'Grayscale with alpha',
          6: 'RGBA'
        }

        return {
          'format': 'PNG',
          'width' : width,
          'height' : height,
          'bit_depth': bit_depth,
          'color_type': color_type.get(color_type, str(color_type)),
          'file_size': os.path.getsize(file_path)
        }
      
      elif header.startswith(b'GIF87a') or header.startswith(b'GIF89a'):
        width = struct.unpack('<H', header[6:8])[0]
        height = struct.unpack('<H', header[8:10])[0]
        packed = header[10]
        global_color_table = bool(packed & 0x80)
        color_resolution = ((packed & 0x70) >> 4) + 1
        bits_per_pixel = (packed & 0x07) + 1 if global_color_table else 0

        return {
          'format': 'GIF',
          'version': header[3:6].decode('ascii'),
          'width': width,
          'hieght': height,
          'global color_table': global_color_table,
          'color_resolution': color_resolution,
          'bits_per_pixel': bits_per_pixel,
          'file_size': os.path.getsize(file_path)
        }
      elif header.startswith(b'BM'):
        file_size = struct.unpack('<I', header[2:6])[0]
        width = struct.unpack('<I', header[18:22])[0]
        height = struct.unpack('<I', header[22:26])[0]
        bits_per_pixel = struct.unpack('<I', header[28:30])[0]

        return {
          'format': 'BMP',
          'width': width,
          'height' : height,
          'bits_per_pixel': bits_per_pixel,
          'file_size': file_size
        }
      
      else:
        return{
          'format': 'Unkown',
          'file_size': os.path.getsize(file_path)
        }
  except Exception as e:
    print(f"Image info check error: {e}")
    return None

def print_image_info(info):
  if not info:
    return
  
  print("\n--- Image Information ---")
  for key, value in info.items():
    print(f"{key}: {value}")

if __name__ == "__main__":
  print("=== Image Information Program ===")

  while True:
    file_path = input("\nImage file path (q to quit)")

    if file_path.lower() == 'q':
      print("Exiting program.")
      break

    info = get_image_info(file_path)
    print_image_info(info)