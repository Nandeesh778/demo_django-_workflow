import pdfkit
import cairosvg
from html2image import Html2Image
hti = Html2Image()

def convert_html_file_to_pdf(html_file_path, output_file_path, type, output_pdf_file_path):
    """
    Convert HTML file to PDF.

    Args:
        html_file_path (str): Path to the HTML file.
        output_file_path (str): Path to save the output PDF file.
        
    """

    if(type == "pdf"):
        try:
            options = {
                'page-size': 'A4',
                'margin-top': '0mm',
                'margin-right': '0mm',
                'margin-bottom': '0mm',
                'margin-left': '0mm',
            }
            print("html_file_path>>>>>>>>>>", html_file_path)
            pdfkit.from_file(html_file_path, output_file_path, options=options)
            print(f'PDF successfully created at: {output_file_path}')
        except FileNotFoundError as e:
            print(f'HTML file not found: {html_file_path}')
        except Exception as e:
            print(f'Error converting HTML to PDF: {e}')

    elif(type == "svg"):
        #write a code to convert html to svg
        # try:
        #     with open(html_file_path, 'rb') as html_file:
        #         svg_data = cairosvg.svg2svg(file_obj=html_file)
        
        #     with open(output_file_path, 'wb') as svg_file:
        #         svg_file.write(svg_data)

        #     print(f'SVG successfully created at: {output_file_path}')
        # except FileNotFoundError as e:
        #     print(f'HTML file not found: {html_file_path}')
        # except Exception as e:
        #     print(f'Error converting HTML to SVG: {e}')
         #Assuming hti.screenshot captures HTML content and saves it to an image
        #hti.screenshot(html_file=html_file_path, save_as='temp_img.svg')
    
        # Convert the temporary image to SVG using cairosvg
        # cairosvg.svg2svg(url='temp_img.png', write_to=output_file_path)
        # try:
        #     cairosvg.svg2svg(url=html_file_path, write_to=output_file_path)
        # except Exception as e:
        #  print(f"Error converting image to SVG: {e}")
        from weasyprint import HTML
        HTML(filename=html_file_path).write_pdf(output_pdf_file_path)
        from cairosvg import svg2svg

        # Convert PDF to SVG using cairosvg
        svg2svg(url=output_pdf_file_path, write_to=output_file_path)



        

    elif(type == "img"):
        #write a code to convert html to img
        hti.screenshot(html_file=html_file_path,save_as='blue_page.png')
        

if __name__ == "__main__":
    type = "svg"
    # Input HTML file path
    html_file_path = "/home/nandeesh/Desktop/demo_django/mypro/myapp/input.html"
    output_pdf_file_path = "/home/nandeesh/Desktop/demo_django/mypro/myapp/output.pdf"

    # Output PDF file path
    output_file_path = "/home/nandeesh/Desktop/demo_django/mypro/myapp/output.svg"

    convert_html_file_to_pdf(html_file_path, output_file_path, type, output_pdf_file_path)
