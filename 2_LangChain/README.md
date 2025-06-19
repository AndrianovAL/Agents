# 📘 Agents with LangChain

> GenAI Engineer's portfolio for LangChain with Gemini and OpenAI.

---

## 🔧 Features

### 01-intro-AAL
- ✅ LangChain
- ✅ Prompts
- ✅ Chains
- ✅ LCEL
- ✅ Building a simple LLM powered assistant multimodal (gen text, gen img, structured output)

---

## 🗂️ Project Structure

```bash
📁 [folder-name]/
├── notebooks/
├── CONTRIBUTING.md
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## 🚀 How to Run

1. **Install dependencies**
   ```bash
    uv init NewFolderName --python 3.12.7
    cd NewFolderName
    rm main.py
    uv sync
    cursor .  # run via Cursor
    code .    # run via VS Code
   ```

2. **Run the scripts**
   ```bash
   run notebooks
   ```

3. *(Optional)* Set up `.env` or config file if credentials are needed

---

## 📊 Inputs and Outputs

### 01-intro-AAL
| Input | Description |
|-------|-------------|
| `article` | Example: "I like berries!" |

| Output | Description |
|--------|-------------|
| `title` | AI-generated title |
| `summary` | AI-generated summary |
| `new paragraph` | AI-generated paragraph and feedback |
| `image` | AI-generated image |

---

## 🧠 How It Works

- **LLM**: Google Gemini or OpenAI
- **Framework**: LangChain, LCEL

---

## 📄 References

- [LangChain Docs](https://docs.langchain.com/)
- [Agent Patterns](https://smith.langchain.com/)

---

## 👨 Author

**Alexander Andrianov**  
Quant → Climate Risk → Agentic AI  
PhD Math | MITx MicroMasters | ex-PwC

[GitHub](https://github.com/AndrianovAL) · [LinkedIn](https://www.linkedin.com/in/alexander--andrianov)
