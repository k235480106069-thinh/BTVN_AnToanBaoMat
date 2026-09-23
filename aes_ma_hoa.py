# Cài đặt thư viện trước khi chạy: pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def aes_encrypt(plaintext, key):
    # Tạo đối tượng mã hóa AES ở chế độ EAX
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    # Mã hóa dữ liệu
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    return nonce, ciphertext, tag

def aes_decrypt(nonce, ciphertext, tag, key):
    # Tạo đối tượng giải mã AES
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    # Giải mã và xác thực
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode('utf-8')

if __name__ == "__main__":
    # Khởi tạo khóa ngẫu nhiên 16 bytes (128-bit) cho AES
    secret_key = get_random_bytes(16)
    
    data_to_encrypt = "Đây là thông điệp bí mật cho bài tập An toàn thông tin."
    print("Dữ liệu gốc:", data_to_encrypt)

    # Quá trình mã hóa
    nonce, ciphertext, tag = aes_encrypt(data_to_encrypt, secret_key)
    print("Dữ liệu đã mã hóa (Ciphertext):", ciphertext)

    # Quá trình giải mã
    decrypted_data = aes_decrypt(nonce, ciphertext, tag, secret_key)
    print("Dữ liệu sau khi giải mã:", decrypted_data)