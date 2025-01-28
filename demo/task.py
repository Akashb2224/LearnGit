import  PyPDF2

class file:

    def open_file(self,file_path):
        self.doc= library.open(file_path)

    def save_pdf(self,output_path):
        self.doc.save(output_path)
        self.doc.close()

    def add_text_to_file(self, text, page,x,y):
        page = self.doc.load_page(page_number)
        page.insert_text((x,y),text)

    file= file()
    file.add_text_to_file
