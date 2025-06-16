# 📘 Agent calling Wikipedia and Math

> GenAI Agent that has 2 tools: Wikipedia and Math. It can, e.g., compute (3 * AverageDogAge) for you!
Version 1: achieves this functionality, but levereges libraries that are going to be depricated.
Version 2: refactors the tool in order to use more modern libraries.
Version 3: further modernization of the tool through using more modern libraries.  

---

## 🔧 Features

- ✅ Search Wikipedia
- ✅ Execute simple math

---

## 🗂️ Project Structure

```bash
📁 1_Wikipedia_and_Math/
├── agent_langchain_v1.py
├── agent_langchain_v2.py
├── agent_langchain_v3.py
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the main script**
   ```bash
   python agent_langchain_v3.py
   ```

3. *(Optional)* Set up `.env` or config file if credentials are needed

---

## 📊 Inputs and Outputs

| Input | Description |
|-------|-------------|
| `user_query` | Example: "What is the average dog age? Multiply by 3." |

| Output | Description |
|--------|-------------|
| `Answer` | AI-generated response using tools and reasoning |

---

## 🧠 How It Works

- **LLM**: Gemini via Google API
- **Tools**: Wikipedia search, calculator
- **Framework**: LangChain agent (ReAct / Tool-Calling / Planner-Executor)

---

## 📄 References

- [LangChain Docs](https://docs.langchain.com/)
- [LangChain Intro](https://python.langchain.com/docs/get_started/introduction.html)
- [Agent Patterns](https://smith.langchain.com/)

---

## 👨 Author

**Alexander Andrianov**  
Quant → Climate Risk → Agentic AI  
PhD Math | MITx MicroMasters | ex-PwC

[GitHub](https://github.com/AndrianovAL) · [LinkedIn](https://www.linkedin.com/in/alexander--andrianov)
