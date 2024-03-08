from fpdf import FPDF

emailList = ["dev_fe@email.com", "example@email.com", "assestant@school.h", "cooordinator@fe.co"]

def encryptMessage(location, element):
    inputText = "I am peter parker. I am a professional freelance photographer."
    inputText_to_list = inputText.split()

    inputText_to_list.insert(location, " ")  # Insert a space at the specified location

    print(inputText_to_list)

    with open('encryptedMessageList.txt', 'a') as f:
        write_to_history = " ".join(inputText_to_list) + " <----> (" + element + ")"
        f.write(write_to_history)  # Write the encrypted message to the file for history
        f.write('\n')
        f.write('<----------------------------------------------------------------->')
        f.write('\n')

    return " ".join(inputText_to_list)  # Return the encrypted message


for index, element in enumerate(emailList):
    pdf = FPDF()
    # Add a page
    pdf.add_page()
    pdf.set_font("Arial", size = 15)

    # create a cell
    pdf.cell(200, 10, txt = encryptMessage(index + 1, element), 
            ln = 1, align = 'S')

    # save the pdf with name .pdf
    pdf.output(element+".pdf")
