# Pharmacy Contract Automation

This project automates the generation of customized pharmacy contracts using a Word template and pharmacy data. The script reads data from a JSON file, replaces placeholders in the template with actual values, and saves the customized contracts as new Word documents.

## Features

- **Dynamic Data Replacement:** Automatically replace placeholders in the Word template with specific data for each pharmacy.
- **Modular Code:** Easy-to-maintain and extend codebase with clear separation of functionalities.
- **Configuration Files:** Externalized data storage to avoid exposing sensitive information.
- **Error Handling:** Robust checks to ensure the template and data files are present before processing.

## Getting Started

### Prerequisites

- Python 3.x
- `python-docx` library (install via `pip install python-docx`)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/pharmacy-contract-automation.git
    cd pharmacy-contract-automation
    ```

2. Install the required library:

    ```bash
    pip install python-docx
    ```

3. Create a `pharmacies.json` file in the `data` directory with your actual data, following the format shown in the `pharmacies_example.json` file:

    ```json
    [
        {
            "nomDocteur": "Doctor Name",
            "nomPharmacie": "Pharmacy Name",
            "telephonePh": "Phone Number",
            "emailPha": "Email"
        }
    ]
    ```

4. Ensure the `pharmacies.json` file is listed in the `.gitignore` to prevent it from being pushed to the repository.

### Running the Script

To generate the contracts, run the main script:

```bash
python src/main.py
