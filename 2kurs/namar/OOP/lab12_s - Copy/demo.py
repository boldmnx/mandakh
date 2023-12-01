from werkzeug.utils import secure_filename

filename = "my file (1).txt"
secure_filename_result = secure_filename(filename)

print(f"Original Filename: {filename}")
print(f"Secure Filename: {secure_filename_result}")
