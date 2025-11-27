# 🩺 Health Management App — Disease / Symptom Recognition

**1. Introduction**

The Health Management App is an AI-powered medical image analysis system built using the Google Gemini 2.5 Flash Vision Model.
This app allows users to upload medical-related images (skin, wounds, infections, rashes, abnormalities) and receive an AI-generated analysis describing possible symptoms or conditions.

The system is designed for educational and awareness purposes, not clinical diagnosis.

**2. Objective**

The main objectives of this project are:

To recognize visible symptoms from medical images

To provide possible disease indications based on visual inspection

To offer safe and responsible suggestions

To identify whether professional diagnosis is needed

To create a simple interface for image-based health insights

**3. Technologies Used**
| Component             | Technology                       |
| --------------------- | -------------------------------- |
| Programming Language  | Python                           |
| Web Framework         | Streamlit                        |
| AI Model              | Google Gemini 2.5 Flash (Vision) |
| Image Processing      | Pillow (PIL)                     |
| Environment Variables | python-dotenv                    |

**4. System Workflow**
- User uploads image 
- Image converted to Gemini-readable format 
- System prompt + user question sent to Gemini 
- Gemini analyzes symptoms in the image 
- AI returns structured and safe medical feedback 
- Streamlit displays result

**5. Features**
**✔ Symptom Recognition**

**The system identifies visible signs such as:**
- Redness, Rash ,Inflammation,Wounds,Spots,Infections,Skin irregularities

✔ **Possible Conditions (Non-diagnostic)**

Provides a list of possible causes, not definitive diagnosis.

✔ **Doctor Advice**
**Suggests:**
- Whether to see a doctor
- Tests that may be needed
- Immediate precautions

✔ **Safety-Focused Output**

If image is unclear or misleading:

"A professional medical diagnosis is required."

**6. Prompt Used**

A structured system prompt ensures responsible medical insights:

- Identify symptoms
- Provide possible conditions
- Explain causes
- Suggest next steps
- No medicines recommended
- Safety-first, non-diagnostic response

**7. User Interface (Streamlit)**

**The UI provides:**
- Medical image upload
- Text box for custom questions
- Display of uploaded image
- AI-generated detailed analysis
- Clean, minimal design

**8. Results**

**The app produces:**
- A clear description of visible symptoms
- A list of potential conditions
- Causes and risk factors
- Recommended medical steps
- Safety guidance

**Example output:**

**Possible Condition**: Contact Dermatitis

**Visible Symptoms:** Red rash, swelling around the affected region

**Recommended Action:** Avoid irritant, consult dermatologist if irritation persists

**9. Conclusion**

The Health Management App demonstrates how AI vision models like Gemini can assist in:

- Early symptom awareness
- Health guidance
- Understanding skin and visual medical issues
- Non-invasive pre-assessment
- The system is not a replacement for professional medical diagnosis but acts as a supportive educational tool.

**10. Future Improvements**

- Add OCR recognition for medical reports
- Multi-image comparison
- Severity scoring
- PDF medical summary export
- Integration with wearable health data
