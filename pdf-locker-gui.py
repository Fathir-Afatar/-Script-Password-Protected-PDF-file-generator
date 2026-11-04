# Standard Library
import os
import secrets
import string

# Third-party
from fpdf import FPDF
import pikepdf

# Determine the current folder location
output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output_locker")
os.makedirs(output_folder, exist_ok=True)


def generate_password(length=8):
    """Generates a secure random password using letters and digits.

    This function utilizes the `secrets` module to ensure cryptographically
    secure pseudorandom number generation, making it suitable for managing
    secrets such as account or file passwords.

    Args:
        length (int, optional): The length of the generated password. 
            Defaults to 8.

    Returns:
        str: A randomly generated password containing uppercase letters,
            lowercase letters, and digits.
    """
    charset = string.ascii_letters + string.digits
    return ''.join(secrets.choice(charset) for _ in range(length))


def generate_encrypted_pdfs(jumlah_file=100):
    """Creates multiple password-protected PDF files and logs their passwords.

    This function generates a specified number of unique PDF files, encrypts each
    one using a secure randomly generated password, and logs the filenames alongside
    their respective passwords into a text file. Temporary unencrypted files are 
    automatically cleaned up during the process.

    Args:
        jumlah_file (int, optional): The total number of encrypted PDF files 
            to generate. Defaults to 100.

    Returns:
        None

    Raises:
        FileNotFoundError: If the output directory cannot be created or accessed.
    """
    log_file_path = os.path.join(output_folder, "demo_passwords.txt")

    # Start the process
    with open(log_file_path, "w") as log:
        for i in range(1, jumlah_file + 1):
            nama_file = f"demo_{i:02d}.pdf"
            path_pdf = os.path.join(output_folder, nama_file)
            password = generate_password()

            # Create PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=14)
            pdf.multi_cell(0, 10, f"PDF Unlocker by Fathir\nFile ke-{i}")
            temp_pdf = os.path.join(output_folder, f"temp_{i:02d}.pdf")
            pdf.output(temp_pdf)

            # PDF Encryption
            with pikepdf.open(temp_pdf) as pdf_doc:
                pdf_doc.save(path_pdf, encryption=pikepdf.Encryption(owner=password, user=password, R=4))

            os.remove(temp_pdf)

            # Save password to log
            log.write(f"{nama_file} > {password}\n")
            print(f"[✓] {nama_file} made – Password: {password}")

    print(f"\n✅ Finished! {jumlah_file} Encrypted PDF files & password logs are stored in:\n{output_folder}")


if __name__ == "__main__":
    # Menjalankan proses pembuatan 100 file PDF terenkripsi
    generate_encrypted_pdfs(jumlah_file=100)

# To generate password, use this command
# python -m pdf-locker-gui