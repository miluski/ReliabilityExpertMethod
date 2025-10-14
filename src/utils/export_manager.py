def export_to_csv(data, filename):
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def export_to_pdf(data, filename):
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.output(filename)

def export_results(data, format='csv', filename='results'):
    if format == 'csv':
        export_to_csv(data, f"{filename}.csv")
    elif format == 'pdf':
        export_to_pdf(data, f"{filename}.pdf")
    else:
        raise ValueError("Unsupported format. Please choose 'csv' or 'pdf'.")