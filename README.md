# 📊 Sorting Algorithm Visualizer

An interactive **Sorting Algorithm Visualizer** built with **Python** and **Pygame** to demonstrate how different sorting algorithms work through real-time animations.

The application allows users to generate random datasets, switch between multiple sorting algorithms, choose ascending or descending order, and observe each algorithm's execution step by step.

---

## ✨ Features

- 🎲 Generate random datasets
- 📈 Sort in **Ascending** or **Descending** order
- ⚡ Real-time visualization of sorting operations
- 🎨 Color-coded comparisons, swaps, heap operations, and sorted elements
- ⌨️ Keyboard shortcuts for selecting algorithms
- 🏗️ Modular project structure with each algorithm implemented in a separate file

---

## 🧠 Implemented Algorithms

- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Bucket Sort

---

## 📁 Project Structure

```text
sorting-algorithm-visualizer/
│
├── main.py                 # Main application loop
├── draw.py                 # Drawing utilities and visualization
├── utils.py                # Helper functions
│
├── algorithms/
│   ├── __init__.py
│   ├── bubble_sort.py
│   ├── insertion_sort.py
│   ├── selection_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   ├── heap_sort.py
│   └── bucket_sort.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🎮 Controls

| Key | Action |
|------|--------|
| **R** | Generate a new random dataset |
| **SPACE** | Start sorting |
| **A** | Sort in Ascending order |
| **D** | Sort in Descending order |
| **B** | Bubble Sort |
| **I** | Insertion Sort |
| **S** | Selection Sort |
| **M** | Merge Sort |
| **Q** | Quick Sort |
| **H** | Heap Sort |
| **K** | Bucket Sort *(or whichever key you've assigned)* |

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/jogaraoentenuka/sorting-algorithm-visualizer.git
cd sorting-algorithm-visualizer
```

### Create a virtual environment (Optional)

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python main.py
```

---

## 🛠️ Technologies Used

- Python 3
- Pygame

---

## 📚 Time Complexity

| Algorithm | Best | Average | Worst | Space |
|-----------|------|----------|--------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Bucket Sort | O(n + k) | O(n + k) | O(n²) | O(n + k) |

---

## 🎯 Future Improvements

- Add Radix Sort
- Add Counting Sort
- Add Shell Sort
- Adjustable visualization speed
- Adjustable dataset size
- Pause and resume animation
- Display real-time statistics (comparisons and swaps)
- Add sound effects during sorting
- Display execution time for each algorithm

---

## 📄 License

This project is currently available for educational and personal use.

---

## 👤 Author

**Joy (Jogarao Entenuka)**

GitHub: **https://github.com/jogaraoentenuka**

If you found this project helpful, consider giving the repository a ⭐!
