import pytest
import tempfile
import os
from file_upload.utils.encryption import encrypt_file, decrypt_file

@pytest.mark.parametrize("content", [b"hello world", b"secure file"])
def test_encryption_decryption(content):
    """Test that files can be encrypted and decrypted correctly."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(content)
        temp_file.close()

        encrypt_file(temp_file.name)
        decrypt_file(temp_file.name)

        with open(temp_file.name, "rb") as f:
            decrypted_data = f.read()

    assert decrypted_data == content
    os.remove(temp_file.name)  # Clean up
