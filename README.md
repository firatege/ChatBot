# **Retrieval-Based Personal Assistant Chatbot(DROPED)**



This project is a **retrieval-based chatbot** designed to assist users in their daily lives. The bot can answer predefined questions, retrieve stored information, and help users manage their day-to-day tasks. The project is built using Python and PostgreSQL.

---

## **Current Progress**

1. **Intent Classification**  
   - Implemented using **TF-IDF** to analyze and determine the user's intent.  
   - Extracts the closest intent from a predefined set of intents.  

2. **Entity Recognition**  
   - Integrated **POS Tagging** for identifying key entities in user messages.  
   - Captures important elements such as dates, tasks, and locations.

3. **Response Selection**  
   - Responses are retrieved using **TF-IDF + Similarity** for finding the closest matching answer from the database.  
   - A predefined response pool is stored in the PostgreSQL database.

4. **Database Structure**  
   - A basic schema for response storage has been created, including user messages, intents, entities, and context.  
   - All questions and responses are organized for retrieval-based selection.

---

## **Planned Improvements**

1. **Context Management**  
   - Add a system to maintain conversational context for multi-turn conversations.

2. **Dynamic Database Integration**  
   - Enable users to add new questions and responses dynamically to the database.  

3. **Advanced Entity Recognition**  
   - Enhance entity extraction with pre-trained models like spaCy or word embeddings.  

4. **Natural Language Understanding (NLU)**  
   - Improve accuracy by experimenting with transformer-based models like BERT for intent classification.  

5. **User Personalization**  
   - Allow the bot to track user preferences, habits, and personal schedules over time.  

6. **Logging and Monitoring**  
   - Implement logs for user interactions and response selections to improve performance.  

7. **Error Handling**  
   - Add fallback responses when the system cannot find a suitable match.  

---

## **Future Vision**

This chatbot will evolve into a personal assistant capable of:  
- Managing personal schedules seamlessly.  
- Providing accurate responses based on real-time data.  
- Adapting to user behavior and improving its knowledge base.  

---

### **Technologies Used**

- **Python**: Core language for logic and implementation.  
- **PostgreSQL**: Database for storing questions, responses, and context.  
- **NLTK**: For text processing and POS tagging.  
- **Scikit-learn**: For TF-IDF and similarity computations.  

---

