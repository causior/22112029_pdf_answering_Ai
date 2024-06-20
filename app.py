st.title('PDF Question-Answering System')

# File uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Text input for the question
question = st.text_input("Enter your question:")

# Submit button
if st.button('Submit'):
    if uploaded_file is not None and question:
        # Read the PDF file and extract text
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Get the answer from the model
        answer = answer_question(question, text, model, tokenizer)

        # Display the answer
        st.write("**Answer:**", answer)
    else:
        st.write("Please upload a PDF file and enter a question.")
