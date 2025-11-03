# 🌊 HydroTrace AI
### Lightweight AI for Affordable Subsurface Exploration

---

## 🚀 Project Overview
**HydroTrace AI** is a lightweight artificial intelligence system that interprets **3D seismic data** to detect **geological features** like faults and rock layers — the same process used by major oil and gas exploration companies.

Unlike existing commercial tools that require **supercomputers and costly licenses**, HydroTrace AI runs efficiently on **regular laptops**, making advanced subsurface imaging **affordable and accessible** for smaller Indian exploration companies.

---

## 💡 The Core Idea (in 3 Lines)
1. **Input:** 3D seismic volumes of underground rock layers  
2. **AI Output:** Automatically identifies faults, layers, and potential drilling zones  
3. **Innovation:** Optimized to be **70% lighter** than commercial models — runs on low-end hardware

---

## 🎯 Project Goals
| Goal | Description |
|------|--------------|
| **Accessibility** | Enable small exploration teams to use seismic AI tools without GPU clusters |
| **Accuracy** | Achieve comparable accuracy to commercial fault detection models |
| **Speed** | Process medium-sized datasets in **under 5 minutes** on a standard laptop |
| **Cost Efficiency** | Replace ₹50 lakh hardware setups with ₹60k laptops |

---

## 🧩 Why It Matters
Traditional seismic interpretation software (like Schlumberger’s Petrel or Halliburton’s DecisionSpace) costs **tens of lakhs** and needs **GPU workstations**.  
HydroTrace AI bridges that gap — it’s the **“mobile app” version** of those tools: simpler, faster, and built for accessibility.

---

## 🧠 How It Works
1. **Data Input**: Load SEG-Y seismic volumes (e.g., Netherlands F3 dataset)  
2. **Preprocessing**: Normalize, slice into 2D/3D patches  
3. **AI Model**: Fine-tuned **MobileNetV2** CNN for fault and layer detection  
4. **Visualization**: Display predictions and overlays on seismic slices  
5. **Dashboard**: Streamlit web interface for easy user interaction  

---

## 🪜 Development Plan (3-Month Roadmap)

### **Month 1 – Foundation**
- Learn seismic interpretation basics  
- Explore F3 dataset and visualize slices  
- Build a simple 2D CNN baseline for fault detection  
- Transition to 3D volume analysis  

**Checkpoint:** Model reliably detects at least one geological feature.

---

### **Month 2 – Optimization**
- Apply **transfer learning** (train on Netherlands F3 → test on New Zealand Parihaka)  
- Implement **model compression** (quantization, pruning)  
- Benchmark speed and memory use  
- Build a **Streamlit dashboard**

**Checkpoint:** Model runs on a regular laptop in <5 minutes.

---

### **Month 3 – Validation & Presentation**
- Test on multiple datasets  
- Compare accuracy and runtime with published models  
- Document findings and limitations  
- Create demo video + cost comparison slides  

---

## 🔧 Tech Stack
| Category | Tools / Libraries |
|-----------|------------------|
| Language | Python 3.8+ |
| AI Framework | TensorFlow / PyTorch |
| Visualization | Matplotlib, Seaborn |
| Seismic Data Handling | `segyio`, `OpendTect` |
| Web App Interface | Streamlit |
| Model Architecture | MobileNetV2 (fine-tuned) |

---

## 📦 Datasets
| Dataset | Source | Description |
|----------|---------|-------------|
| **Netherlands F3 Block** | [Terranubis F3 Dataset](https://terranubis.com/datainfo/Netherlands-Offshore-F3-Block-Complete) | Public 3D seismic data used for training |
| **Parihaka (New Zealand)** | Open seismic dataset | Used for testing transfer learning and model robustness |

---

## 📊 Success Metrics
| Metric | Target |
|---------|--------|
| Fault Detection Accuracy | ≥ 70% |
| Model Size Reduction | ≥ 60% |
| Inference Time | < 5 minutes (laptop) |
| Hardware Requirement | CPU-only, 8GB RAM |

---

## 👥 Team Roles
| Discipline | Responsibilities |
|-------------|------------------|
| **Chemical / Petroleum Engineering** | Geological interpretation, defining exploration features, validating fault outputs |
| **Computer Science** | Model training, optimization, dashboard development, benchmarking |

**Daily 15-min sync:**  
> ChemE → “Does this make geological sense?”  
> CS → “Does it run fast and predict correctly?”

---

## 📅 Quick Start (Week 1 Checklist)
1. Download **Netherlands F3 Dataset** → [link](https://terranubis.com/datainfo/Netherlands-Offshore-F3-Block-Complete)  
2. Install **OpendTect** or **Python `segyio`**  
3. Visualize a seismic slice:
   ```python
   import segyio, numpy as np, matplotlib.pyplot as plt

   with segyio.open("F3.sgy", "r", ignore_geometry=True) as f:
       data = segyio.tools.cube(f)
   plt.imshow(data[:, :, 100], cmap='gray')
   plt.title("Seismic Inline Slice (F3)")
   plt.show()
